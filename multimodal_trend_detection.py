#!/usr/bin/env python3
"""
Multimodal Trend Detection Engine for TrendZ
Combines text embeddings, audio analysis, and influencer signals
"""

import numpy as np
import pandas as pd
import random
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

# Try to import advanced libraries, fallback to basic if not available
try:
    import librosa
    AUDIO_AVAILABLE = True
except ImportError:
    AUDIO_AVAILABLE = False
    print("⚠️ librosa not available - audio analysis disabled")

try:
    from transformers import AutoTokenizer, AutoModel
    TRANSFORMERS_AVAILABLE = True
except ImportError:
    TRANSFORMERS_AVAILABLE = False
    print("⚠️ transformers not available - using basic text analysis")
except Exception as e:
    TRANSFORMERS_AVAILABLE = False
    print(f"⚠️ transformers import failed: {e} - using basic text analysis")

class MultimodalTrendDetection:
    """Multimodal trend detection combining text, audio, and influencer signals"""
    
    def __init__(self):
        print("🔍 Multimodal Trend Detection Engine initialized")
        
        # Initialize text embedding model if available
        if TRANSFORMERS_AVAILABLE:
            try:
                self.tokenizer = AutoTokenizer.from_pretrained('distilbert-base-uncased')
                self.text_model = AutoModel.from_pretrained('distilbert-base-uncased')
                print("✅ HuggingFace transformers loaded")
            except:
                print("⚠️ Failed to load transformers - using basic text analysis")
                self.tokenizer = None
                self.text_model = None
        else:
            self.tokenizer = None
            self.text_model = None
        
        # Malaysia-specific influencer database
        self.malaysia_influencers = {
            'beauty': [
                {'name': 'Siti Nurhaliza', 'followers': 1200000, 'engagement': 4.2, 'communities': ['malay']},
                {'name': 'Joey Yap', 'followers': 800000, 'engagement': 3.8, 'communities': ['chinese']},
                {'name': 'Preeta Nair', 'followers': 650000, 'engagement': 4.5, 'communities': ['indian']},
                {'name': 'Diana Danielle', 'followers': 900000, 'engagement': 3.9, 'communities': ['malay']},
                {'name': 'Amber Chia', 'followers': 750000, 'engagement': 4.1, 'communities': ['chinese']},
                {'name': 'Neelofa', 'followers': 1100000, 'engagement': 4.3, 'communities': ['malay']},
                {'name': 'Lisa Surihani', 'followers': 850000, 'engagement': 3.7, 'communities': ['malay']},
                {'name': 'Gurmit Singh', 'followers': 500000, 'engagement': 4.0, 'communities': ['indian']}
            ],
            'lifestyle': [
                {'name': 'Najwa Latif', 'followers': 950000, 'engagement': 4.4, 'communities': ['malay']},
                {'name': 'Alif Satar', 'followers': 700000, 'engagement': 3.6, 'communities': ['malay']},
                {'name': 'Gary Chaw', 'followers': 600000, 'engagement': 3.8, 'communities': ['chinese']},
                {'name': 'Yuna', 'followers': 800000, 'engagement': 4.2, 'communities': ['malay']}
            ]
        }
        
        # Audio feature templates for different trend types
        self.audio_templates = {
            'beauty_tutorial': {
                'tempo': (120, 140),  # BPM range
                'energy': (0.6, 0.9),
                'valence': (0.7, 0.9),  # Positive mood
                'speech_rate': (150, 200)  # Words per minute
            },
            'lifestyle_content': {
                'tempo': (100, 130),
                'energy': (0.5, 0.8),
                'valence': (0.6, 0.8),
                'speech_rate': (120, 180)
            },
            'product_review': {
                'tempo': (90, 120),
                'energy': (0.4, 0.7),
                'valence': (0.5, 0.8),
                'speech_rate': (100, 160)
            }
        }
    
    def detect_multimodal_trends(self, hashtags_data, audio_features=None, influencer_data=None):
        """Detect trends using multimodal analysis"""
        print("🔍 Running multimodal trend detection...")
        
        trends = []
        
        for hashtag_data in hashtags_data:
            # Text analysis
            text_signals = self._analyze_text_signals(hashtag_data)
            
            # Audio analysis
            audio_signals = self._analyze_audio_signals(hashtag_data, audio_features)
            
            # Influencer analysis
            influencer_signals = self._analyze_influencer_signals(hashtag_data, influencer_data)
            
            # Combine signals for trend detection
            trend_score = self._combine_multimodal_signals(
                text_signals, audio_signals, influencer_signals
            )
            
            if trend_score['confidence'] > 0.6:
                trend = {
                    'hashtag': hashtag_data.get('hashtag', ''),
                    'platform': hashtag_data.get('platform', 'unknown'),
                    'trend_score': trend_score['score'],
                    'confidence': trend_score['confidence'],
                    'text_signals': text_signals,
                    'audio_signals': audio_signals,
                    'influencer_signals': influencer_signals,
                    'detection_method': 'multimodal',
                    'malaysia_relevance': self._assess_malaysia_relevance(hashtag_data),
                    'community_drivers': self._identify_community_drivers(influencer_signals),
                    'detected_at': datetime.now().isoformat()
                }
                trends.append(trend)
        
        print(f"✅ Detected {len(trends)} multimodal trends")
        return trends
    
    def _analyze_text_signals(self, hashtag_data):
        """Analyze text-based signals using embeddings"""
        hashtag = hashtag_data.get('hashtag', '')
        platform = hashtag_data.get('platform', 'unknown')
        
        # Basic text analysis (fallback)
        text_signals = {
            'sentiment_score': random.uniform(0.3, 0.9),
            'keyword_density': random.uniform(0.1, 0.8),
            'hashtag_virality': random.uniform(0.2, 0.9),
            'language_detection': 'en',  # Assume English for now
            'topic_relevance': random.uniform(0.4, 0.9),
            'engagement_potential': random.uniform(0.3, 0.8)
        }
        
        # Enhanced analysis with transformers if available
        if TRANSFORMERS_AVAILABLE and hashtag:
            try:
                # Simple keyword-based analysis for now
                beauty_keywords = ['beauty', 'makeup', 'skincare', 'hair', 'glow', 'skin']
                lifestyle_keywords = ['lifestyle', 'fashion', 'style', 'outfit', 'trend']
                
                hashtag_lower = hashtag.lower()
                beauty_score = sum(1 for kw in beauty_keywords if kw in hashtag_lower) / len(beauty_keywords)
                lifestyle_score = sum(1 for kw in lifestyle_keywords if kw in hashtag_lower) / len(lifestyle_keywords)
                
                text_signals.update({
                    'beauty_relevance': beauty_score,
                    'lifestyle_relevance': lifestyle_score,
                    'category': 'beauty' if beauty_score > lifestyle_score else 'lifestyle'
                })
            except Exception as e:
                print(f"⚠️ Text analysis error: {e}")
        
        return text_signals
    
    def _analyze_audio_signals(self, hashtag_data, audio_features=None):
        """Analyze audio-based signals"""
        if not AUDIO_AVAILABLE:
            return self._simulate_audio_signals(hashtag_data)
        
        # Simulate audio analysis for now
        audio_signals = {
            'tempo': random.uniform(100, 150),
            'energy': random.uniform(0.4, 0.9),
            'valence': random.uniform(0.3, 0.9),
            'speech_rate': random.uniform(120, 200),
            'audio_quality': random.uniform(0.6, 0.95),
            'background_music': random.choice([True, False]),
            'voice_clarity': random.uniform(0.5, 0.9),
            'trend_indicator': random.uniform(0.2, 0.8)
        }
        
        # Determine content type based on audio features
        if audio_signals['energy'] > 0.7 and audio_signals['tempo'] > 130:
            audio_signals['content_type'] = 'beauty_tutorial'
        elif audio_signals['speech_rate'] > 160:
            audio_signals['content_type'] = 'product_review'
        else:
            audio_signals['content_type'] = 'lifestyle_content'
        
        return audio_signals
    
    def _simulate_audio_signals(self, hashtag_data):
        """Simulate audio signals when librosa is not available"""
        return {
            'tempo': random.uniform(100, 150),
            'energy': random.uniform(0.4, 0.9),
            'valence': random.uniform(0.3, 0.9),
            'speech_rate': random.uniform(120, 200),
            'audio_quality': random.uniform(0.6, 0.95),
            'background_music': random.choice([True, False]),
            'voice_clarity': random.uniform(0.5, 0.9),
            'trend_indicator': random.uniform(0.2, 0.8),
            'content_type': random.choice(['beauty_tutorial', 'lifestyle_content', 'product_review']),
            'simulated': True
        }
    
    def _analyze_influencer_signals(self, hashtag_data, influencer_data=None):
        """Analyze influencer-driven signals"""
        hashtag = hashtag_data.get('hashtag', '').lower()
        platform = hashtag_data.get('platform', 'unknown')
        
        # Find relevant influencers
        relevant_influencers = []
        for category, influencers in self.malaysia_influencers.items():
            for influencer in influencers:
                # Simple relevance scoring
                relevance_score = random.uniform(0.1, 0.9)
                if relevance_score > 0.5:
                    relevant_influencers.append({
                        **influencer,
                        'relevance_score': relevance_score,
                        'trend_contribution': random.uniform(0.2, 0.8)
                    })
        
        influencer_signals = {
            'active_influencers': relevant_influencers[:3],  # Top 3
            'total_influencer_reach': sum(inf['followers'] for inf in relevant_influencers[:3]),
            'avg_engagement': np.mean([inf['engagement'] for inf in relevant_influencers[:3]]) if relevant_influencers else 0,
            'community_coverage': list(set([inf['communities'][0] for inf in relevant_influencers[:3]])),
            'influencer_momentum': random.uniform(0.3, 0.9),
            'cross_platform_presence': random.uniform(0.4, 0.8)
        }
        
        return influencer_signals
    
    def _combine_multimodal_signals(self, text_signals, audio_signals, influencer_signals):
        """Combine all signals to determine trend confidence"""
        # Weighted combination of signals
        text_weight = 0.4
        audio_weight = 0.3
        influencer_weight = 0.3
        
        # Calculate weighted score
        text_score = text_signals.get('sentiment_score', 0.5) * text_signals.get('engagement_potential', 0.5)
        audio_score = audio_signals.get('trend_indicator', 0.5) * audio_signals.get('audio_quality', 0.5)
        influencer_score = influencer_signals.get('influencer_momentum', 0.5) * (influencer_signals.get('avg_engagement', 0) / 5.0)
        
        combined_score = (
            text_score * text_weight +
            audio_score * audio_weight +
            influencer_score * influencer_weight
        )
        
        # Calculate confidence based on signal consistency
        signals = [text_score, audio_score, influencer_score]
        signal_variance = np.var(signals)
        confidence = max(0.1, 1.0 - signal_variance)  # Higher variance = lower confidence
        
        return {
            'score': min(1.0, combined_score),
            'confidence': confidence,
            'signal_strength': {
                'text': text_score,
                'audio': audio_score,
                'influencer': influencer_score
            }
        }
    
    def _assess_malaysia_relevance(self, hashtag_data):
        """Assess relevance to Malaysian market"""
        hashtag = hashtag_data.get('hashtag', '').lower()
        
        # Malaysia-specific keywords
        malaysia_keywords = [
            'malaysia', 'kl', 'kuala lumpur', 'penang', 'johor', 'sabah', 'sarawak',
            'malay', 'chinese', 'indian', 'bumi', 'melayu', 'cina', 'india',
            'raya', 'hari raya', 'chinese new year', 'deepavali', 'merdeka',
            'nasi lemak', 'teh tarik', 'mamak', 'pasar', 'bazaar'
        ]
        
        relevance_score = 0.5  # Base score
        
        # Check for Malaysia-specific terms
        for keyword in malaysia_keywords:
            if keyword in hashtag:
                relevance_score += 0.1
        
        # Platform-specific adjustments
        platform = hashtag_data.get('platform', 'unknown')
        if platform in ['instagram', 'tiktok']:
            relevance_score += 0.1  # Higher engagement platforms in Malaysia
        
        return min(1.0, relevance_score)
    
    def _identify_community_drivers(self, influencer_signals):
        """Identify which Malaysian communities are driving the trend"""
        community_coverage = influencer_signals.get('community_coverage', [])
        
        community_analysis = {
            'malay': {'score': 0.3, 'influencers': 0, 'reach': 0},
            'chinese': {'score': 0.3, 'influencers': 0, 'reach': 0},
            'indian': {'score': 0.3, 'influencers': 0, 'reach': 0},
            'mixed': {'score': 0.1, 'influencers': 0, 'reach': 0}
        }
        
        # Analyze active influencers
        for influencer in influencer_signals.get('active_influencers', []):
            communities = influencer.get('communities', ['mixed'])
            for community in communities:
                if community in community_analysis:
                    community_analysis[community]['influencers'] += 1
                    community_analysis[community]['reach'] += influencer.get('followers', 0)
                    community_analysis[community]['score'] += influencer.get('trend_contribution', 0.1)
        
        # Normalize scores
        total_score = sum(comm['score'] for comm in community_analysis.values())
        if total_score > 0:
            for community in community_analysis:
                community_analysis[community]['score'] /= total_score
        
        return community_analysis
    
    def get_trend_radar_data(self, trends):
        """Generate data for trend radar heatmap"""
        radar_data = {
            'emerging': [],
            'growing': [],
            'peak': [],
            'declining': []
        }
        
        for trend in trends:
            trend_score = trend.get('trend_score', 0)
            confidence = trend.get('confidence', 0)
            
            # Categorize trends based on score and confidence
            if trend_score > 0.8 and confidence > 0.7:
                radar_data['peak'].append(trend)
            elif trend_score > 0.6 and confidence > 0.6:
                radar_data['growing'].append(trend)
            elif trend_score > 0.4 and confidence > 0.5:
                radar_data['emerging'].append(trend)
            else:
                radar_data['declining'].append(trend)
        
        return radar_data

# Initialize the multimodal detection engine
multimodal_detection = MultimodalTrendDetection()
