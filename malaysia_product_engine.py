#!/usr/bin/env python3
"""
Malaysia Product Mapping Engine for TrendSpotter
L'Oréal Malaysia product mapping and localization
"""
import random
from datetime import datetime

class MalaysiaProductEngine:
    """Malaysia-specific product mapping and recommendations"""
    
    def __init__(self):
        print("🇲🇾 Malaysia Product Engine initialized")
        
        # L'Oréal Malaysia product portfolio
        self.loreal_products = {
            'skincare': {
                'revitalift': {
                    'name': 'Revitalift Crystal Micro-Essence',
                    'category': 'Anti-aging',
                    'price_range': 'RM 89-129',
                    'key_ingredients': ['Salicylic Acid', 'Micro-crystals'],
                    'skin_concerns': ['Fine lines', 'Dullness', 'Uneven texture'],
                    'suitable_for': ['Normal', 'Combination', 'Oily'],
                    'humidity_friendly': True,
                    'local_availability': 'High'
                },
                'white_perfect': {
                    'name': 'White Perfect Clinical Day Cream',
                    'category': 'Brightening',
                    'price_range': 'RM 45-65',
                    'key_ingredients': ['Melanin-Block', 'Pro-Vitamin B3'],
                    'skin_concerns': ['Dark spots', 'Uneven tone', 'UV protection'],
                    'suitable_for': ['All skin types'],
                    'humidity_friendly': True,
                    'local_availability': 'High'
                },
                'hydrafresh': {
                    'name': 'Hydrafresh Aqua Essence',
                    'category': 'Hydrating',
                    'price_range': 'RM 25-39',
                    'key_ingredients': ['Hydra-Nutri Matrix', 'Aqua Essence'],
                    'skin_concerns': ['Dehydration', 'AC dryness', 'Tightness'],
                    'suitable_for': ['Dry', 'Normal', 'Sensitive'],
                    'humidity_friendly': True,
                    'local_availability': 'Very High'
                }
            },
            'makeup': {
                'true_match': {
                    'name': 'True Match Foundation',
                    'category': 'Foundation',
                    'price_range': 'RM 49-69',
                    'shade_range': '24 shades (Asian-inclusive)',
                    'skin_concerns': ['Color matching', 'Natural finish'],
                    'suitable_for': ['All skin types'],
                    'humidity_friendly': True,
                    'local_availability': 'Very High'
                },
                'infallible': {
                    'name': 'Infallible 24HR Fresh Wear',
                    'category': 'Long-wear foundation',
                    'price_range': 'RM 65-89',
                    'key_features': ['24HR wear', 'Transfer-resistant', 'Natural matte'],
                    'skin_concerns': ['Oiliness', 'Humidity', 'Longevity'],
                    'suitable_for': ['Oily', 'Combination'],
                    'humidity_friendly': True,
                    'local_availability': 'High'
                },
                'color_riche': {
                    'name': 'Color Riche Matte Lipstick',
                    'category': 'Lipstick',
                    'price_range': 'RM 39-55',
                    'key_features': ['Matte finish', 'Rich pigment', 'Comfortable'],
                    'suitable_for': ['All skin tones'],
                    'humidity_friendly': True,
                    'local_availability': 'Very High'
                }
            },
            'hair': {
                'elvive': {
                    'name': 'Elvive Extraordinary Oil',
                    'category': 'Hair treatment',
                    'price_range': 'RM 15-25',
                    'key_ingredients': ['6 precious oils'],
                    'hair_concerns': ['Dryness', 'Damage', 'Frizz'],
                    'suitable_for': ['All hair types'],
                    'humidity_friendly': True,
                    'local_availability': 'Very High'
                }
            }
        }
        
        # Malaysia seasonal/cultural calendar
        self.malaysia_calendar = {
            'chinese_new_year': {
                'period': 'January/February',
                'beauty_focus': ['Red lips', 'Golden eye looks', 'Radiant skin'],
                'product_opportunities': ['Limited edition reds', 'Gold packaging', 'Gift sets']
            },
            'hari_raya': {
                'period': 'May/June (varies)',
                'beauty_focus': ['Traditional colors', 'Long-wear makeup', 'Elegant looks'],
                'product_opportunities': ['Modest coverage', 'Raya collections', 'Family-friendly sets']
            },
            'deepavali': {
                'period': 'October/November',
                'beauty_focus': ['Rich colors', 'Golden highlights', 'Festival glamour'],
                'product_opportunities': ['Vibrant eyeshadows', 'Statement lips', 'Glow products']
            },
            'monsoon_season': {
                'period': 'November - February',
                'beauty_focus': ['Waterproof makeup', 'Extra hydration', 'Long-wear'],
                'product_opportunities': ['Weather-proof formulas', 'Hydrating treatments', 'Setting products']
            },
            'hot_season': {
                'period': 'March - September',
                'beauty_focus': ['Oil control', 'Sun protection', 'Lightweight formulas'],
                'product_opportunities': ['Mattifying products', 'SPF makeup', 'Cooling treatments']
            }
        }
    
    def map_trend_to_products(self, trend_data):
        """Map a beauty trend to relevant L'Oréal Malaysia products"""
        
        trend_name = trend_data.get('name', '').lower()
        trend_category = trend_data.get('category', '').lower()
        
        # Analyze trend characteristics
        mapping = {
            'trend_id': trend_data.get('id'),
            'trend_name': trend_data.get('name'),
            'trend_category': trend_category,
            'recommended_products': [],
            'opportunity_score': random.randint(70, 95),
            'local_relevance': self._assess_local_relevance(trend_data),
            'climate_compatibility': self._assess_climate_compatibility(trend_data),
            'cultural_fit': self._assess_cultural_fit(trend_data),
            'launch_strategy': self._suggest_launch_strategy(trend_data)
        }
        
        # Find matching products
        for category, products in self.loreal_products.items():
            if self._category_matches_trend(category, trend_category, trend_name):
                for product_id, product_info in products.items():
                    if self._product_matches_trend(product_info, trend_data):
                        product_match = {
                            'product_id': product_id,
                            'product_name': product_info['name'],
                            'category': category,
                            'match_score': random.randint(75, 95),
                            'price_range': product_info['price_range'],
                            'availability': product_info['local_availability'],
                            'humidity_suitable': product_info['humidity_friendly'],
                            'trend_application': self._get_trend_application(product_info, trend_data),
                            'marketing_angle': self._get_marketing_angle(product_info, trend_data)
                        }
                        mapping['recommended_products'].append(product_match)
        
        # Sort products by match score
        mapping['recommended_products'].sort(key=lambda x: x['match_score'], reverse=True)
        
        # Add seasonal considerations
        mapping['seasonal_insights'] = self._get_seasonal_insights(trend_data)
        
        return mapping
    
    def get_seasonal_opportunities(self):
        """Get seasonal product opportunities for Malaysia"""
        
        current_month = datetime.now().month
        
        # Determine current season/period
        seasonal_opportunities = {}
        
        for event, details in self.malaysia_calendar.items():
            opportunity = {
                'event_name': event.replace('_', ' ').title(),
                'period': details['period'],
                'beauty_focus': details['beauty_focus'],
                'product_opportunities': details['product_opportunities'],
                'relevance_score': self._calculate_seasonal_relevance(event, current_month),
                'recommended_actions': self._get_seasonal_actions(event, details),
                'target_communities': self._get_target_communities(event),
                'budget_considerations': self._get_budget_considerations(event)
            }
            seasonal_opportunities[event] = opportunity
        
        return seasonal_opportunities
    
    def analyze_community_preferences(self, community_type):
        """Analyze beauty preferences for Malaysian communities"""
        
        community_preferences = {
            'malay': {
                'color_preferences': ['Natural tones', 'Warm browns', 'Modest brights'],
                'coverage_preference': 'Medium to full coverage',
                'key_concerns': ['Humidity resistance', 'Halal certification', 'Longevity'],
                'popular_trends': ['Natural glam', 'Hijab-friendly makeup', 'Wedding looks'],
                'price_sensitivity': 'Medium',
                'shopping_behavior': 'Research-driven, community influenced',
                'product_priorities': ['Quality', 'Religious compliance', 'Value for money']
            },
            'chinese': {
                'color_preferences': ['Classic reds', 'Golden tones', 'Subtle brights'],
                'coverage_preference': 'Light to medium coverage',
                'key_concerns': ['Skin brightening', 'Anti-aging', 'Natural finish'],
                'popular_trends': ['K-beauty inspired', 'Glass skin', 'Minimal makeup'],
                'price_sensitivity': 'Low to medium',
                'shopping_behavior': 'Brand conscious, quality focused',
                'product_priorities': ['Innovation', 'Brand reputation', 'Results']
            },
            'indian': {
                'color_preferences': ['Rich jewel tones', 'Gold accents', 'Vibrant colors'],
                'coverage_preference': 'Medium to full coverage',
                'key_concerns': ['Color matching', 'Festival looks', 'Skin tone enhancement'],
                'popular_trends': ['Bold eyes', 'Traditional with modern twist', 'Bridal makeup'],
                'price_sensitivity': 'Medium to high',
                'shopping_behavior': 'Occasion-driven, family influenced',
                'product_priorities': ['Color payoff', 'Versatility', 'Cultural relevance']
            },
            'mixed': {
                'color_preferences': ['Versatile neutrals', 'Adaptable tones', 'Universal shades'],
                'coverage_preference': 'Buildable coverage',
                'key_concerns': ['Versatility', 'Multi-cultural events', 'Adaptability'],
                'popular_trends': ['Fusion looks', 'Adaptable styles', 'Cultural celebrations'],
                'price_sensitivity': 'Medium',
                'shopping_behavior': 'Trend-aware, inclusive focused',
                'product_priorities': ['Versatility', 'Inclusivity', 'Multi-use products']
            }
        }
        
        return community_preferences.get(community_type.lower(), community_preferences['mixed'])
    
    def _assess_local_relevance(self, trend_data):
        """Assess how relevant a trend is to Malaysian market"""
        
        # Factors that increase relevance
        relevance_score = 50  # Base score
        
        trend_name = trend_data.get('name', '').lower()
        category = trend_data.get('category', '').lower()
        
        # Climate-related trends get boost
        if any(word in trend_name for word in ['humid', 'tropical', 'hot', 'sweat', 'oil']):
            relevance_score += 20
        
        # Natural/modest trends get boost
        if any(word in trend_name for word in ['natural', 'modest', 'minimal', 'clean']):
            relevance_score += 15
        
        # Skincare gets boost (popular in Malaysia)
        if category == 'skincare':
            relevance_score += 10
        
        return min(100, relevance_score)
    
    def _assess_climate_compatibility(self, trend_data):
        """Assess how well trend works in Malaysian climate"""
        
        trend_name = trend_data.get('name', '').lower()
        
        # High humidity, heat considerations
        if any(word in trend_name for word in ['waterproof', 'longwear', 'setting', 'matte']):
            return 'Excellent'
        elif any(word in trend_name for word in ['dewy', 'glossy', 'hydrating']):
            return 'Good with setting'
        elif any(word in trend_name for word in ['powder', 'heavy', 'layered']):
            return 'Challenging'
        else:
            return 'Adaptable'
    
    def _assess_cultural_fit(self, trend_data):
        """Assess cultural fit for Malaysian communities"""
        
        trend_name = trend_data.get('name', '').lower()
        
        # Conservative-friendly trends
        if any(word in trend_name for word in ['natural', 'modest', 'subtle', 'professional']):
            return 'High - suitable for all communities'
        elif any(word in trend_name for word in ['bold', 'dramatic', 'experimental']):
            return 'Medium - occasion-dependent'
        else:
            return 'Adaptable to community preferences'
    
    def _suggest_launch_strategy(self, trend_data):
        """Suggest launch strategy for Malaysian market"""
        
        trend_score = trend_data.get('trend_score', 0)
        lifecycle = trend_data.get('lifecycle', 'Unknown')
        
        if trend_score > 80 and lifecycle == 'Emerging':
            return 'Fast track - capitalize on early trend'
        elif trend_score > 70:
            return 'Standard launch - test in key cities first'
        elif trend_score > 60:
            return 'Careful approach - monitor and adapt'
        else:
            return 'Wait and see - low priority'
    
    def _category_matches_trend(self, product_category, trend_category, trend_name):
        """Check if product category matches trend"""
        
        category_mapping = {
            'skincare': ['skincare', 'skin', 'glow', 'hydrat', 'bright'],
            'makeup': ['makeup', 'foundation', 'lip', 'eye', 'contour'],
            'hair': ['hair', 'scalp']
        }
        
        keywords = category_mapping.get(product_category, [])
        
        return (product_category == trend_category or 
                any(keyword in trend_name for keyword in keywords))
    
    def _product_matches_trend(self, product_info, trend_data):
        """Check if specific product matches trend"""
        
        # Basic matching logic
        return random.choice([True, False])  # Simplified for demo
    
    def _get_trend_application(self, product_info, trend_data):
        """Get how to use product for the trend"""
        
        return f"Use {product_info['name']} to achieve {trend_data.get('name', 'the trend')} look"
    
    def _get_marketing_angle(self, product_info, trend_data):
        """Get marketing angle for product-trend combination"""
        
        angles = [
            f"Perfect for Malaysian climate",
            f"Humidity-tested formula",
            f"Suitable for all Malaysian skin tones",
            f"Long-lasting in tropical weather",
            f"Ideal for {trend_data.get('platform', 'social media')} content"
        ]
        
        return random.choice(angles)
    
    def _get_seasonal_insights(self, trend_data):
        """Get seasonal insights for trend"""
        
        current_month = datetime.now().month
        
        if current_month in [12, 1, 2]:
            return "Perfect for monsoon season - focus on waterproof formulas"
        elif current_month in [3, 4, 5]:
            return "Spring transition - great for fresh, natural looks"
        elif current_month in [6, 7, 8]:
            return "Hot season - emphasize oil control and longevity"
        else:
            return "Festival season - highlight versatility for celebrations"
    
    def _calculate_seasonal_relevance(self, event, current_month):
        """Calculate relevance of seasonal event"""
        
        event_months = {
            'chinese_new_year': [1, 2],
            'hari_raya': [5, 6],
            'deepavali': [10, 11],
            'monsoon_season': [11, 12, 1, 2],
            'hot_season': [3, 4, 5, 6, 7, 8, 9]
        }
        
        months = event_months.get(event, [current_month])
        
        if current_month in months:
            return random.randint(85, 95)
        elif abs(min(months) - current_month) <= 2:
            return random.randint(70, 85)
        else:
            return random.randint(40, 70)
    
    def _get_seasonal_actions(self, event, details):
        """Get recommended actions for seasonal opportunity"""
        
        actions = [
            f"Launch {event.replace('_', ' ')} themed collection",
            f"Partner with local influencers for {event.replace('_', ' ')} content",
            f"Create tutorials for {event.replace('_', ' ')} looks",
            f"Offer special promotions during {details['period']}",
            f"Develop culturally relevant marketing campaigns"
        ]
        
        return random.sample(actions, 3)
    
    def _get_target_communities(self, event):
        """Get target communities for seasonal event"""
        
        community_mapping = {
            'chinese_new_year': ['Chinese Malaysian', 'General population'],
            'hari_raya': ['Malay Malaysian', 'Muslim community'],
            'deepavali': ['Indian Malaysian', 'Hindu community'],
            'monsoon_season': ['All communities'],
            'hot_season': ['All communities']
        }
        
        return community_mapping.get(event, ['All communities'])
    
    def _get_budget_considerations(self, event):
        """Get budget considerations for seasonal event"""
        
        considerations = {
            'chinese_new_year': 'Higher budget for premium gifts and limited editions',
            'hari_raya': 'Family-focused pricing and value sets',
            'deepavali': 'Festival special pricing and vibrant collections',
            'monsoon_season': 'Practical pricing for everyday essentials',
            'hot_season': 'Affordable options for frequent repurchase'
        }
        
        return considerations.get(event, 'Standard pricing strategy')

# Initialize the Malaysia product engine
malaysia_product_engine = MalaysiaProductEngine()
