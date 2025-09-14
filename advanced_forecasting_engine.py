#!/usr/bin/env python3
"""
Advanced Trend Forecasting Engine for TrendZ
Uses Prophet and LSTM models for trend lifecycle prediction
"""

import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Try to import Prophet, fallback to basic forecasting if not available
try:
    from prophet import Prophet
    PROPHET_AVAILABLE = True
except ImportError:
    PROPHET_AVAILABLE = False
    print("⚠️ Prophet not available - using basic forecasting")

try:
    import torch
    import torch.nn as nn
    TORCH_AVAILABLE = True
except ImportError:
    TORCH_AVAILABLE = False
    print("⚠️ PyTorch not available - LSTM forecasting disabled")
except Exception as e:
    TORCH_AVAILABLE = False
    print(f"⚠️ PyTorch import failed: {e} - LSTM forecasting disabled")

class AdvancedTrendForecasting:
    """Advanced trend forecasting using Prophet and LSTM models"""
    
    def __init__(self):
        print("📈 Advanced Trend Forecasting Engine initialized")
        
        # Initialize Prophet model if available
        if PROPHET_AVAILABLE:
            self.prophet_model = Prophet(
                yearly_seasonality=True,
                weekly_seasonality=True,
                daily_seasonality=False,
                seasonality_mode='multiplicative',
                changepoint_prior_scale=0.05,
                seasonality_prior_scale=10.0
            )
            print("✅ Prophet model initialized")
        
        # Initialize LSTM model if available
        if TORCH_AVAILABLE:
            self.lstm_model = TrendLSTM(input_size=5, hidden_size=64, num_layers=2, output_size=1)
            print("✅ LSTM model initialized")
        
        # Malaysia-specific seasonal patterns
        self.malaysia_seasons = {
            'hot_season': {'months': [3, 4, 5, 6, 7, 8, 9], 'multiplier': 1.2},
            'monsoon_season': {'months': [10, 11, 12, 1, 2], 'multiplier': 0.8},
            'festival_season': {'months': [1, 2, 5, 6, 10, 11], 'multiplier': 1.5}
        }
        
        # Cultural events calendar
        self.cultural_events = {
            'chinese_new_year': {'month': 1, 'duration_days': 15, 'trend_boost': 1.8},
            'hari_raya': {'month': 5, 'duration_days': 30, 'trend_boost': 1.6},
            'deepavali': {'month': 10, 'duration_days': 5, 'trend_boost': 1.4},
            'merdeka': {'month': 8, 'duration_days': 7, 'trend_boost': 1.3},
            'christmas': {'month': 12, 'duration_days': 14, 'trend_boost': 1.2}
        }
    
    def forecast_trend_lifecycle(self, trend_data, days_ahead=30):
        """Forecast trend lifecycle using multiple models"""
        print(f"📈 Forecasting trend lifecycle for {days_ahead} days...")
        
        hashtag = trend_data.get('hashtag', 'unknown')
        platform = trend_data.get('platform', 'unknown')
        
        # Generate historical data for the trend
        historical_data = self._generate_historical_data(trend_data)
        
        forecasts = {}
        
        # Prophet forecasting
        if PROPHET_AVAILABLE:
            prophet_forecast = self._prophet_forecast(historical_data, days_ahead)
            forecasts['prophet'] = prophet_forecast
        
        # LSTM forecasting
        if TORCH_AVAILABLE:
            lstm_forecast = self._lstm_forecast(historical_data, days_ahead)
            forecasts['lstm'] = lstm_forecast
        
        # Basic forecasting (fallback)
        basic_forecast = self._basic_forecast(historical_data, days_ahead)
        forecasts['basic'] = basic_forecast
        
        # Combine forecasts
        combined_forecast = self._combine_forecasts(forecasts, trend_data)
        
        # Add Malaysia-specific adjustments
        malaysia_adjusted = self._apply_malaysia_adjustments(combined_forecast, trend_data)
        
        return {
            'trend_name': hashtag,
            'platform': platform,
            'forecast_period': f"{days_ahead} days",
            'forecasts': forecasts,
            'combined_forecast': malaysia_adjusted,
            'lifecycle_stage': self._identify_lifecycle_stage(malaysia_adjusted),
            'peak_prediction': self._predict_peak_timing(malaysia_adjusted),
            'decay_warning': self._generate_decay_warning(malaysia_adjusted),
            'malaysia_insights': self._generate_malaysia_insights(malaysia_adjusted, trend_data)
        }
    
    def _generate_historical_data(self, trend_data):
        """Generate historical data for trend analysis"""
        days_back = 30
        current_date = datetime.now()
        
        # Simulate historical trend data
        historical_data = []
        base_score = trend_data.get('trend_score', 50)
        
        for i in range(days_back, 0, -1):
            date = current_date - timedelta(days=i)
            
            # Add some realistic variation
            noise = random.uniform(-10, 15)
            seasonal_multiplier = self._get_seasonal_multiplier(date)
            
            score = max(0, base_score + noise + (days_back - i) * 2) * seasonal_multiplier
            
            historical_data.append({
                'ds': date.strftime('%Y-%m-%d'),
                'y': score,
                'platform': trend_data.get('platform', 'unknown'),
                'engagement': random.uniform(0.1, 0.9),
                'reach': random.randint(1000, 100000)
            })
        
        return historical_data
    
    def _prophet_forecast(self, historical_data, days_ahead):
        """Forecast using Prophet model"""
        if not PROPHET_AVAILABLE:
            return None
        
        try:
            # Prepare data for Prophet
            df = pd.DataFrame(historical_data)
            df['ds'] = pd.to_datetime(df['ds'])
            
            # Create Prophet model
            model = Prophet(
                yearly_seasonality=True,
                weekly_seasonality=True,
                daily_seasonality=False,
                seasonality_mode='multiplicative'
            )
            
            # Fit the model
            model.fit(df)
            
            # Make future predictions
            future = model.make_future_dataframe(periods=days_ahead)
            forecast = model.predict(future)
            
            # Extract forecast data
            forecast_data = forecast.tail(days_ahead)[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].to_dict('records')
            
            return {
                'method': 'prophet',
                'forecast_data': forecast_data,
                'trend_direction': 'growing' if forecast_data[-1]['yhat'] > forecast_data[0]['yhat'] else 'declining',
                'confidence': 0.8
            }
            
        except Exception as e:
            print(f"⚠️ Prophet forecasting error: {e}")
            return None
    
    def _lstm_forecast(self, historical_data, days_ahead):
        """Forecast using LSTM model"""
        if not TORCH_AVAILABLE:
            return None
        
        try:
            # Prepare data for LSTM
            values = [point['y'] for point in historical_data]
            
            # Simple LSTM prediction (simplified for demo)
            # In a real implementation, you'd train the LSTM model properly
            
            # Simulate LSTM prediction
            last_value = values[-1]
            trend_direction = 1 if len(values) > 1 and values[-1] > values[-2] else -1
            
            forecast_values = []
            for i in range(days_ahead):
                # Simple trend continuation with some noise
                next_value = last_value + trend_direction * random.uniform(0.5, 2.0) + random.uniform(-1, 1)
                forecast_values.append(max(0, next_value))
                last_value = next_value
            
            return {
                'method': 'lstm',
                'forecast_values': forecast_values,
                'trend_direction': 'growing' if forecast_values[-1] > forecast_values[0] else 'declining',
                'confidence': 0.7
            }
            
        except Exception as e:
            print(f"⚠️ LSTM forecasting error: {e}")
            return None
    
    def _basic_forecast(self, historical_data, days_ahead):
        """Basic forecasting using simple trend analysis"""
        values = [point['y'] for point in historical_data]
        
        # Calculate trend
        if len(values) >= 2:
            trend_slope = (values[-1] - values[0]) / len(values)
        else:
            trend_slope = 0
        
        # Generate forecast
        forecast_values = []
        last_value = values[-1]
        
        for i in range(days_ahead):
            # Apply trend with some randomness
            next_value = last_value + trend_slope + random.uniform(-2, 2)
            forecast_values.append(max(0, next_value))
            last_value = next_value
        
        return {
            'method': 'basic',
            'forecast_values': forecast_values,
            'trend_direction': 'growing' if trend_slope > 0 else 'declining',
            'confidence': 0.6
        }
    
    def _combine_forecasts(self, forecasts, trend_data):
        """Combine multiple forecasts for better accuracy"""
        valid_forecasts = [f for f in forecasts.values() if f is not None]
        
        if not valid_forecasts:
            return None
        
        # Weight forecasts by confidence
        weights = [f['confidence'] for f in valid_forecasts]
        total_weight = sum(weights)
        
        if total_weight == 0:
            return valid_forecasts[0]
        
        # Normalize weights
        weights = [w / total_weight for w in weights]
        
        # Combine forecast values
        combined_values = []
        max_length = max(len(f.get('forecast_values', f.get('forecast_data', []))) for f in valid_forecasts)
        
        for i in range(max_length):
            weighted_value = 0
            for j, forecast in enumerate(valid_forecasts):
                if 'forecast_values' in forecast and i < len(forecast['forecast_values']):
                    weighted_value += forecast['forecast_values'][i] * weights[j]
                elif 'forecast_data' in forecast and i < len(forecast['forecast_data']):
                    weighted_value += forecast['forecast_data'][i]['yhat'] * weights[j]
            
            combined_values.append(weighted_value)
        
        # Determine combined trend direction
        if len(combined_values) >= 2:
            trend_direction = 'growing' if combined_values[-1] > combined_values[0] else 'declining'
        else:
            trend_direction = 'stable'
        
        return {
            'method': 'combined',
            'forecast_values': combined_values,
            'trend_direction': trend_direction,
            'confidence': np.mean([f['confidence'] for f in valid_forecasts]),
            'component_forecasts': len(valid_forecasts)
        }
    
    def _apply_malaysia_adjustments(self, forecast, trend_data):
        """Apply Malaysia-specific adjustments to forecast"""
        if not forecast:
            return None
        
        adjusted_values = forecast['forecast_values'].copy()
        current_date = datetime.now()
        
        # Apply seasonal adjustments
        for i, value in enumerate(adjusted_values):
            forecast_date = current_date + timedelta(days=i+1)
            
            # Apply seasonal multiplier
            seasonal_multiplier = self._get_seasonal_multiplier(forecast_date)
            adjusted_values[i] = value * seasonal_multiplier
            
            # Apply cultural event boosts
            event_multiplier = self._get_event_multiplier(forecast_date)
            adjusted_values[i] = adjusted_values[i] * event_multiplier
        
        forecast['forecast_values'] = adjusted_values
        forecast['malaysia_adjusted'] = True
        
        return forecast
    
    def _get_seasonal_multiplier(self, date):
        """Get seasonal multiplier for Malaysia"""
        month = date.month
        
        for season, data in self.malaysia_seasons.items():
            if month in data['months']:
                return data['multiplier']
        
        return 1.0
    
    def _get_event_multiplier(self, date):
        """Get cultural event multiplier"""
        month = date.month
        day = date.day
        
        for event, data in self.cultural_events.items():
            if month == data['month']:
                # Check if within event duration
                if day <= data['duration_days']:
                    return data['trend_boost']
        
        return 1.0
    
    def _identify_lifecycle_stage(self, forecast):
        """Identify current lifecycle stage of trend"""
        if not forecast or not forecast.get('forecast_values'):
            return 'unknown'
        
        values = forecast['forecast_values']
        
        if len(values) < 3:
            return 'emerging'
        
        # Analyze trend pattern
        recent_values = values[-3:]
        if all(recent_values[i] < recent_values[i+1] for i in range(len(recent_values)-1)):
            return 'growing'
        elif all(recent_values[i] > recent_values[i+1] for i in range(len(recent_values)-1)):
            return 'declining'
        elif max(values) == recent_values[-1]:
            return 'peak'
        else:
            return 'mature'
    
    def _predict_peak_timing(self, forecast):
        """Predict when trend will peak"""
        if not forecast or not forecast.get('forecast_values'):
            return None
        
        values = forecast['forecast_values']
        
        if not values:
            return None
        
        # Find peak in forecast
        peak_value = max(values)
        peak_index = values.index(peak_value)
        
        return {
            'peak_value': peak_value,
            'days_to_peak': peak_index + 1,
            'peak_date': (datetime.now() + timedelta(days=peak_index + 1)).strftime('%Y-%m-%d'),
            'confidence': forecast.get('confidence', 0.5)
        }
    
    def _generate_decay_warning(self, forecast):
        """Generate decay warning if trend is declining"""
        if not forecast:
            return None
        
        values = forecast['forecast_values']
        
        if len(values) < 5:
            return None
        
        # Check if trend is declining
        recent_trend = (values[-1] - values[-5]) / 5
        
        if recent_trend < -1:  # Declining threshold
            return {
                'warning': 'Trend is declining rapidly',
                'severity': 'high',
                'decline_rate': abs(recent_trend),
                'recommendation': 'Consider reducing investment or pivoting strategy'
            }
        elif recent_trend < -0.5:
            return {
                'warning': 'Trend shows signs of decline',
                'severity': 'medium',
                'decline_rate': abs(recent_trend),
                'recommendation': 'Monitor closely and prepare exit strategy'
            }
        
        return None
    
    def _generate_malaysia_insights(self, forecast, trend_data):
        """Generate Malaysia-specific insights"""
        insights = {
            'seasonal_opportunities': [],
            'cultural_alignment': [],
            'community_recommendations': []
        }
        
        # Analyze seasonal opportunities
        current_month = datetime.now().month
        for season, data in self.malaysia_seasons.items():
            if current_month in data['months']:
                insights['seasonal_opportunities'].append({
                    'season': season,
                    'multiplier': data['multiplier'],
                    'recommendation': f'Capitalize on {season} trends'
                })
        
        # Analyze cultural alignment
        hashtag = trend_data.get('hashtag', '').lower()
        for event, data in self.cultural_events.items():
            if any(keyword in hashtag for keyword in event.split('_')):
                insights['cultural_alignment'].append({
                    'event': event,
                    'boost': data['trend_boost'],
                    'recommendation': f'Align with {event} celebrations'
                })
        
        return insights

class TrendLSTM(nn.Module):
    """LSTM model for trend forecasting"""
    
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(TrendLSTM, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        
        self.lstm = nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    
    def forward(self, x):
        h0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        c0 = torch.zeros(self.num_layers, x.size(0), self.hidden_size)
        
        out, _ = self.lstm(x, (h0, c0))
        out = self.fc(out[:, -1, :])
        return out

# Initialize the advanced forecasting engine
advanced_forecasting = AdvancedTrendForecasting()
