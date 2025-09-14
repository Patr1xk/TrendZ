#!/usr/bin/env python3
"""
Malaysia Product Mapping Engine for TrendZ
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
                    'local_availability': 'High',
                    'image_url': '/static/images/revitalift.jpg',
                    'description': 'Advanced anti-aging essence with micro-crystals for radiant skin'
                },
                'white_perfect': {
                    'name': 'White Perfect Clinical Day Cream',
                    'category': 'Brightening',
                    'price_range': 'RM 45-65',
                    'key_ingredients': ['Melanin-Block', 'Pro-Vitamin B3'],
                    'skin_concerns': ['Dark spots', 'Uneven tone', 'UV protection'],
                    'suitable_for': ['All skin types'],
                    'humidity_friendly': True,
                    'local_availability': 'High',
                    'image_url': '/static/images/white_perfect.jpg',
                    'description': 'Clinical-grade brightening cream for even skin tone'
                },
                'hydrafresh': {
                    'name': 'Hydrafresh Aqua Essence',
                    'category': 'Hydrating',
                    'price_range': 'RM 25-39',
                    'key_ingredients': ['Hydra-Nutri Matrix', 'Aqua Essence'],
                    'skin_concerns': ['Dehydration', 'AC dryness', 'Tightness'],
                    'suitable_for': ['Dry', 'Normal', 'Sensitive'],
                    'humidity_friendly': True,
                    'local_availability': 'Very High',
                    'image_url': '/static/images/hydrafresh.jpg',
                    'description': 'Intensive hydration essence for tropical climate'
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
                    'local_availability': 'Very High',
                    'image_url': '/static/images/true_match.jpg',
                    'description': 'Perfect color match foundation for Asian skin tones'
                },
                'infallible': {
                    'name': 'Infallible 24HR Fresh Wear',
                    'category': 'Long-wear foundation',
                    'price_range': 'RM 65-89',
                    'key_features': ['24HR wear', 'Transfer-resistant', 'Natural matte'],
                    'skin_concerns': ['Oiliness', 'Humidity', 'Longevity'],
                    'suitable_for': ['Oily', 'Combination'],
                    'humidity_friendly': True,
                    'local_availability': 'High',
                    'image_url': '/static/images/infallible.jpg',
                    'description': '24-hour fresh wear foundation for tropical climate'
                },
                'color_riche': {
                    'name': 'Color Riche Matte Lipstick',
                    'category': 'Lipstick',
                    'price_range': 'RM 39-55',
                    'key_features': ['Matte finish', 'Rich pigment', 'Comfortable'],
                    'suitable_for': ['All skin tones'],
                    'humidity_friendly': True,
                    'local_availability': 'Very High',
                    'image_url': '/static/images/color_riche.jpg',
                    'description': 'Rich matte lipstick with comfortable long-wear formula'
                },
                'lash_paradise': {
                    'name': 'Lash Paradise Mascara',
                    'category': 'Mascara',
                    'price_range': 'RM 35-49',
                    'key_features': ['Volume', 'Length', 'No clumping'],
                    'suitable_for': ['All eye types'],
                    'humidity_friendly': True,
                    'local_availability': 'Very High',
                    'image_url': '/static/images/lash_paradise.jpg',
                    'description': 'Paradise-worthy lashes with volume and length'
                },
                'infallible_eyeshadow': {
                    'name': 'Infallible 24HR Eyeshadow',
                    'category': 'Eyeshadow',
                    'price_range': 'RM 25-35',
                    'key_features': ['24HR wear', 'Cream-powder formula', 'No creasing'],
                    'suitable_for': ['All eye types'],
                    'humidity_friendly': True,
                    'local_availability': 'High',
                    'image_url': '/static/images/infallible_eyeshadow.jpg',
                    'description': 'Long-wear eyeshadow that stays put in humidity'
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
                    'local_availability': 'Very High',
                    'image_url': '/static/images/elvive_oil.jpg',
                    'description': 'Extraordinary hair oil with 6 precious oils'
                }
            }
        }
        
        # Hashtag-to-Product Mapping Database
        self.hashtag_product_mapping = {
            # Barbie-themed trends
            'barbiemakeup': {
                'primary_products': ['color_riche', 'lash_paradise', 'infallible_eyeshadow'],
                'trend_description': 'Pink, glamorous, and playful makeup looks inspired by Barbie',
                'color_palette': ['Hot Pink', 'Bubblegum Pink', 'Rose Gold', 'Bright Coral'],
                'look_style': 'Glamorous, playful, and feminine',
                'target_audience': 'Gen Z, Millennials, Beauty enthusiasts',
                'application_tips': [
                    'Use bright pink lipstick for statement lips',
                    'Apply rose gold eyeshadow for glamorous eyes',
                    'Finish with volumizing mascara for doll-like lashes',
                    'Add subtle pink blush for healthy glow'
                ],
                'marketing_angles': [
                    'Perfect for Barbie movie premiere',
                    'Instagram-worthy pink aesthetic',
                    'Fun and playful summer look',
                    'Celebrity-inspired glamour'
                ]
            },
            'barbiecore': {
                'primary_products': ['color_riche', 'lash_paradise', 'infallible'],
                'trend_description': 'Ultra-feminine pink aesthetic with bold, playful elements',
                'color_palette': ['Barbie Pink', 'Hot Pink', 'Rose Gold', 'Coral'],
                'look_style': 'Bold, feminine, and Instagram-ready',
                'target_audience': 'Social media influencers, Gen Z, Fashion-forward',
                'application_tips': [
                    'Bold pink lips are essential',
                    'Glowing skin with pink undertones',
                    'Dramatic lashes for doll effect',
                    'Pink accessories to complete the look'
                ],
                'marketing_angles': [
                    'Movie tie-in opportunity',
                    'Social media viral potential',
                    'Celebrity endorsement ready',
                    'Limited edition packaging opportunity'
                ]
            },
            'barbiepink': {
                'primary_products': ['color_riche', 'infallible_eyeshadow'],
                'trend_description': 'Signature Barbie pink color in makeup and fashion',
                'color_palette': ['Signature Barbie Pink', 'Hot Pink', 'Bubblegum'],
                'look_style': 'Classic, iconic, and instantly recognizable',
                'target_audience': 'All ages, Barbie fans, Pink lovers',
                'application_tips': [
                    'Signature pink lipstick is key',
                    'Pink eyeshadow for monochromatic look',
                    'Keep skin glowing and fresh',
                    'Minimal but impactful application'
                ],
                'marketing_angles': [
                    'Iconic color recognition',
                    'Cross-generational appeal',
                    'Nostalgia factor',
                    'Brand partnership opportunity'
                ]
            },
            
            # Natural beauty trends
            'naturalmakeup': {
                'primary_products': ['true_match', 'hydrafresh', 'white_perfect'],
                'trend_description': 'Clean, minimal makeup that enhances natural beauty',
                'color_palette': ['Nude', 'Beige', 'Soft Brown', 'Natural Pink'],
                'look_style': 'Fresh, clean, and effortless',
                'target_audience': 'Working professionals, Minimalists, Natural beauty lovers',
                'application_tips': [
                    'Light foundation for even skin tone',
                    'Subtle lip color for natural look',
                    'Minimal eye makeup',
                    'Focus on skincare for glow'
                ],
                'marketing_angles': [
                    'Perfect for Malaysian climate',
                    'Work-appropriate styling',
                    'Skincare-first approach',
                    'Long-lasting in humidity'
                ]
            },
            'cleangirl': {
                'primary_products': ['hydrafresh', 'white_perfect', 'true_match'],
                'trend_description': 'Skincare-focused approach with minimal makeup',
                'color_palette': ['Nude', 'Clear', 'Soft Pink', 'Natural'],
                'look_style': 'Fresh, healthy, and glowing',
                'target_audience': 'Skincare enthusiasts, Health-conscious, Young adults',
                'application_tips': [
                    'Prioritize skincare routine',
                    'Use lightweight foundation',
                    'Natural lip balm or gloss',
                    'Focus on skin health'
                ],
                'marketing_angles': [
                    'Skincare-makeup hybrid',
                    'Healthy lifestyle alignment',
                    'Malaysian humidity-friendly',
                    'Sustainable beauty approach'
                ]
            },
            
            # Glamour trends
            'glammakeup': {
                'primary_products': ['infallible', 'lash_paradise', 'infallible_eyeshadow', 'color_riche'],
                'trend_description': 'Full glamour makeup for special occasions',
                'color_palette': ['Gold', 'Bronze', 'Deep Red', 'Black'],
                'look_style': 'Dramatic, sophisticated, and elegant',
                'target_audience': 'Special occasions, Events, Glamour lovers',
                'application_tips': [
                    'Full coverage foundation',
                    'Dramatic eye makeup',
                    'Bold lip color',
                    'Contouring and highlighting'
                ],
                'marketing_angles': [
                    'Special occasion ready',
                    'Malaysian wedding season',
                    'Festival celebrations',
                    'Professional makeup artist approved'
                ]
            },
            'partyready': {
                'primary_products': ['infallible', 'lash_paradise', 'color_riche'],
                'trend_description': 'Long-wear makeup perfect for parties and events',
                'color_palette': ['Bold', 'Vibrant', 'Metallic', 'Shimmer'],
                'look_style': 'Fun, vibrant, and party-appropriate',
                'target_audience': 'Party-goers, Event attendees, Social butterflies',
                'application_tips': [
                    'Long-wear foundation essential',
                    'Waterproof mascara for dancing',
                    'Bold lip color that lasts',
                    'Setting spray for all-night wear'
                ],
                'marketing_angles': [
                    'All-night wear guarantee',
                    'Malaysian party scene',
                    'Social media ready',
                    'Celebration season perfect'
                ]
            },
            
            # Skincare trends
            'glassskin': {
                'primary_products': ['hydrafresh', 'white_perfect', 'revitalift'],
                'trend_description': 'Korean-inspired dewy, translucent skin',
                'color_palette': ['Clear', 'Dewy', 'Translucent', 'Glowing'],
                'look_style': 'Radiant, dewy, and luminous',
                'target_audience': 'K-beauty fans, Skincare enthusiasts, Young adults',
                'application_tips': [
                    'Intensive hydration routine',
                    'Brightening treatments',
                    'Minimal makeup to show skin',
                    'Dewy finish products'
                ],
                'marketing_angles': [
                    'K-beauty trend alignment',
                    'Malaysian humidity benefits',
                    'Social media viral potential',
                    'Skincare-makeup integration'
                ]
            },
            'skincare': {
                'primary_products': ['hydrafresh', 'white_perfect', 'revitalift'],
                'trend_description': 'Focus on healthy, well-cared-for skin',
                'color_palette': ['Natural', 'Healthy', 'Glowing'],
                'look_style': 'Healthy, natural, and well-maintained',
                'target_audience': 'Skincare conscious, Health-focused, All ages',
                'application_tips': [
                    'Consistent skincare routine',
                    'Sun protection daily',
                    'Hydration is key',
                    'Gentle cleansing'
                ],
                'marketing_angles': [
                    'Health and wellness alignment',
                    'Malaysian climate adaptation',
                    'Preventive skincare approach',
                    'Long-term skin health'
                ]
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
    
    def get_hashtag_product_recommendations(self, hashtag):
        """Get specific product recommendations for a trending hashtag"""
        
        hashtag_clean = hashtag.lower().replace('#', '').replace(' ', '')
        
        # Check if we have specific mapping for this hashtag
        if hashtag_clean in self.hashtag_product_mapping:
            mapping_data = self.hashtag_product_mapping[hashtag_clean]
            
            # Get detailed product information
            recommended_products = []
            for product_id in mapping_data['primary_products']:
                product_info = self._find_product_by_id(product_id)
                if product_info:
                    product_detail = {
                        'product_id': product_id,
                        'product_name': product_info['name'],
                        'category': product_info.get('category', 'Unknown'),
                        'price_range': product_info['price_range'],
                        'description': product_info['description'],
                        'image_url': product_info.get('image_url', '/static/images/default.jpg'),
                        'availability': product_info['local_availability'],
                        'humidity_suitable': product_info['humidity_friendly'],
                        'match_reason': self._get_hashtag_match_reason(product_id, hashtag_clean),
                        'application_tip': self._get_product_application_tip(product_id, hashtag_clean)
                    }
                    recommended_products.append(product_detail)
            
            return {
                'hashtag': hashtag,
                'trend_description': mapping_data['trend_description'],
                'color_palette': mapping_data['color_palette'],
                'look_style': mapping_data['look_style'],
                'target_audience': mapping_data['target_audience'],
                'recommended_products': recommended_products,
                'application_tips': mapping_data['application_tips'],
                'marketing_angles': mapping_data['marketing_angles'],
                'total_products': len(recommended_products),
                'estimated_cost': self._calculate_total_cost(recommended_products),
                'malaysia_relevance': self._assess_malaysia_relevance(hashtag_clean)
            }
        else:
            # Fallback to general trend mapping
            return self._get_general_hashtag_recommendations(hashtag)
    
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
    
    def _find_product_by_id(self, product_id):
        """Find product information by ID across all categories"""
        
        for category, products in self.loreal_products.items():
            if product_id in products:
                product_info = products[product_id].copy()
                product_info['category'] = category
                return product_info
        return None
    
    def _get_hashtag_match_reason(self, product_id, hashtag):
        """Get reason why product matches the hashtag"""
        
        match_reasons = {
            'color_riche': {
                'barbiemakeup': 'Perfect pink lipstick for Barbie-inspired looks',
                'barbiecore': 'Essential pink lipstick for Barbiecore aesthetic',
                'barbiepink': 'Signature pink color matches Barbie pink',
                'glammakeup': 'Rich pigment perfect for glamorous looks',
                'partyready': 'Long-wear formula ideal for parties'
            },
            'lash_paradise': {
                'barbiemakeup': 'Volumizing mascara creates doll-like lashes',
                'barbiecore': 'Dramatic lashes essential for Barbiecore look',
                'glammakeup': 'Volume and length for full glamour',
                'partyready': 'Long-lasting mascara for all-night wear'
            },
            'infallible_eyeshadow': {
                'barbiemakeup': 'Rose gold eyeshadow perfect for Barbie eyes',
                'barbiecore': 'Pink eyeshadow essential for Barbiecore',
                'glammakeup': 'Long-wear eyeshadow for dramatic looks',
                'partyready': '24HR wear perfect for parties'
            },
            'infallible': {
                'barbiecore': 'Long-wear foundation for all-day Barbie look',
                'glammakeup': 'Full coverage foundation for glamour',
                'partyready': '24HR wear foundation for parties'
            },
            'true_match': {
                'naturalmakeup': 'Natural finish foundation for clean look',
                'cleangirl': 'Lightweight foundation for skincare-focused look'
            },
            'hydrafresh': {
                'naturalmakeup': 'Hydrating essence for natural glow',
                'cleangirl': 'Skincare-first approach with hydration',
                'glassskin': 'Intensive hydration for dewy skin'
            },
            'white_perfect': {
                'naturalmakeup': 'Brightening cream for natural glow',
                'cleangirl': 'Skincare-focused brightening',
                'glassskin': 'Brightening treatment for glass skin'
            },
            'revitalift': {
                'glassskin': 'Anti-aging essence for radiant skin',
                'skincare': 'Advanced anti-aging for healthy skin'
            }
        }
        
        return match_reasons.get(product_id, {}).get(hashtag, 'Perfect match for this trend')
    
    def _get_product_application_tip(self, product_id, hashtag):
        """Get specific application tip for product-hashtag combination"""
        
        application_tips = {
            'color_riche': {
                'barbiemakeup': 'Apply bold pink lipstick and blot for long-wear',
                'barbiecore': 'Use as statement lip for Instagram-worthy look',
                'glammakeup': 'Layer for intense color payoff',
                'partyready': 'Apply and set with powder for all-night wear'
            },
            'lash_paradise': {
                'barbiemakeup': 'Apply multiple coats for doll-like volume',
                'barbiecore': 'Build up volume for dramatic effect',
                'glammakeup': 'Use for both upper and lower lashes',
                'partyready': 'Apply waterproof version for dancing'
            },
            'infallible_eyeshadow': {
                'barbiemakeup': 'Apply rose gold shade for Barbie eyes',
                'barbiecore': 'Use pink shades for monochromatic look',
                'glammakeup': 'Layer colors for dramatic effect',
                'partyready': 'Apply primer first for 24HR wear'
            },
            'infallible': {
                'barbiecore': 'Apply with sponge for flawless finish',
                'glammakeup': 'Use full coverage for special occasions',
                'partyready': 'Set with powder for humidity resistance'
            },
            'true_match': {
                'naturalmakeup': 'Apply lightly for natural finish',
                'cleangirl': 'Use fingers for skin-like application'
            },
            'hydrafresh': {
                'naturalmakeup': 'Apply before makeup for natural glow',
                'cleangirl': 'Use morning and night for hydration',
                'glassskin': 'Layer multiple times for dewy effect'
            },
            'white_perfect': {
                'naturalmakeup': 'Apply daily for even skin tone',
                'cleangirl': 'Use as part of skincare routine',
                'glassskin': 'Apply before makeup for brightening'
            },
            'revitalift': {
                'glassskin': 'Apply before moisturizer for anti-aging',
                'skincare': 'Use consistently for best results'
            }
        }
        
        return application_tips.get(product_id, {}).get(hashtag, 'Apply as directed for best results')
    
    def _calculate_total_cost(self, products):
        """Calculate estimated total cost for product recommendations"""
        
        total_min = 0
        total_max = 0
        
        for product in products:
            price_range = product['price_range']
            # Extract numbers from price range like "RM 39-55"
            import re
            numbers = re.findall(r'\d+', price_range)
            if len(numbers) >= 2:
                total_min += int(numbers[0])
                total_max += int(numbers[1])
            elif len(numbers) == 1:
                total_min += int(numbers[0])
                total_max += int(numbers[0])
        
        return f"RM {total_min}-{total_max}"
    
    def _assess_malaysia_relevance(self, hashtag):
        """Assess how relevant the hashtag is to Malaysian market"""
        
        relevance_factors = {
            'barbiemakeup': 'High - Movie tie-in, social media viral',
            'barbiecore': 'Very High - Instagram trend, Gen Z appeal',
            'barbiepink': 'High - Iconic color, cross-generational',
            'naturalmakeup': 'Very High - Perfect for Malaysian climate',
            'cleangirl': 'High - Skincare focus popular in Malaysia',
            'glammakeup': 'Medium - Special occasions, festivals',
            'partyready': 'High - Malaysian party culture',
            'glassskin': 'High - K-beauty influence in Malaysia',
            'skincare': 'Very High - Skincare-conscious market'
        }
        
        return relevance_factors.get(hashtag, 'Medium - Monitor trend development')
    
    def _get_general_hashtag_recommendations(self, hashtag):
        """Get general recommendations for unmapped hashtags"""
        
        return {
            'hashtag': hashtag,
            'trend_description': f'General beauty trend analysis for #{hashtag}',
            'color_palette': ['Versatile', 'Adaptable', 'Trend-appropriate'],
            'look_style': 'Adaptable to trend requirements',
            'target_audience': 'Beauty enthusiasts, Trend followers',
            'recommended_products': [
                {
                    'product_id': 'true_match',
                    'product_name': 'True Match Foundation',
                    'category': 'Foundation',
                    'price_range': 'RM 49-69',
                    'description': 'Versatile foundation for any trend',
                    'image_url': '/static/images/true_match.jpg',
                    'availability': 'Very High',
                    'humidity_suitable': True,
                    'match_reason': 'Versatile foundation suitable for any trend',
                    'application_tip': 'Apply as needed for trend-appropriate coverage'
                }
            ],
            'application_tips': [
                'Adapt products to match trend aesthetic',
                'Consider Malaysian climate factors',
                'Test products before trend launch'
            ],
            'marketing_angles': [
                'Monitor trend development',
                'Adapt to Malaysian preferences',
                'Consider cultural factors'
            ],
            'total_products': 1,
            'estimated_cost': 'RM 49-69',
            'malaysia_relevance': 'Medium - Monitor trend development'
        }

# Initialize the Malaysia product engine
malaysia_product_engine = MalaysiaProductEngine()
