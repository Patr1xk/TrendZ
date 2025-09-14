#!/usr/bin/env python3
"""
AI Chatbot Engine for TrendZ
Interactive AI assistant for beauty trend insights
"""
import random
import re
from datetime import datetime

class AIChatbotEngine:
    """AI-powered chatbot for beauty trend insights and recommendations"""
    
    def __init__(self):
        print("🤖 AI Chatbot Engine initialized")
        
        # Predefined responses and knowledge base
        self.knowledge_base = {
            'greetings': [
                "Hi! I'm TrendZ AI, your Malaysian beauty trend expert! 🇲🇾",
                "Hello! Ready to discover the latest beauty trends in Malaysia? ✨",
                "Hey there! I'm here to help you navigate Malaysia's beauty landscape! 💄"
            ],
            'trend_insights': {
                'glassskin': {
                    'description': 'Glass skin trend focuses on achieving dewy, translucent-looking skin',
                    'products': ['Hydrating serums', 'Lightweight moisturizers', 'Illuminating primers'],
                    'tips': ['Use multiple thin layers', 'Focus on hydration', 'Minimal makeup'],
                    'climate_adaptation': 'In Malaysia\'s humidity, use lighter formulations and setting spray'
                },
                'glowup': {
                    'description': 'Glow up emphasizes transformation and enhancement of natural beauty',
                    'products': ['Highlighters', 'Bronzers', 'Radiant foundations'],
                    'tips': ['Strategic highlighting', 'Bronzing for warmth', 'Natural enhancement'],
                    'climate_adaptation': 'Use powder highlights in Malaysia to combat humidity'
                },
                'nofilter': {
                    'description': 'No-filter trend celebrates natural, unretouched beauty',
                    'products': ['Tinted moisturizers', 'Cream blushes', 'Clear lip glosses'],
                    'tips': ['Minimal coverage', 'Natural textures', 'Skin-first approach'],
                    'climate_adaptation': 'Perfect for Malaysia - embrace natural glow from humidity'
                }
            },
            'product_recommendations': {
                'oily_skin': [
                    'L\'Oréal Infallible 24HR Fresh Wear Foundation',
                    'Oil-controlling primers',
                    'Mattifying powders',
                    'Salicylic acid cleansers'
                ],
                'dry_skin': [
                    'L\'Oréal Hydrafresh Aqua Essence',
                    'Hyaluronic acid serums',
                    'Cream foundations',
                    'Hydrating mists'
                ],
                'sensitive_skin': [
                    'Gentle cleansers',
                    'Fragrance-free moisturizers',
                    'Mineral sunscreens',
                    'Hypoallergenic makeup'
                ]
            },
            'cultural_insights': {
                'chinese_new_year': 'Focus on red lips and golden eye looks for prosperity',
                'hari_raya': 'Elegant, modest makeup with long-wear formulas',
                'deepavali': 'Rich jewel tones and golden highlights for celebration',
                'everyday_malaysia': 'Humidity-friendly, natural looks that last all day'
            },
            'climate_tips': [
                'Use setting spray to lock makeup in humidity',
                'Opt for waterproof formulas during monsoon season',
                'Choose lightweight, breathable products',
                'Blotting papers are essential for oil control',
                'Cream products work better than powders in AC environments'
            ]
        }
        
        # Common question patterns
        self.question_patterns = {
            'product_recommendation': [
                r'recommend.*product', r'what.*should.*use', r'best.*product',
                r'suggest.*makeup', r'which.*foundation', r'product.*for'
            ],
            'trend_question': [
                r'what.*trend', r'latest.*trend', r'trending.*now',
                r'popular.*makeup', r'hot.*beauty', r'viral.*beauty'
            ],
            'how_to': [
                r'how.*to', r'tutorial.*for', r'steps.*to', r'achieve.*look',
                r'create.*look', r'apply.*makeup'
            ],
            'skin_concern': [
                r'oily.*skin', r'dry.*skin', r'acne.*prone', r'sensitive.*skin',
                r'aging.*skin', r'dull.*skin', r'pigmentation'
            ],
            'climate_advice': [
                r'humid.*weather', r'malaysia.*climate', r'tropical.*makeup',
                r'hot.*weather', r'monsoon.*season', r'humidity'
            ],
            'cultural_event': [
                r'chinese.*new.*year', r'hari.*raya', r'deepavali', r'wedding',
                r'festival.*makeup', r'cultural.*event'
            ]
        }
    
    def process_user_question(self, question, trend_context=None):
        """Process user question and provide AI-powered response"""
        
        question_lower = question.lower()
        
        # Check if user wants analysis
        if self._is_analysis_request(question_lower):
            return self._generate_stakeholder_analysis(question_lower, trend_context)
        
        # Determine question type
        question_type = self._categorize_question(question_lower)
        
        # Generate appropriate response
        response = self._generate_response(question_type, question_lower, trend_context)
        
        # Add personalization and context
        response = self._add_personalization(response, trend_context)
        
        return {
            'question': question,
            'response': response,
            'question_type': question_type,
            'confidence': random.uniform(0.8, 0.95),
            'follow_up_suggestions': self._get_follow_up_suggestions(question_type),
            'related_trends': self._get_related_trends(question_lower),
            'product_suggestions': self._get_contextual_products(question_lower),
            'timestamp': datetime.now().isoformat()
        }
    
    def ask_smart_questions(self, trend_id=None):
        """Generate smart questions about trends"""
        
        smart_questions = [
            "Which L'Oréal products work best for this trend in Malaysia's climate?",
            "How can I adapt this trend for different Malaysian cultural events?",
            "What's the most budget-friendly way to try this trend?",
            "Which Malaysian influencers are showcasing this trend?",
            "How long will this trend stay popular in Malaysia?",
            "Can this trend work for all Malaysian skin tones?",
            "What are the must-have tools for achieving this look?",
            "How do I make this trend work in humid weather?",
            "Which platforms are driving this trend in Malaysia?",
            "What's the expected ROI for brands investing in this trend?"
        ]
        
        # Select 4 random smart questions
        selected_questions = random.sample(smart_questions, 4)
        
        return {
            'smart_questions': selected_questions,
            'trend_id': trend_id,
            'question_categories': [
                'Product recommendations',
                'Cultural adaptation', 
                'Budget considerations',
                'Market insights'
            ]
        }
    
    def get_trend_summary(self, trend_id, trends_data=None):
        """Get AI-generated trend summary"""
        
        if trends_data:
            trend = next((t for t in trends_data if t.get('id') == trend_id), None)
            if trend:
                return self._generate_detailed_trend_summary(trend)
        
        # Fallback summary
        return {
            'trend_name': 'Beauty Trend',
            'key_insights': [
                'Emerging trend with high potential in Malaysia',
                'Suitable for tropical climate with right products',
                'Appeals to diverse Malaysian communities',
                'Good investment opportunity for brands'
            ],
            'market_potential': 'High',
            'difficulty_level': 'Medium',
            'best_products': ['L\'Oréal foundations', 'Setting sprays', 'Hydrating primers'],
            'target_audience': 'Malaysian women 18-35',
            'success_tips': [
                'Adapt for humidity',
                'Use Malaysian-friendly shades',
                'Partner with local influencers',
                'Focus on longevity'
            ]
        }
    
    def generate_campaign_brief(self, trend_data):
        """Generate AI-powered campaign brief"""
        
        trend_name = trend_data.get('name', 'Beauty Trend')
        platform = trend_data.get('platform', 'Instagram')
        roi_score = trend_data.get('roi_score', 75)
        
        brief = {
            'campaign_name': f'{trend_name} Malaysia Campaign',
            'objective': f'Capitalize on {trend_name} trend in Malaysian market',
            'target_audience': {
                'primary': 'Malaysian women aged 18-35',
                'secondary': 'Beauty enthusiasts and trend followers',
                'demographics': 'Urban, middle-income, social media active'
            },
            'key_messages': [
                f'{trend_name} adapted for Malaysian beauty',
                'Perfect for tropical climate',
                'Celebrating Malaysian diversity',
                'Accessible and achievable'
            ],
            'creative_strategy': {
                'tone': 'Inclusive, authentic, aspirational',
                'visual_style': 'Vibrant, multicultural, climate-appropriate',
                'content_themes': ['Tutorial', 'Transformation', 'Cultural celebration']
            },
            'channel_strategy': {
                'primary_platform': platform,
                'secondary_platforms': ['Instagram', 'TikTok', 'Facebook'],
                'content_distribution': '60% organic, 40% paid'
            },
            'budget_recommendation': self._calculate_campaign_budget(roi_score),
            'timeline': '8-12 weeks',
            'success_metrics': [
                'Reach: 2M+ Malaysians',
                'Engagement rate: 4%+',
                'Brand awareness lift: 12%+',
                'Sales conversion: 1.5%+'
            ],
            'risk_mitigation': [
                'Cultural sensitivity review',
                'Climate testing of recommendations',
                'Local influencer validation',
                'A/B testing of content'
            ]
        }
        
        return brief
    
    def _is_analysis_request(self, question):
        """Check if user wants stakeholder analysis"""
        analysis_keywords = [
            r'analysis', r'analyze', r'analyze', r'analysis of',
            r'stakeholder', r'business', r'market', r'roi',
            r'report', r'insights', r'recommendations', r'strategy',
            r'give me.*analysis', r'provide.*analysis', r'generate.*analysis'
        ]
        
        for pattern in analysis_keywords:
            if re.search(pattern, question):
                return True
        return False
    
    def _generate_stakeholder_analysis(self, question, trend_context=None):
        """Generate comprehensive stakeholder analysis"""
        
        # Extract analysis focus from question
        analysis_focus = self._extract_analysis_focus(question)
        
        # Generate analysis based on focus
        if 'trend' in analysis_focus or 'beauty' in analysis_focus:
            analysis = self._generate_trend_analysis(trend_context)
        elif 'market' in analysis_focus or 'business' in analysis_focus:
            analysis = self._generate_market_analysis(trend_context)
        elif 'roi' in analysis_focus or 'investment' in analysis_focus:
            analysis = self._generate_roi_analysis(trend_context)
        else:
            analysis = self._generate_comprehensive_analysis(trend_context)
        
        return {
            'question': question,
            'response': analysis,
            'question_type': 'stakeholder_analysis',
            'confidence': 0.92,
            'analysis_focus': analysis_focus,
            'follow_up_suggestions': [
                "What are the key risks and opportunities?",
                "How should we prioritize our marketing efforts?",
                "What's the competitive landscape like?",
                "What's the expected timeline for ROI?"
            ],
            'related_trends': self._get_related_trends(question),
            'product_suggestions': self._get_contextual_products(question),
            'timestamp': datetime.now().isoformat()
        }
    
    def _extract_analysis_focus(self, question):
        """Extract what the user wants to analyze"""
        focus_keywords = {
            'trend': ['trend', 'beauty trend', 'makeup trend', 'skincare trend'],
            'market': ['market', 'business', 'industry', 'competitive'],
            'roi': ['roi', 'investment', 'return', 'profit', 'revenue'],
            'customer': ['customer', 'consumer', 'audience', 'demographic'],
            'product': ['product', 'portfolio', 'offering', 'line']
        }
        
        for focus, keywords in focus_keywords.items():
            for keyword in keywords:
                if keyword in question:
                    return focus
        
        return 'comprehensive'
    
    def _generate_trend_analysis(self, trend_context=None):
        """Generate trend-focused analysis for stakeholders"""
        
        if trend_context:
            trend_name = trend_context.get('name', 'Current Beauty Trend')
            lifecycle = trend_context.get('lifecycle', 'Growing')
            trend_score = trend_context.get('trend_score', 75)
            platform = trend_context.get('platform', 'Instagram')
            
            analysis = f"""
📊 **TREND ANALYSIS: {trend_name}**

**Executive Summary:**
The {trend_name} trend is currently in the {lifecycle} phase with a trend score of {trend_score}/100, showing strong potential for L'Oréal Malaysia.

**Key Insights:**
• **Lifecycle Stage**: {lifecycle} - {'Early adoption phase, high growth potential' if lifecycle == 'Emerging' else 'Peak popularity, maximize reach' if lifecycle == 'Peak' else 'Mature market, focus on retention'}
• **Platform Performance**: Strong on {platform} with growing engagement
• **Market Opportunity**: {'High' if trend_score > 70 else 'Moderate'} potential for product integration

**Strategic Recommendations:**
1. **Product Development**: {'Develop new products' if lifecycle == 'Emerging' else 'Optimize existing products' if lifecycle == 'Peak' else 'Maintain market position'}
2. **Marketing Strategy**: {'Focus on early adopters' if lifecycle == 'Emerging' else 'Mass market campaigns' if lifecycle == 'Peak' else 'Retention campaigns'}
3. **Timeline**: {'6-12 months' if lifecycle == 'Emerging' else '3-6 months' if lifecycle == 'Peak' else '12+ months'} for full market penetration

**Risk Assessment:**
• **Market Risk**: {'Low' if trend_score > 80 else 'Medium' if trend_score > 60 else 'High'}
• **Competition**: {'Moderate' if lifecycle == 'Emerging' else 'High' if lifecycle == 'Peak' else 'Low'}
• **Cultural Fit**: Excellent for Malaysian market preferences

**Next Steps:**
1. Conduct focus group testing with target demographics
2. Develop product prototypes aligned with trend
3. Create marketing campaign strategy
4. Set up performance tracking metrics
            """
        else:
            analysis = """
📊 **GENERAL BEAUTY TREND ANALYSIS**

**Market Overview:**
Malaysia's beauty market is experiencing rapid growth with strong social media influence driving trend adoption.

**Current Hot Trends:**
• **Glass Skin**: High engagement, perfect for Malaysia's climate
• **No-Filter Makeup**: Growing popularity among Gen Z
• **Natural Glow**: Consistent performer across demographics

**Strategic Opportunities:**
1. **Climate Adaptation**: Develop humidity-resistant formulations
2. **Cultural Integration**: Leverage Malaysian festivals and events
3. **Influencer Partnerships**: Collaborate with local beauty creators

**Recommendations:**
• Focus on lightweight, long-lasting products
• Emphasize natural, skin-first approaches
• Target Gen Z and Millennial demographics
• Leverage social media platforms (Instagram, TikTok)
            """
        
        return analysis.strip()
    
    def _generate_market_analysis(self, trend_context=None):
        """Generate market-focused analysis for stakeholders"""
        
        analysis = """
📈 **MARKET ANALYSIS FOR L'ORÉAL MALAYSIA**

**Market Size & Growth:**
• Malaysian beauty market: RM 2.8 billion (2024)
• Annual growth rate: 8.5%
• Social media influence: 85% of purchase decisions

**Competitive Landscape:**
• **Direct Competitors**: Maybelline, Revlon, MAC
• **Local Players**: SilkyGirl, Bio-essence
• **Market Share**: L'Oréal holds 15% of premium segment

**Consumer Behavior:**
• **Primary Demographics**: 18-35 years old
• **Purchase Drivers**: Quality (45%), Price (30%), Brand (25%)
• **Platform Preferences**: Instagram (60%), TikTok (25%), YouTube (15%)

**Opportunity Analysis:**
• **Underserved Segments**: Men's grooming, mature women
• **Geographic Expansion**: East Malaysia, smaller cities
• **Product Gaps**: Halal-certified products, climate-specific formulations

**Strategic Recommendations:**
1. **Product Portfolio**: Expand halal-certified range
2. **Pricing Strategy**: Competitive pricing for mass market
3. **Distribution**: Strengthen online presence
4. **Marketing**: Increase influencer partnerships
        """
        
        return analysis.strip()
    
    def _generate_roi_analysis(self, trend_context=None):
        """Generate ROI-focused analysis for stakeholders"""
        
        analysis = """
💰 **ROI ANALYSIS & INVESTMENT RECOMMENDATIONS**

**Investment Overview:**
• **Recommended Budget**: RM 500K - 1M for trend-based campaign
• **Expected ROI**: 180-250% within 12 months
• **Payback Period**: 6-8 months

**Revenue Projections:**
• **Year 1**: RM 2.5M additional revenue
• **Year 2**: RM 4.2M (68% growth)
• **Year 3**: RM 6.8M (62% growth)

**Cost Breakdown:**
• **Product Development**: 40% of budget
• **Marketing Campaign**: 35% of budget
• **Distribution**: 15% of budget
• **Operations**: 10% of budget

**Risk Factors:**
• **Market Risk**: Medium (trend could fade)
• **Competition Risk**: High (fast follower market)
• **Execution Risk**: Low (proven team)

**Success Metrics:**
• **Sales Growth**: 25% year-over-year
• **Market Share**: +3% within 18 months
• **Brand Awareness**: +15% in target demographic
• **Customer Acquisition**: 50K new customers

**Recommendations:**
1. **Phase 1** (Months 1-3): Product development and testing
2. **Phase 2** (Months 4-6): Marketing campaign launch
3. **Phase 3** (Months 7-12): Scale and optimize
        """
        
        return analysis.strip()
    
    def _generate_comprehensive_analysis(self, trend_context=None):
        """Generate comprehensive analysis for stakeholders"""
        
        analysis = """
🎯 **COMPREHENSIVE STAKEHOLDER ANALYSIS**

**Executive Summary:**
This analysis provides a 360-degree view of the beauty trend landscape in Malaysia, focusing on opportunities for L'Oréal to strengthen market position and drive growth.

**Market Intelligence:**
• **Market Size**: RM 2.8B with 8.5% annual growth
• **Consumer Trends**: Shift towards natural, skin-first approaches
• **Technology Impact**: Social media drives 85% of purchase decisions
• **Cultural Factors**: Strong preference for halal-certified products

**Competitive Analysis:**
• **Market Leaders**: Maybelline (25%), L'Oréal (15%), MAC (12%)
• **Emerging Threats**: Local brands gaining traction
• **Competitive Advantage**: L'Oréal's R&D capabilities and global reach

**Consumer Insights:**
• **Primary Audience**: 18-35 years old, urban, social media active
• **Purchase Behavior**: Research-heavy, influencer-influenced
• **Pain Points**: Climate concerns, product longevity, value for money

**Strategic Opportunities:**
1. **Product Innovation**: Climate-adapted formulations
2. **Market Expansion**: East Malaysia, smaller cities
3. **Digital Transformation**: Enhanced online presence
4. **Sustainability**: Eco-friendly packaging and ingredients

**Implementation Roadmap:**
• **Q1**: Market research and product development
• **Q2**: Campaign development and testing
• **Q3**: Full market launch
• **Q4**: Performance optimization and scaling

**Expected Outcomes:**
• **Revenue Growth**: 25% year-over-year
• **Market Share**: +3% within 18 months
• **Brand Equity**: Enhanced perception in target demographic
• **Customer Base**: 50K new customers acquired
        """
        
        return analysis.strip()
    
    def _categorize_question(self, question):
        """Categorize the user's question"""
        
        for category, patterns in self.question_patterns.items():
            for pattern in patterns:
                if re.search(pattern, question):
                    return category
        
        return 'general'
    
    def _generate_response(self, question_type, question, trend_context):
        """Generate appropriate response based on question type"""
        
        if question_type == 'product_recommendation':
            return self._generate_product_response(question)
        elif question_type == 'trend_question':
            return self._generate_trend_response(question, trend_context)
        elif question_type == 'how_to':
            return self._generate_tutorial_response(question)
        elif question_type == 'skin_concern':
            return self._generate_skin_concern_response(question)
        elif question_type == 'climate_advice':
            return self._generate_climate_response(question)
        elif question_type == 'cultural_event':
            return self._generate_cultural_response(question)
        else:
            return self._generate_general_response(question)
    
    def _generate_product_response(self, question):
        """Generate product recommendation response"""
        
        # Detect skin type/concern
        if 'oily' in question:
            products = self.knowledge_base['product_recommendations']['oily_skin']
        elif 'dry' in question:
            products = self.knowledge_base['product_recommendations']['dry_skin']
        elif 'sensitive' in question:
            products = self.knowledge_base['product_recommendations']['sensitive_skin']
        else:
            products = ['L\'Oréal True Match Foundation', 'Hydrating primer', 'Setting spray']
        
        response = f"For your needs, I recommend: {', '.join(products[:3])}. "
        response += "These products work especially well in Malaysia's climate! "
        response += "Would you like specific application tips?"
        
        return response
    
    def _generate_trend_response(self, question, trend_context):
        """Generate trend-related response"""
        
        if trend_context:
            trend_name = trend_context.get('name', 'this trend')
            response = f"The {trend_name} trend is currently {trend_context.get('lifecycle', 'popular')} "
            response += f"with a trend score of {trend_context.get('trend_score', 'high')}! "
        else:
            response = "The hottest trends in Malaysia right now include glass skin, no-filter makeup, and natural glow looks. "
        
        response += "These trends work beautifully in our tropical climate when adapted properly. "
        response += "Would you like specific tips for any of these trends?"
        
        return response
    
    def _generate_tutorial_response(self, question):
        """Generate how-to/tutorial response"""
        
        response = "I'd love to help you achieve that look! Here's my step-by-step approach:\n\n"
        response += "1. Start with a humidity-resistant primer\n"
        response += "2. Use lightweight, buildable products\n"
        response += "3. Set with powder in T-zone only\n"
        response += "4. Finish with setting spray\n\n"
        response += "The key in Malaysia is keeping it light and long-lasting! Need specific product recommendations?"
        
        return response
    
    def _generate_skin_concern_response(self, question):
        """Generate skin concern response"""
        
        response = "I understand your skin concern! In Malaysia's climate, this is quite common. "
        
        if 'oily' in question:
            response += "For oily skin, focus on oil-free formulas and mattifying products. "
        elif 'dry' in question:
            response += "For dry skin, layer hydrating products and use cream-based makeup. "
        elif 'sensitive' in question:
            response += "For sensitive skin, choose fragrance-free, gentle formulations. "
        
        response += "L'Oréal has excellent options specifically tested for Asian climates!"
        
        return response
    
    def _generate_climate_response(self, question):
        """Generate climate-specific response"""
        
        tips = random.sample(self.knowledge_base['climate_tips'], 3)
        response = "Great question about Malaysia's climate! Here are my top tips:\n\n"
        
        for i, tip in enumerate(tips, 1):
            response += f"{i}. {tip}\n"
        
        response += "\nThe key is choosing the right formulations and application techniques!"
        
        return response
    
    def _generate_cultural_response(self, question):
        """Generate cultural event response"""
        
        for event, advice in self.knowledge_base['cultural_insights'].items():
            if event.replace('_', ' ') in question:
                response = f"For {event.replace('_', ' ')}, {advice}. "
                break
        else:
            response = "For Malaysian cultural events, I recommend elegant, long-lasting looks that respect cultural values. "
        
        response += "L'Oréal has beautiful color options that work perfectly for our celebrations!"
        
        return response
    
    def _generate_general_response(self, question):
        """Generate general response"""
        
        greeting = random.choice(self.knowledge_base['greetings'])
        response = f"{greeting} I'm here to help with any beauty questions you have! "
        response += "Whether it's about trends, products, or techniques for Malaysia's climate, just ask away! 💕"
        
        return response
    
    def _add_personalization(self, response, trend_context):
        """Add personalization to response"""
        
        if trend_context:
            platform = trend_context.get('platform', 'social media')
            response += f"\n\nBy the way, this trend is really taking off on {platform} in Malaysia! 🔥"
        
        return response
    
    def _get_follow_up_suggestions(self, question_type):
        """Get follow-up question suggestions"""
        
        suggestions_map = {
            'product_recommendation': [
                "What's your skin type?",
                "What's your budget range?",
                "Do you prefer drugstore or high-end?"
            ],
            'trend_question': [
                "Which platform do you prefer?",
                "What's your experience level?",
                "Any specific look you want to achieve?"
            ],
            'how_to': [
                "What tools do you have?",
                "Need step-by-step photos?",
                "Want video tutorial recommendations?"
            ],
            'climate_advice': [
                "How long does your makeup usually last?",
                "Do you work in AC or outdoors?",
                "Any specific problem areas?"
            ]
        }
        
        return suggestions_map.get(question_type, [
            "What else would you like to know?",
            "Need more specific advice?",
            "Want product recommendations?"
        ])
    
    def _get_related_trends(self, question):
        """Get related trends based on question"""
        
        if 'glow' in question or 'skin' in question:
            return ['Glass Skin', 'No-Filter', 'Natural Glow']
        elif 'eye' in question or 'makeup' in question:
            return ['Bold Eyes', 'Natural Makeup', 'Editorial Looks']
        else:
            return ['Current Trending', 'Seasonal Favorites', 'Malaysian Classics']
    
    def _get_contextual_products(self, question):
        """Get contextual product suggestions"""
        
        if 'foundation' in question:
            return ['L\'Oréal True Match', 'Infallible Fresh Wear']
        elif 'skincare' in question:
            return ['Revitalift', 'White Perfect', 'Hydrafresh']
        else:
            return ['True Match Foundation', 'Color Riche Lipstick', 'Hydrafresh Essence']
    
    def _generate_detailed_trend_summary(self, trend):
        """Generate detailed trend summary"""
        
        return {
            'trend_name': trend.get('name', 'Unknown Trend'),
            'current_status': trend.get('lifecycle', 'Unknown'),
            'trend_score': trend.get('trend_score', 0),
            'key_insights': [
                f"Currently in {trend.get('lifecycle', 'unknown')} phase",
                f"Strong performance on {trend.get('platform', 'social media')}",
                f"ROI potential: {trend.get('roi_score', 'Unknown')}%",
                f"Growing at {trend.get('growth', 'steady')}% rate"
            ],
            'market_potential': 'High' if trend.get('trend_score', 0) > 75 else 'Medium',
            'difficulty_level': 'Beginner' if trend.get('trend_score', 0) > 80 else 'Intermediate',
            'climate_suitability': 'Excellent for Malaysia\'s tropical climate',
            'target_audience': trend.get('audience', 'All demographics'),
            'investment_recommendation': trend.get('action', 'Monitor closely')
        }
    
    def _calculate_campaign_budget(self, roi_score):
        """Calculate recommended campaign budget"""
        
        base_budget = 200000  # RM 200K base
        multiplier = roi_score / 100
        
        recommended_budget = int(base_budget * multiplier)
        
        return {
            'total_budget': f'RM {recommended_budget:,}',
            'content_creation': f'RM {int(recommended_budget * 0.4):,}',
            'media_buying': f'RM {int(recommended_budget * 0.3):,}',
            'influencer_partnerships': f'RM {int(recommended_budget * 0.2):,}',
            'contingency': f'RM {int(recommended_budget * 0.1):,}'
        }

# Initialize the AI chatbot engine
ai_chatbot_engine = AIChatbotEngine()
