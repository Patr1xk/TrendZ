#!/usr/bin/env python3
"""
Simplified ML Service for TrendZ
Fast, rule-based predictions for real-time analysis
"""
import random
import numpy as np
from datetime import datetime, timedelta

class SimpleMLService:
    """Simplified ML service for faster execution"""
    
    def __init__(self):
        print("✅ Simple ML Service initialized")
    
    def predict_trend_score(self, video_data):
        """Predict trend score based on engagement metrics"""
        
        # Get engagement metrics
        views = video_data.get('viewCount', 0)
        likes = video_data.get('likeCount', 0)
        comments = video_data.get('commentCount', 0)
        engagement_rate = video_data.get('engagement_rate', 0)
        
        # Calculate base score from engagement
        if views > 0:
            like_ratio = likes / views
            comment_ratio = comments / views
            
            # Engagement velocity (higher is better)
            engagement_velocity = (like_ratio + comment_ratio) * 100
            
            # Base score calculation
            base_score = min(engagement_velocity * 50, 100)
            
            # Platform multipliers
            platform = video_data.get('platform', 'instagram').lower()
            platform_multipliers = {
                'tiktok': 1.2,    # TikTok trends spread faster
                'instagram': 1.0,  # Baseline
                'youtube': 0.9,   # Slower viral spread
                'twitter': 1.1    # Fast but shorter lifespan
            }
            
            platform_score = base_score * platform_multipliers.get(platform, 1.0)
            
            # Hashtag quality boost
            hashtags = video_data.get('all_hashtags', [])
            if len(hashtags) > 3:
                platform_score *= 1.1
            
            # Recency boost (newer content scores higher)
            published_at = video_data.get('publishedAt')
            if published_at:
                if isinstance(published_at, str):
                    published_at = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                days_old = (datetime.now() - published_at.replace(tzinfo=None)).days
                recency_multiplier = max(0.7, 1.0 - (days_old / 30))
                platform_score *= recency_multiplier
            
            return max(10, min(100, int(platform_score)))
        
        return random.randint(40, 85)
    
    def predict_lifecycle(self, video_data):
        """Predict trend lifecycle stage"""
        
        views = video_data.get('viewCount', 0)
        engagement_rate = video_data.get('engagement_rate', 0)
        trend_score = self.predict_trend_score(video_data)
        
        # Rule-based lifecycle prediction
        if trend_score >= 80 and engagement_rate > 0.05:
            return 'Emerging'
        elif trend_score >= 60 and engagement_rate > 0.03:
            return 'Growing'
        elif trend_score >= 40 and engagement_rate > 0.02:
            return 'Mature'
        else:
            return random.choice(['Mature', 'Decay'])
    
    def predict_roi(self, video_data):
        """Predict ROI potential"""
        
        views = video_data.get('viewCount', 0)
        engagement_rate = video_data.get('engagement_rate', 0)
        trend_score = self.predict_trend_score(video_data)
        
        # Base ROI calculation
        base_roi = (trend_score * engagement_rate * 100) / 10
        
        # Platform-specific ROI adjustments
        platform = video_data.get('platform', 'instagram').lower()
        platform_roi_multipliers = {
            'tiktok': 1.3,      # High conversion potential
            'instagram': 1.0,   # Baseline
            'youtube': 1.2,     # Good for detailed content
            'twitter': 0.8      # Lower conversion
        }
        
        roi_score = base_roi * platform_roi_multipliers.get(platform, 1.0)
        
        # Category adjustments
        category = video_data.get('category', 'beauty')
        if 'skincare' in str(category).lower():
            roi_score *= 1.2  # Skincare has high ROI
        elif 'makeup' in str(category).lower():
            roi_score *= 1.1  # Makeup has good ROI
        
        return max(20, min(200, int(roi_score)))
    
    def analyze_sentiment(self, text_data):
        """Analyze sentiment from text"""
        
        if not text_data:
            return 0.6  # Neutral-positive default
        
        # Simple keyword-based sentiment
        positive_words = ['love', 'amazing', 'perfect', 'beautiful', 'gorgeous', 'stunning']
        negative_words = ['hate', 'ugly', 'terrible', 'awful', 'bad', 'worst']
        
        text_lower = str(text_data).lower()
        
        positive_count = sum(1 for word in positive_words if word in text_lower)
        negative_count = sum(1 for word in negative_words if word in text_lower)
        
        if positive_count > negative_count:
            return min(0.9, 0.6 + (positive_count * 0.1))
        elif negative_count > positive_count:
            return max(0.2, 0.6 - (negative_count * 0.1))
        else:
            return 0.6
    
    def predict_fomo_timer(self, video_data):
        """Predict days until FOMO peaks"""
        
        trend_score = self.predict_trend_score(video_data)
        lifecycle = self.predict_lifecycle(video_data)
        
        # FOMO timing based on lifecycle and score
        if lifecycle == 'Emerging':
            if trend_score >= 80:
                return random.randint(3, 7)   # Very urgent
            else:
                return random.randint(7, 14)  # Urgent
        elif lifecycle == 'Growing':
            return random.randint(14, 21)      # Moderate urgency
        elif lifecycle == 'Mature':
            return random.randint(21, 30)      # Lower urgency
        else:
            return random.randint(30, 60)      # No urgency
    
    def analyze_trend_direction(self, video_data):
        """Analyze if trend is rising or declining"""
        
        trend_score = self.predict_trend_score(video_data)
        engagement_rate = video_data.get('engagement_rate', 0)
        views = video_data.get('viewCount', 0)
        
        # Combine multiple factors for direction analysis
        momentum_score = (trend_score + (engagement_rate * 1000) + (views / 10000)) / 3
        
        # Add some randomness for realistic variation
        momentum_score += random.uniform(-10, 10)
        
        if momentum_score >= 70:
            return 'Rising'
        elif momentum_score >= 50:
            return 'Stable'
        elif momentum_score >= 30:
            return 'Declining'
        else:
            return 'Fading'

# Initialize the service
ml_service = SimpleMLService()
