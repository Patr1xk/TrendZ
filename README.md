# ✨ TrendSpotter - AI-Powered Beauty Trend Analysis

## 🎯 Project Overview

TrendSpotter is an AI-powered dashboard that identifies emerging beauty trends using multimodal data analysis, predicts their entire lifecycle (from emerging to decay), and provides actionable insights with a clear "Opportunity Score" for L'Oréal.

## 🚀 Core Features

### A. Trend Detection Engine
- **Multi-Modal Analysis**: Audio snippets, text & hashtags, and visual aesthetics
- **Real-time Monitoring**: Track mention volume, velocity, and acceleration
- **Smart Classification**: Identify rising aesthetics, colors, and makeup styles

### B. Trend Analysis & Prediction
- **Lifecycle Curve Visualization**: Shows trend journey through 4 stages (Emerging → Growing → Mature → Decay)
- **Predictive FOMO Timer**: Estimates peak engagement and decay timing
- **Optimal Entry Point**: Highlights the best time to join a trend

### C. Audience & Context Analysis
- **Demographic Segmentation**: Age group breakdown (Gen Z, Millennials, etc.)
- **Cross-Platform View**: Performance across TikTok, Instagram, YouTube, Twitter, Pinterest
- **Interest Classification**: Beauty, Lifestyle, Health categories

### D. Actionable Insights
- **TrendScore**: Single metric (0-100) combining growth, audience fit, and platform strength
- **Opportunity Meter**: Clear visual call-to-action for trend participation
- **Strategic Recommendations**: Content strategy, product development, and investment priorities

## 🛠️ Technology Stack

- **Frontend**: Streamlit (Python web framework)
- **Data Visualization**: Plotly, Matplotlib, Seaborn
- **Data Processing**: Pandas, NumPy
- **Machine Learning**: Scikit-learn (for trend prediction)
- **Styling**: Custom CSS with L'Oréal brand colors

## 📦 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Quick Start

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd TrendSpotter
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application**
   ```bash
   streamlit run app.py
   ```

4. **Open your browser**
   - Navigate to `http://localhost:8501`
   - The dashboard will automatically open

## 🎮 How to Use

### 1. Trend Selection
- Use the sidebar to select from available beauty trends
- Choose from: GlassSkin, Dewy Makeup, Clean Beauty, Contour Makeup, Matte Lipstick, Viral Skincare

### 2. Analyze the Dashboard
- **Main Chart**: View the trend lifecycle curve with growth rate and acceleration
- **TrendScore**: See the overall opportunity score (0-100)
- **Opportunity Meter**: Understand the current lifecycle stage
- **FOMO Timer**: Get estimated days of peak engagement remaining

### 3. Explore Insights
- **Audience Demographics**: Pie chart showing age group distribution
- **Platform Performance**: Bar chart comparing social media platforms
- **Actionable Recommendations**: Strategic guidance for L'Oréal teams

## 🔧 Customization

### Adding New Trends
1. Update the `available_trends` list in `app.py`
2. Modify the `generate_trend_data()` function for custom trend patterns
3. Adjust audience and platform data generation functions

### Modifying the Algorithm
1. Update the `calculate_trend_score()` function for different scoring weights
2. Modify the `predict_trend_lifecycle()` function for custom lifecycle logic
3. Adjust the FOMO timer calculation in the main function

### Branding Changes
1. Update CSS variables in the custom styles section
2. Modify the header and footer content
3. Change color schemes in the gradient backgrounds

## 📊 Mock Data Structure

The prototype uses sophisticated mock data generation:

- **Trend Data**: 30-day time series with realistic growth patterns
- **Audience Data**: Demographic breakdowns based on trend type
- **Platform Data**: Cross-platform performance metrics
- **Lifecycle Stages**: Automatic classification based on growth patterns

## 🎯 Hackathon Demo Tips

### 1. **The "Money Shot"**
- Start with GlassSkin trend (high score, emerging stage)
- Show the TrendScore prominently
- Demonstrate the Opportunity Meter in action

### 2. **Interactive Elements**
- Switch between different trends to show varying scores
- Highlight the FOMO Timer for emerging trends
- Show how recommendations change based on lifecycle stage

### 3. **Key Talking Points**
- **Multi-modal Analysis**: Explain how audio, text, and visuals are integrated
- **Predictive Power**: Demonstrate the lifecycle prediction capabilities
- **Actionable Insights**: Show how the dashboard drives business decisions

### 4. **Technical Highlights**
- **Real-time Updates**: Data refreshes with each trend selection
- **Responsive Design**: Works on all screen sizes
- **Professional UI**: L'Oréal-branded interface

## 🔮 Future Enhancements

### Phase 2 Features
- **Live Data Integration**: Real-time social media API connections
- **Advanced ML Models**: Deep learning for trend prediction
- **Audio Analysis**: Real-time sound trend detection
- **Visual Recognition**: AI-powered makeup style identification

### Phase 3 Features
- **Global Expansion**: Multi-language and regional trend analysis
- **Competitor Analysis**: Track competitor brand mentions
- **ROI Calculator**: Estimate potential returns on trend investments
- **Automated Alerts**: Push notifications for emerging trends

## 📁 Project Structure

```
TrendSpotter/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── code.py            # Legacy file (can be removed)
```

## 🤝 Contributing

This is a hackathon prototype built for L'Oréal Innovation Lab. For questions or collaboration opportunities, please contact the development team.

## 📄 License

Built for L'Oréal Innovation Lab Hackathon 2024. All rights reserved.

---

**✨ Built with ❤️ for the future of beauty trend analysis ✨** 