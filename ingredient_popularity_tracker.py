#!/usr/bin/env python3
"""
Ingredient Popularity Tracker for TrendZ
Tracks trending beauty ingredients and their popularity
"""
import random
from datetime import datetime, timedelta

class IngredientPopularityTracker:
    """Tracks popularity of beauty ingredients"""
    
    def __init__(self):
        print("🧪 Ingredient Popularity Tracker initialized")
        
        # Comprehensive ingredient database
        self.ingredients_db = {
            'skincare': {
                'hyaluronic_acid': {
                    'name': 'Hyaluronic Acid',
                    'category': 'Hydrating',
                    'benefits': ['Deep hydration', 'Plumping effect', 'Suitable for all skin types'],
                    'trending_score': random.randint(85, 95)
                },
                'niacinamide': {
                    'name': 'Niacinamide',
                    'category': 'Multi-purpose',
                    'benefits': ['Pore minimizing', 'Oil control', 'Brightening'],
                    'trending_score': random.randint(80, 90)
                },
                'retinol': {
                    'name': 'Retinol',
                    'category': 'Anti-aging',
                    'benefits': ['Wrinkle reduction', 'Skin renewal', 'Texture improvement'],
                    'trending_score': random.randint(75, 85)
                },
                'vitamin_c': {
                    'name': 'Vitamin C',
                    'category': 'Antioxidant',
                    'benefits': ['Brightening', 'Antioxidant protection', 'Collagen support'],
                    'trending_score': random.randint(82, 92)
                },
                'ceramides': {
                    'name': 'Ceramides',
                    'category': 'Barrier repair',
                    'benefits': ['Barrier restoration', 'Moisture retention', 'Sensitive skin friendly'],
                    'trending_score': random.randint(70, 80)
                },
                'salicylic_acid': {
                    'name': 'Salicylic Acid',
                    'category': 'Exfoliating',
                    'benefits': ['Acne treatment', 'Pore cleaning', 'Texture smoothing'],
                    'trending_score': random.randint(78, 88)
                }
            },
            'makeup': {
                'peptides': {
                    'name': 'Peptides',
                    'category': 'Anti-aging makeup',
                    'benefits': ['Skin firming', 'Long-wear', 'Skincare benefits'],
                    'trending_score': random.randint(65, 75)
                },
                'squalane': {
                    'name': 'Squalane',
                    'category': 'Hydrating makeup',
                    'benefits': ['Moisture boost', 'Smooth application', 'Non-comedogenic'],
                    'trending_score': random.randint(60, 70)
                }
            },
            'hair': {
                'argan_oil': {
                    'name': 'Argan Oil',
                    'category': 'Nourishing',
                    'benefits': ['Hair softening', 'Shine enhancement', 'Damage repair'],
                    'trending_score': random.randint(70, 80)
                },
                'keratin': {
                    'name': 'Keratin',
                    'category': 'Strengthening',
                    'benefits': ['Hair strengthening', 'Frizz control', 'Shine boost'],
                    'trending_score': random.randint(65, 75)
                }
            }
        }
    
    def track_ingredient_popularity(self):
        """Track current ingredient popularity"""
        print("🧪 Tracking ingredient popularity...")
        print("📊 Tracking ingredient popularity...")
        
        popular_ingredients = []
        
        for category, ingredients in self.ingredients_db.items():
            for ingredient_id, ingredient_data in ingredients.items():
                
                # Simulate real-time popularity tracking
                base_score = ingredient_data['trending_score']
                current_score = base_score + random.randint(-5, 15)  # Add volatility
                
                # Calculate trend metrics
                search_volume = random.randint(10000, 500000)
                social_mentions = random.randint(5000, 100000)
                product_launches = random.randint(5, 50)
                
                # Growth calculation
                growth_rate = random.uniform(-10, 30)
                
                ingredient_info = {
                    'ingredient_id': ingredient_id,
                    'name': ingredient_data['name'],
                    'category': category,
                    'subcategory': ingredient_data['category'],
                    'trending_score': min(100, max(0, current_score)),
                    'growth_rate': round(growth_rate, 1),
                    'search_volume': search_volume,
                    'social_mentions': social_mentions,
                    'product_launches': product_launches,
                    'benefits': ingredient_data['benefits'],
                    'trend_direction': self._determine_trend_direction(growth_rate),
                    'market_penetration': random.uniform(0.1, 0.8),
                    'price_impact': random.choice(['Premium', 'Mid-range', 'Accessible']),
                    'consumer_awareness': random.uniform(0.3, 0.9),
                    'expert_rating': random.uniform(7.0, 9.5),
                    'safety_profile': random.choice(['Excellent', 'Good', 'Moderate']),
                    'recommended_for': self._get_recommendations(ingredient_data),
                    'last_updated': datetime.now().isoformat()
                }
                
                popular_ingredients.append(ingredient_info)
        
        # Sort by trending score
        popular_ingredients.sort(key=lambda x: x['trending_score'], reverse=True)
        
        print(f"✅ Tracked popularity for {len(popular_ingredients)} ingredients")
        return popular_ingredients
    
    def analyze_ingredient_trends(self, ingredients_list):
        """Analyze trends in ingredient popularity"""
        
        analysis = {
            'top_trending': self._get_top_trending(ingredients_list),
            'emerging_ingredients': self._get_emerging_ingredients(ingredients_list),
            'declining_ingredients': self._get_declining_ingredients(ingredients_list),
            'category_analysis': self._analyze_by_category(ingredients_list),
            'market_insights': self._generate_market_insights(ingredients_list),
            'predictions': self._generate_predictions(ingredients_list)
        }
        
        return analysis
    
    def get_ingredient_recommendations(self, skin_concern, category='skincare'):
        """Get ingredient recommendations for specific concerns"""
        
        concern_mapping = {
            'acne': ['salicylic_acid', 'niacinamide'],
            'aging': ['retinol', 'vitamin_c', 'peptides'],
            'hydration': ['hyaluronic_acid', 'ceramides', 'squalane'],
            'brightening': ['vitamin_c', 'niacinamide'],
            'sensitive': ['ceramides', 'hyaluronic_acid'],
            'oily': ['niacinamide', 'salicylic_acid'],
            'dry': ['hyaluronic_acid', 'ceramides', 'squalane']
        }
        
        recommended_ids = concern_mapping.get(skin_concern.lower(), ['hyaluronic_acid'])
        recommendations = []
        
        for ingredient_id in recommended_ids:
            if category in self.ingredients_db and ingredient_id in self.ingredients_db[category]:
                ingredient = self.ingredients_db[category][ingredient_id].copy()
                ingredient['ingredient_id'] = ingredient_id
                ingredient['trending_score'] = random.randint(70, 95)
                recommendations.append(ingredient)
        
        return recommendations
    
    def predict_next_trending_ingredient(self):
        """Predict the next ingredient likely to trend"""
        
        # Emerging ingredients with potential
        emerging_candidates = [
            {
                'name': 'Bakuchiol',
                'category': 'Natural retinol alternative',
                'trend_potential': 85,
                'predicted_peak': '3-6 months',
                'key_benefits': ['Gentle anti-aging', 'Pregnancy-safe', 'Antioxidant'],
                'target_audience': 'Sensitive skin, pregnant women'
            },
            {
                'name': 'Polyglutamic Acid',
                'category': 'Advanced hydrator',
                'trend_potential': 78,
                'predicted_peak': '6-9 months',
                'key_benefits': ['Superior hydration', 'Moisture retention', 'Plumping'],
                'target_audience': 'Dry skin, mature skin'
            },
            {
                'name': 'Centella Asiatica',
                'category': 'Soothing botanical',
                'trend_potential': 82,
                'predicted_peak': '2-4 months',
                'key_benefits': ['Anti-inflammatory', 'Healing', 'Calming'],
                'target_audience': 'Irritated skin, rosacea'
            },
            {
                'name': 'Azelaic Acid',
                'category': 'Multi-tasking acid',
                'trend_potential': 75,
                'predicted_peak': '4-7 months',
                'key_benefits': ['Acne treatment', 'Brightening', 'Rosacea relief'],
                'target_audience': 'Acne-prone, sensitive skin'
            }
        ]
        
        # Sort by trend potential
        emerging_candidates.sort(key=lambda x: x['trend_potential'], reverse=True)
        
        return emerging_candidates[0]  # Return the top candidate
    
    def _determine_trend_direction(self, growth_rate):
        """Determine trend direction based on growth rate"""
        if growth_rate > 15:
            return 'Rapidly Rising'
        elif growth_rate > 5:
            return 'Rising'
        elif growth_rate > -5:
            return 'Stable'
        elif growth_rate > -15:
            return 'Declining'
        else:
            return 'Rapidly Declining'
    
    def _get_recommendations(self, ingredient_data):
        """Get usage recommendations for ingredient"""
        category = ingredient_data['category'].lower()
        
        recommendations = {
            'hydrating': ['Dry skin', 'All skin types', 'Post-treatment'],
            'anti-aging': ['Mature skin', '25+ years', 'Prevention'],
            'exfoliating': ['Textured skin', 'Acne-prone', 'Dull complexion'],
            'brightening': ['Hyperpigmentation', 'Dull skin', 'Even tone'],
            'multi-purpose': ['All skin types', 'Combination skin', 'Minimalist routine']
        }
        
        return recommendations.get(category, ['Consult dermatologist'])
    
    def _get_top_trending(self, ingredients_list):
        """Get top trending ingredients"""
        return sorted(ingredients_list, key=lambda x: x['trending_score'], reverse=True)[:5]
    
    def _get_emerging_ingredients(self, ingredients_list):
        """Get emerging ingredients (high growth, medium score)"""
        emerging = [
            ing for ing in ingredients_list 
            if ing['growth_rate'] > 10 and 60 <= ing['trending_score'] <= 80
        ]
        return sorted(emerging, key=lambda x: x['growth_rate'], reverse=True)[:3]
    
    def _get_declining_ingredients(self, ingredients_list):
        """Get declining ingredients"""
        declining = [
            ing for ing in ingredients_list 
            if ing['growth_rate'] < -5
        ]
        return sorted(declining, key=lambda x: x['growth_rate'])[:3]
    
    def _analyze_by_category(self, ingredients_list):
        """Analyze ingredients by category"""
        categories = {}
        
        for ingredient in ingredients_list:
            category = ingredient['category']
            if category not in categories:
                categories[category] = {
                    'count': 0,
                    'avg_score': 0,
                    'avg_growth': 0,
                    'top_ingredient': None
                }
            
            cat_data = categories[category]
            cat_data['count'] += 1
            cat_data['avg_score'] += ingredient['trending_score']
            cat_data['avg_growth'] += ingredient['growth_rate']
            
            if not cat_data['top_ingredient'] or ingredient['trending_score'] > cat_data['top_ingredient']['trending_score']:
                cat_data['top_ingredient'] = ingredient
        
        # Calculate averages
        for category in categories:
            cat_data = categories[category]
            cat_data['avg_score'] = round(cat_data['avg_score'] / cat_data['count'], 1)
            cat_data['avg_growth'] = round(cat_data['avg_growth'] / cat_data['count'], 1)
        
        return categories
    
    def _generate_market_insights(self, ingredients_list):
        """Generate market insights"""
        total_ingredients = len(ingredients_list)
        high_trending = len([i for i in ingredients_list if i['trending_score'] > 80])
        growing = len([i for i in ingredients_list if i['growth_rate'] > 5])
        
        return {
            'market_health': 'Strong' if high_trending / total_ingredients > 0.3 else 'Moderate',
            'innovation_rate': 'High' if growing / total_ingredients > 0.4 else 'Moderate',
            'consumer_education_needed': total_ingredients - len([i for i in ingredients_list if i['consumer_awareness'] > 0.7]),
            'premium_opportunities': len([i for i in ingredients_list if i['price_impact'] == 'Premium']),
            'accessibility_focus': len([i for i in ingredients_list if i['price_impact'] == 'Accessible'])
        }
    
    def _generate_predictions(self, ingredients_list):
        """Generate future predictions"""
        return {
            'next_6_months': [
                'Continued growth in multi-functional ingredients',
                'Increased focus on gentle, sensitive skin formulations',
                'Rise of sustainable and naturally-derived actives'
            ],
            'emerging_categories': [
                'Microbiome-supporting ingredients',
                'Blue light protection compounds',
                'Pollution defense actives'
            ],
            'market_opportunities': [
                'Education-focused marketing',
                'Personalized ingredient recommendations',
                'Combination therapy products'
            ]
        }

# Initialize the tracker
ingredient_tracker = IngredientPopularityTracker()
