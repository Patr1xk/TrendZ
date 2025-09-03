import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression
from datetime import datetime, timedelta
import json
from pathlib import Path

# Page configuration
st.set_page_config(
    page_title="TrendSpotter - AI-Powered Beauty Trend Analysis",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for L'Oréal branding
st.markdown("""
<style>
    .main-header {
        background: linear-gradient(90deg, #FF6B9D, #C44569);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin-bottom: 2rem;
    }
    .trend-score {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    .opportunity-meter {
        background: linear-gradient(90deg, #56ab2f, #a8e6cf);
        padding: 1rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
    }
    .metric-card {
        background: white;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        border-left: 4px solid #FF6B9D;
    }
</style>
""", unsafe_allow_html=True)

# Mock data generation functions
def generate_trend_data(trend_name, days=30):
    """Generate mock trend data for demonstration"""
    dates = pd.date_range(start=datetime.now() - timedelta(days=days), periods=days, freq='D')
    
    # Generate realistic trend lifecycle data
    if trend_name.lower() in ['glassskin', 'dewy makeup', 'clean beauty']:
        # Growing trend
        mentions = np.concatenate([
            np.random.poisson(50, 10),  # Emerging
            np.random.poisson(150, 10),  # Growing
            np.random.poisson(300, 10)   # Peak
        ])
    elif trend_name.lower() in ['contour makeup', 'matte lipstick']:
        # Mature trend
        mentions = np.concatenate([
            np.random.poisson(300, 15),  # Peak
            np.random.poisson(200, 15)   # Slight decline
        ])
    else:
        # Decaying trend
        mentions = np.concatenate([
            np.random.poisson(400, 10),  # Peak
            np.random.poisson(200, 10),  # Decline
            np.random.poisson(50, 10)    # Decay
        ])
    
    # Ensure we have enough data points
    if len(mentions) < days:
        mentions = np.pad(mentions, (0, days - len(mentions)), mode='edge')
    else:
        mentions = mentions[:days]
    
    return pd.DataFrame({
        'date': dates,
        'mentions': mentions,
        'growth_rate': np.gradient(mentions),
        'acceleration': np.gradient(np.gradient(mentions))
    })

def load_trend_csv(uploaded_file_or_path, trend_name_hint=None):
    """Load time-series CSV with columns: date, mentions. Returns normalized DataFrame or None on failure."""
    try:
        if uploaded_file_or_path is None:
            return None
        df = pd.read_csv(uploaded_file_or_path)
        # Normalize column names
        cols = {c.lower().strip(): c for c in df.columns}
        date_col = cols.get('date') or cols.get('timestamp')
        mentions_col = cols.get('mentions') or cols.get('count') or cols.get('volume')
        if date_col is None or mentions_col is None:
            return None
        df = df[[date_col, mentions_col]].rename(columns={date_col: 'date', mentions_col: 'mentions'})
        df['date'] = pd.to_datetime(df['date'])
        df = df.sort_values('date')
        df['mentions'] = pd.to_numeric(df['mentions'], errors='coerce').fillna(0)
        df['growth_rate'] = np.gradient(df['mentions'])
        df['acceleration'] = np.gradient(np.gradient(df['mentions']))
        return df
    except Exception:
        return None

def create_forecast(trend_data, horizon_days=14, window=10):
    """Create a simple linear regression forecast on the latest window."""
    if len(trend_data) < max(5, window):
        window = min(window, len(trend_data))
    y = trend_data['mentions'].tail(window).values.reshape(-1, 1)
    X = np.arange(window).reshape(-1, 1)
    model = LinearRegression()
    model.fit(X, y)
    future_X = np.arange(window, window + horizon_days).reshape(-1, 1)
    y_pred = model.predict(future_X).ravel()
    last_date = trend_data['date'].iloc[-1]
    future_dates = pd.date_range(start=last_date + pd.Timedelta(days=1), periods=horizon_days, freq='D')
    forecast_df = pd.DataFrame({'date': future_dates, 'mentions': np.maximum(0, y_pred)})
    return forecast_df

def predict_lifecycle_with_forecast(trend_data, forecast_horizon=14):
    """Determine lifecycle stage and FOMO using recent derivatives and short-term forecast."""
    forecast_df = create_forecast(trend_data, horizon_days=forecast_horizon)
    recent_growth = trend_data['growth_rate'].tail(7).mean()
    recent_accel = trend_data['acceleration'].tail(7).mean()

    if recent_growth > 30 and recent_accel > 0:
        stage = "Emerging"
        color = "green"
    elif recent_growth > 10 and recent_accel >= 0:
        stage = "Growing"
        color = "blue"
    elif recent_growth > -10:
        stage = "Mature"
        color = "orange"
    else:
        stage = "Decaying"
        color = "red"

    combined = pd.concat([
        trend_data[['date', 'mentions']],
        forecast_df[['date', 'mentions']]
    ], ignore_index=True)
    peak_idx = combined['mentions'].idxmax()
    peak_date = combined.loc[peak_idx, 'date']
    today = trend_data['date'].iloc[-1]
    days_to_peak = (peak_date.date() - today.date()).days

    peak_value = combined['mentions'].max()
    threshold = 0.9 * peak_value
    future_mask = combined['date'] >= today
    above_threshold = combined[future_mask & (combined['mentions'] >= threshold)]
    remaining_peak_days = above_threshold['date'].nunique()

    if days_to_peak > 0:
        fomo_text = f"Trend expected to peak in {days_to_peak} days; {remaining_peak_days} high-impact days ahead."
    elif days_to_peak == 0:
        fomo_text = "Trend is peaking now — act immediately for maximum impact!"
    else:
        days_since_peak = abs(days_to_peak)
        fomo_text = f"Peak passed {days_since_peak} days ago; impact declining."

    return stage, fomo_text, color, forecast_df, peak_date, remaining_peak_days

def generate_audience_data(trend_name):
    """Generate mock audience demographics data"""
    if trend_name.lower() in ['glassskin', 'dewy makeup']:
        return {
            'Gen Z (16-24)': 65,
            'Millennials (25-40)': 25,
            'Gen X (41-56)': 8,
            'Boomers (57+)': 2
        }
    else:
        return {
            'Gen Z (16-24)': 45,
            'Millennials (25-40)': 40,
            'Gen X (41-56)': 12,
            'Boomers (57+)': 3
        }

def generate_platform_data(trend_name):
    """Generate mock cross-platform data"""
    platforms = ['TikTok', 'Instagram', 'YouTube', 'Twitter', 'Pinterest']
    if trend_name.lower() in ['glassskin', 'dewy makeup']:
        values = [45, 30, 15, 7, 3]
    else:
        values = [35, 40, 15, 8, 2]
    
    return dict(zip(platforms, values))

def calculate_trend_score(trend_data, audience_data, platform_data):
    """Calculate the TrendScore (0-100)"""
    # Growth rate score (0-40 points)
    avg_growth = trend_data['growth_rate'].mean()
    growth_score = min(40, max(0, (avg_growth + 100) / 2))
    
    # Audience fit score (0-30 points)
    gen_z_percentage = audience_data.get('Gen Z (16-24)', 0)
    audience_score = (gen_z_percentage / 100) * 30
    
    # Platform strength score (0-30 points)
    tiktok_percentage = platform_data.get('TikTok', 0)
    platform_score = (tiktok_percentage / 100) * 30
    
    total_score = growth_score + audience_score + platform_score
    return min(100, max(0, total_score))

def predict_trend_lifecycle(trend_data):
    # Backward-compatible wrapper using regression-enhanced prediction
    stage, fomo_text, color, _, _, _ = predict_lifecycle_with_forecast(trend_data)
    return stage, fomo_text, color

def create_lifecycle_curve(trend_data, trend_name):
    """Create the main lifecycle curve visualization"""
    fig = go.Figure()
    
    # Add the main trend line
    fig.add_trace(go.Scatter(
        x=trend_data['date'],
        y=trend_data['mentions'],
        mode='lines+markers',
        name='Mentions',
        line=dict(color='#FF6B9D', width=3),
        marker=dict(size=8)
    ))

    # Optional forecast line
    try:
        forecast_df = create_forecast(trend_data)
        fig.add_trace(go.Scatter(
            x=forecast_df['date'],
            y=forecast_df['mentions'],
            mode='lines',
            name='Forecast',
            line=dict(color='#222222', width=2, dash='dot')
        ))
    except Exception:
        pass
    
    # Add growth rate line
    fig.add_trace(go.Scatter(
        x=trend_data['date'],
        y=trend_data['growth_rate'] + 200,  # Offset for visibility
        mode='lines',
        name='Growth Rate',
        line=dict(color='#667eea', width=2, dash='dash'),
        yaxis='y2'
    ))
    
    # Add acceleration line
    fig.add_trace(go.Scatter(
        x=trend_data['date'],
        y=trend_data['acceleration'] + 400,  # Offset for visibility
        mode='lines',
        name='Acceleration',
        line=dict(color='#56ab2f', width=2, dash='dot'),
        yaxis='y2'
    ))
    
    # Update layout
    fig.update_layout(
        title=f'<b>{trend_name} Trend Lifecycle Analysis</b>',
        xaxis_title='Date',
        yaxis_title='Mentions',
        yaxis2=dict(
            title='Growth Rate & Acceleration',
            overlaying='y',
            side='right'
        ),
        hovermode='x unified',
        template='plotly_white',
        height=500
    )
    
    # Add lifecycle stage annotations
    stages = ['Emerging', 'Growing', 'Mature', 'Decay']
    stage_positions = [0.1, 0.3, 0.6, 0.9]
    
    for stage, pos in zip(stages, stage_positions):
        fig.add_annotation(
            x=trend_data['date'].iloc[int(len(trend_data) * pos)],
            y=trend_data['mentions'].max() * 0.8,
            text=stage,
            showarrow=True,
            arrowhead=2,
            arrowcolor='#FF6B9D',
            font=dict(size=14, color='#FF6B9D')
        )
    
    return fig

# Main application
def main():
    # Header
    st.markdown("""
    <div class="main-header">
        <h1>✨ TrendSpotter ✨</h1>
        <h3>AI-Powered Beauty Trend Analysis Dashboard</h3>
        <p>Powered by L'Oréal Innovation Lab</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Sidebar
    st.sidebar.title("🎯 Trend Selection")
    
    # Trend selector
    available_trends = [
        "GlassSkin", "Dewy Makeup", "Clean Beauty", 
        "Contour Makeup", "Matte Lipstick", "Viral Skincare"
    ]
    
    selected_trend = st.sidebar.selectbox(
        "Choose a trend to analyze:",
        available_trends,
        index=0
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("### 📊 Quick Stats")

    # Optional CSV uploader for PowerBI-like flexibility
    st.sidebar.markdown("### 📥 Upload CSV (date, mentions)")
    uploaded_csv = st.sidebar.file_uploader("Upload a CSV to override mock data", type=["csv"])        
    
    # Generate data for selected trend (CSV override if provided)
    trend_data = None
    if uploaded_csv is not None:
        trend_data = load_trend_csv(uploaded_csv, trend_name_hint=selected_trend)
    if trend_data is None:
        # Fallback to mock
        trend_data = generate_trend_data(selected_trend)
    audience_data = generate_audience_data(selected_trend)
    platform_data = generate_platform_data(selected_trend)
    trend_score = calculate_trend_score(trend_data, audience_data, platform_data)
    stage, fomo_timer, color, forecast_df, peak_date, remaining_peak_days = predict_lifecycle_with_forecast(trend_data)
    
    # Display quick stats in sidebar
    st.sidebar.metric("Current Mentions", f"{trend_data['mentions'].iloc[-1]:,}")
    st.sidebar.metric("Growth Rate", f"{trend_data['growth_rate'].iloc[-1]:.1f}")
    st.sidebar.metric("Lifecycle Stage", stage)
    
    # Main content area
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown(f"## 📈 {selected_trend} Trend Analysis")
        
        # Lifecycle curve
        lifecycle_fig = create_lifecycle_curve(trend_data, selected_trend)
        st.plotly_chart(lifecycle_fig, width='stretch')
        
        # Trend insights
        st.markdown("### 🔍 Trend Insights")
        col1_1, col1_2, col1_3, col1_4 = st.columns(4)
        
        with col1_1:
            st.metric("Peak Mentions", f"{trend_data['mentions'].max():,}")
        
        with col1_2:
            st.metric("Velocity (Growth)", f"{trend_data['growth_rate'].iloc[-1]:.1f}")
        
        with col1_3:
            st.metric("Acceleration", f"{trend_data['acceleration'].iloc[-1]:.1f}")

        with col1_4:
            st.metric("Peak Date", peak_date.strftime('%Y-%m-%d'))

        st.info("Optimal Entry: when acceleration turns positive and velocity > 10. You're currently in: " + stage)
    
    with col2:
        # TrendScore
        st.markdown(f"""
        <div class="trend-score">
            <h2>🎯 TrendScore</h2>
            <h1>{trend_score:.0f}/100</h1>
            <p>Combined growth, audience & platform strength</p>
        </div>
        """, unsafe_allow_html=True)
        
        # Opportunity Meter
        st.markdown(f"""
        <div class="opportunity-meter">
            <h3>🚀 Opportunity Meter</h3>
            <h4 style="color: {color};">{stage}</h4>
            <p>{fomo_timer}</p>
        </div>
        """, unsafe_allow_html=True)

        # KPI Gauge (PowerBI-style)
        gauge = go.Figure(go.Indicator(
            mode="gauge+number",
            value=trend_score,
            number={'suffix': "/100"},
            gauge={
                'axis': {'range': [0, 100]},
                'bar': {'color': '#764ba2'},
                'steps': [
                    {'range': [0, 40], 'color': '#f8d7da'},
                    {'range': [40, 70], 'color': '#fff3cd'},
                    {'range': [70, 100], 'color': '#d4edda'}
                ]
            },
            title={'text': 'Opportunity Gauge'}
        ))
        gauge.update_layout(height=260, margin=dict(l=10, r=10, t=40, b=0))
        st.plotly_chart(gauge, width='stretch')
        
        # FOMO Timer (regression-driven)
        st.markdown(f"""
        <div class="metric-card">
            <h4>⏰ FOMO Timer</h4>
            <p>{fomo_timer}</p>
        </div>
        """, unsafe_allow_html=True)
    
    # Audience and Platform Analysis
    st.markdown("---")
    st.markdown("## 👥 Audience & Platform Analysis")
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("### 🎭 Audience Demographics")
        
        # Audience pie chart
        audience_df = pd.DataFrame(list(audience_data.items()), columns=['Age Group', 'Percentage'])
        fig_audience = px.pie(
            audience_df, 
            values='Percentage', 
            names='Age Group',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        fig_audience.update_layout(height=400)
        st.plotly_chart(fig_audience, width='stretch')
        
        # Audience insights
        st.markdown("#### 💡 Key Insights")
        for age_group, percentage in audience_data.items():
            if percentage > 20:
                st.markdown(f"- **{age_group}**: {percentage}% of trend participants")
    
    with col4:
        st.markdown("### 📱 Cross-Platform Performance")
        
        # Platform bar chart
        platform_df = pd.DataFrame(list(platform_data.items()), columns=['Platform', 'Percentage'])
        fig_platform = px.bar(
            platform_df,
            x='Platform',
            y='Percentage',
            color='Percentage',
            color_continuous_scale='Viridis'
        )
        fig_platform.update_layout(height=400)
        st.plotly_chart(fig_platform, width='stretch')
        
        # Platform insights
        st.markdown("#### 💡 Key Insights")
        top_platform = max(platform_data.items(), key=lambda x: x[1])
        st.markdown(f"- **{top_platform[0]}** leads with {top_platform[1]}% of mentions")
        
        if platform_data['TikTok'] > 30:
            st.markdown("- **TikTok** is the primary driver - perfect for short-form content")

    # Creator Archetypes
    st.markdown("---")
    st.markdown("## 🧑‍🎨 Creator Archetypes")
    archetypes = pd.DataFrame({
        'Archetype': [
            'Aesthetic Gurus', 'Derm-Educators', 'Makeup Artists', 'Lifestyle Vloggers', 'Eco-Beauty Advocates'
        ],
        'Share': [28, 18, 24, 20, 10]
    })
    col_ca1, col_ca2 = st.columns([1, 1])
    with col_ca1:
        fig_arch = px.bar(archetypes, x='Archetype', y='Share', color='Share', color_continuous_scale='PuRd')
        fig_arch.update_layout(height=360, xaxis_title='', yaxis_title='Share (%)')
        st.plotly_chart(fig_arch, width='stretch')
    with col_ca2:
        donut = px.pie(archetypes, values='Share', names='Archetype', hole=0.5, color_discrete_sequence=px.colors.sequential.Purples)
        donut.update_layout(height=360)
        st.plotly_chart(donut, width='stretch')

    st.markdown("### 👤 Sample Creators")
    creators = pd.DataFrame({
        'Handle': ['@glowbymia', '@dermfacts', '@artistry_lee', '@dailyviolet', '@eco_bea'],
        'Archetype': ['Aesthetic Gurus', 'Derm-Educators', 'Makeup Artists', 'Lifestyle Vloggers', 'Eco-Beauty Advocates'],
        'Avg Views': ['120k', '95k', '140k', '80k', '60k']
    })
    st.dataframe(creators, width='stretch')
    
    # Actionable Recommendations
    st.markdown("---")
    st.markdown("## 🎯 Actionable Recommendations for L'Oréal")
    
    col5, col6, col7 = st.columns(3)
    
    with col5:
        st.markdown("### 📱 Content Strategy")
        if stage in ["Emerging", "Growing"]:
            st.markdown("""
            - **Immediate Action Required**
            - Create trending content within 48 hours
            - Partner with micro-influencers in the space
            - Launch user-generated content campaigns
            """)
        else:
            st.markdown("""
            - **Strategic Approach**
            - Focus on quality over quantity
            - Target niche audiences
            - Consider product innovation
            """)
    
    with col6:
        st.markdown("### 🎨 Product Development")
        if trend_score > 70:
            st.markdown("""
            - **High Priority**
            - Fast-track product development
            - Consider limited edition releases
            - Invest in marketing campaigns
            """)
        else:
            st.markdown("""
            - **Moderate Priority**
            - Monitor trend evolution
            - Prepare for potential resurgence
            - Focus on core products
            """)
    
    with col7:
        st.markdown("### 💰 Investment Priority")
        if stage == "Emerging" and trend_score > 80:
            st.markdown("""
            - **🚀 Maximum Investment**
            - Allocate significant budget
            - Scale up production capacity
            - Aggressive marketing push
            """)
        elif stage == "Growing":
            st.markdown("""
            - **📈 Strategic Investment**
            - Moderate budget allocation
            - Focus on execution quality
            - Monitor competition
            """)
        else:
            st.markdown("""
            - **⚠️ Conservative Approach**
            - Minimal investment
            - Focus on learning
            - Prepare for next trend
            """)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem;">
        <p>✨ TrendSpotter - AI-Powered Beauty Trend Analysis ✨</p>
        <p>Built for L'Oréal Innovation Lab | Hackathon 2024</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()