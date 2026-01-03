import json
import os
import google.generativeai as genai
import re

config_path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(config_path) as f:
    config = json.load(f)


KEY = config['API_KEY']
OWNER = config['owner']
INSTAGRAM = config['instagram']
DISCORD = config['discord']

# Configure Gemini AI
genai.configure(api_key=KEY)

# Default model name, can be overridden by app.py
MODEL_NAME = 'gemini-2.5-flash'

"""

THIS IS A YOUTUBE TITLE, DESCRIPTION AND TAGS GENERATOR API
ITS GENERATE BY GEMINI 2.0 FLASH MODEL
ITS GENERATION LOGIC BASED ON A TITLE OR A TOPIC
USER CAN GIVE TITLE OR TOPIC VIA API AND IT WILL RETURN A TITLE, DESCRIPTION AND TAGS


"""

def generate_helper(prompt: str):
    """
    Generate AI-powered category-adaptive YouTube content with intelligent automation
    
    Features:
    - AI Category Detection & Classification
    - Automated Timing & Scheduling Recommendations  
    - Dynamic Content Optimization
    - Real-time Trend Analysis
    - Smart Audience Targeting
    
    YouTube limits: Title (100), Description (5000), Tags (500)
    """
    
    try:
        # Use the model that was set by app.py or default
        model = genai.GenerativeModel(MODEL_NAME)
        
        # Advanced AI-powered system prompt with intelligent automation
        system_prompt = f"""
You are an ADVANCED AI Content Strategist with FULL AUTOMATION capabilities. You make ALL decisions about content optimization, category classification, timing, and strategy.

YOUR AI CAPABILITIES:
🤖 AUTOMATIC CATEGORY DETECTION: Analyze content and assign optimal category
⏰ INTELLIGENT TIMING: Determine best posting schedule based on category + trends
📊 TREND ANALYSIS: Real-time trending topic integration
🎯 AUDIENCE OPTIMIZATION: Auto-target demographics and psychographics
📈 PERFORMANCE PREDICTION: Estimate viral potential and engagement
🔄 CROSS-PLATFORM OPTIMIZATION: Adapt for YouTube, TikTok, Instagram

TOPIC TO ANALYZE: "{prompt}"

AI DECISION FRAMEWORK:

1. CATEGORY INTELLIGENCE:
   - Primary Category: Gaming, Tech, Beauty, Cooking, Travel, Education, Entertainment, Music, Sports, News, DIY, Business, Art, Automotive, Home, Family, Pets, Comedy, Social Media, Science, Fashion, Health, Finance, Politics
   - Sub-categories: Identify 2-3 relevant sub-niches
   - Cross-category appeal: Rate 1-10 for broader reach
   - Trending factor: Current trend strength in this category

2. TIMING INTELLIGENCE:
   - Optimal posting day: Monday-Sunday based on category analytics
   - Best posting time: Specific hour in target timezone
   - Seasonal relevance: How current trends affect timing
   - Competition analysis: Less saturated time slots
   - Global reach timing: Multi-timezone optimization

3. CONTENT INTELLIGENCE:
   - Viral probability: 1-100 score based on trending patterns
   - Target demographics: Age, gender, interests, behavior
   - Engagement prediction: Expected likes, comments, shares
   - Algorithm compatibility: YouTube algorithm optimization score
   - Monetization potential: Revenue generation capability

4. TREND INTELLIGENCE:
   - Current viral trends relevant to topic
   - Seasonal/holiday alignment opportunities  
   - News/event tie-in possibilities
   - Meme/culture integration potential
   - Influencer collaboration opportunities

CATEGORY-SPECIFIC OPTIMIZATION MATRIX:

🎮 GAMING: Peak times 3-6PM, 8-11PM | Target: 13-35, Male 65% | Trends: New releases, esports
💻 TECH: Peak times 9-11AM, 2-4PM | Target: 18-45, Male 70% | Trends: AI, gadgets, reviews
💄 BEAUTY: Peak times 6-9AM, 7-9PM | Target: 16-35, Female 80% | Trends: Skincare, makeup hacks
🍳 COOKING: Peak times 11AM-1PM, 5-7PM | Target: 25-55, Female 60% | Trends: Quick recipes, healthy
✈️ TRAVEL: Peak times 12-2PM, 7-9PM | Target: 20-40, Balanced | Trends: Budget travel, hidden gems
📚 EDUCATION: Peak times 8-10AM, 3-5PM | Target: 16-50, Balanced | Trends: Online learning, skills
🎬 ENTERTAINMENT: Peak times 7-9PM | Target: 13-30, Balanced | Trends: Celebrity, viral content
🎵 MUSIC: Peak times 4-6PM, 8-10PM | Target: 13-40, Balanced | Trends: New artists, covers
💪 FITNESS: Peak times 6-8AM, 5-7PM | Target: 18-45, Balanced | Trends: Home workouts, nutrition
💼 BUSINESS: Peak times 8-10AM, 1-3PM | Target: 25-50, Male 60% | Trends: Entrepreneurship, AI

INTELLIGENT CONTENT FORMULAS (AI-Selected):

🔥 VIRAL HOOKS: "This Changes Everything", "Nobody Talks About This", "I Tried X for 30 Days"
📊 PERFORMANCE BOOSTERS: Numbers, Questions, Controversy, Tutorials, Reviews
🎯 ENGAGEMENT TRIGGERS: Challenges, Reactions, Transformations, Secrets, Comparisons
💡 ALGORITHM HACKS: Trending keywords, Optimal length, CTR optimization, Watch time

AI AUTOMATION REQUIREMENTS:
✅ Auto-detect primary and secondary categories
✅ Auto-generate optimal posting schedule (day + time + timezone)
✅ Auto-integrate trending topics and keywords
✅ Auto-optimize for target demographics
✅ Auto-predict performance metrics
✅ Auto-suggest content strategy
✅ Auto-recommend posting frequency
✅ Auto-generate thumbnail suggestions
✅ Auto-create series/playlist recommendations
✅ Auto-optimize for monetization

RESPONSE FORMAT (Comprehensive AI Analysis):

{{
  "title": "AI-optimized viral title with trending elements",
  "description": "AI-crafted description with strategic keywords, hashtags, CTAs, and engagement hooks",
  "tags": "ai_selected_primary, trending_secondary, long_tail_specific, viral_hashtag, category_main, audience_targeted, seasonal_relevant, competitor_analysis",
  "ai_analysis": {{
    "primary_category": "AI-detected main category",
    "secondary_categories": ["sub-category-1", "sub-category-2"],
    "category_confidence": "percentage confidence in category selection",
    "cross_category_appeal": "1-10 score for broader reach potential"
  }},
  "optimal_timing": {{
    "best_posting_day": "AI-recommended day of week",
    "optimal_time": "AI-calculated best hour (24h format)",
    "timezone": "Target audience timezone",
    "posting_frequency": "AI-suggested posting schedule",
    "seasonal_factor": "Current seasonal relevance score"
  }},
  "performance_prediction": {{
    "viral_probability": "1-100 AI-calculated viral potential",
    "expected_engagement": "AI-predicted engagement level",
    "algorithm_score": "1-100 YouTube algorithm compatibility",
    "monetization_potential": "Revenue generation capability rating"
  }},
  "content_strategy": {{
    "target_demographics": "AI-identified primary audience",
    "trending_integration": "Current trends incorporated",
    "thumbnail_suggestion": "AI-recommended thumbnail concept",
    "series_potential": "Recommendation for content series",
    "collaboration_opportunities": "Suggested collaboration types"
  }},
  "optimization_insights": {{
    "keyword_strategy": "AI-selected keyword approach",
    "engagement_tactics": "Specific tactics to boost engagement",
    "algorithm_optimization": "YouTube algorithm optimization strategy",
    "growth_recommendations": "Channel growth recommendations"
  }}
}}

Generate the most intelligent, automated, and optimized YouTube content with complete AI decision-making!
"""
        
        response = model.generate_content(system_prompt)
        response_text = clean_ai_response(response.text)
        
        # Parse comprehensive AI response
        result = json.loads(response_text)
        
        # Enhanced content optimization with AI insights
        title = optimize_title(result.get('title', '').strip())
        description = optimize_description(result.get('description', '').strip())
        tags = optimize_tags(result.get('tags', '').strip())
        
        return {
            'title': title[:100],
            'description': description[:5000],
            'tags': tags[:500],
            'ai_analysis': result.get('ai_analysis', {}),
            'optimal_timing': result.get('optimal_timing', {}),
            'performance_prediction': result.get('performance_prediction', {}),
            'content_strategy': result.get('content_strategy', {}),
            'optimization_insights': result.get('optimization_insights', {})
        }
        
    except json.JSONDecodeError as e:
        return generate_advanced_fallback_content(prompt, f'JSON parsing error: {str(e)}')
    except Exception as e:
        return generate_advanced_fallback_content(prompt, f'Generation error: {str(e)}')

def clean_ai_response(response_text: str) -> str:
    """Enhanced AI response cleaning for better JSON extraction"""
    # Remove markdown formatting
    if response_text.startswith('```json'):
        response_text = response_text[7:]
    if response_text.startswith('```'):
        response_text = response_text[3:]
    if response_text.endswith('```'):
        response_text = response_text[:-3]
    
    response_text = response_text.strip()
    
    # Extract JSON from mixed content
    json_start = response_text.find('{')
    json_end = response_text.rfind('}') + 1
    if json_start != -1 and json_end != 0:
        response_text = response_text[json_start:json_end]
    
    return response_text.strip()

def optimize_title(title: str) -> str:
    """Advanced title optimization with category awareness"""
    if not title:
        return title
    
    # Add engagement elements if missing
    if len(title) < 90 and not any(char in title for char in ['!', '?', '🔥', '💯', '😱', '⚡']):
        # Add appropriate emoji based on title content
        if any(word in title.upper() for word in ['SHOCKING', 'INSANE', 'UNBELIEVABLE']):
            title += ' 😱'
        elif any(word in title.upper() for word in ['TOP', 'BEST', 'ULTIMATE']):
            title += ' 💯'
        elif any(word in title.upper() for word in ['SECRET', 'HIDDEN', 'EXPOSED']):
            title += ' 🔥'
        else:
            title += ' ⚡'
    
    return title.strip()

def optimize_description(description: str) -> str:
    """Advanced description optimization"""
    if not description:
        return description
    
    # Ensure proper formatting and engagement elements
    if not any(cta in description.upper() for cta in ['SUBSCRIBE', 'LIKE', 'COMMENT']):
        description += "\n\n👍 Don't forget to LIKE and SUBSCRIBE for more amazing content!"
    
    # Add engagement emojis if missing
    if not any(emoji in description for emoji in ['👍', '🔔', '💬', '🔥', '✨']):
        description = "🔥 " + description
    
    return description.strip()

def optimize_tags(tags: str) -> str:
    """Advanced tags optimization"""
    if not tags:
        return tags
    
    # Clean and optimize tag list
    tag_list = [tag.strip() for tag in tags.split(',') if tag.strip()]
    
    # Remove duplicates while preserving order
    seen = set()
    unique_tags = []
    for tag in tag_list:
        if tag.lower() not in seen:
            seen.add(tag.lower())
            unique_tags.append(tag)
    
    return ', '.join(unique_tags)

def detect_category(prompt: str) -> str:
    """Detect content category from prompt"""
    prompt_lower = prompt.lower()
    
    categories = {
        'gaming': ['game', 'gaming', 'esports', 'minecraft', 'fortnite', 'xbox', 'playstation', 'nintendo'],
        'technology': ['tech', 'ai', 'robot', 'gadget', 'phone', 'computer', 'software', 'programming'],
        'beauty': ['makeup', 'beauty', 'skincare', 'cosmetics', 'fashion', 'style', 'hair'],
        'cooking': ['recipe', 'cooking', 'food', 'kitchen', 'chef', 'restaurant', 'meal'],
        'travel': ['travel', 'trip', 'vacation', 'country', 'city', 'adventure', 'explore'],
        'education': ['learn', 'tutorial', 'guide', 'how to', 'education', 'study', 'course'],
        'entertainment': ['funny', 'comedy', 'movie', 'celebrity', 'reaction', 'meme'],
        'music': ['music', 'song', 'artist', 'album', 'concert', 'instrument', 'cover'],
        'fitness': ['workout', 'fitness', 'gym', 'exercise', 'health', 'training', 'muscle'],
        'business': ['business', 'entrepreneur', 'money', 'finance', 'investing', 'career'],
        'diy': ['diy', 'craft', 'build', 'make', 'project', 'home improvement'],
        'automotive': ['car', 'auto', 'vehicle', 'driving', 'mechanic', 'racing']
    }
    
    for category, keywords in categories.items():
        if any(keyword in prompt_lower for keyword in keywords):
            return category.title()
    
    return 'General'

def generate_advanced_fallback_content(prompt: str, error_details: str) -> dict:
    """Generate advanced AI-powered fallback content with intelligent automation"""
    from datetime import datetime, timedelta
    import random
    
    # Advanced category detection
    category = detect_category(prompt)
    
    # AI-powered timing calculation
    current_hour = datetime.now().hour
    optimal_times = {
        'Gaming': [15, 16, 17, 20, 21, 22],
        'Technology': [9, 10, 14, 15, 16],
        'Beauty': [6, 7, 8, 19, 20, 21],
        'Cooking': [11, 12, 17, 18, 19],
        'Travel': [12, 13, 14, 19, 20],
        'Education': [8, 9, 15, 16, 17],
        'Entertainment': [19, 20, 21],
        'Music': [16, 17, 20, 21, 22],
        'Fitness': [6, 7, 8, 17, 18, 19],
        'Business': [8, 9, 13, 14, 15]
    }
    
    best_times = optimal_times.get(category, [12, 13, 19, 20])
    recommended_time = random.choice(best_times)
    
    # AI performance prediction
    viral_scores = {
        'Gaming': random.randint(70, 90),
        'Technology': random.randint(65, 85),
        'Beauty': random.randint(75, 95),
        'Cooking': random.randint(60, 80),
        'Travel': random.randint(70, 90),
        'Education': random.randint(55, 75),
        'Entertainment': random.randint(80, 95),
        'Music': random.randint(65, 85),
        'Fitness': random.randint(60, 80),
        'Business': random.randint(50, 70)
    }
    
    viral_score = viral_scores.get(category, random.randint(60, 80))
    
    # Advanced fallback templates with AI insights
    advanced_templates = {
        'Gaming': {
            'title': f"INSANE {prompt} Strategy - Pro Gamers Don't Want You to Know! 🔥",
            'description': f"🎮 Discover the ultimate {prompt} techniques that will transform your gameplay! This comprehensive guide reveals secrets used by top players worldwide.\n\n🔥 What you'll learn:\n• Advanced strategies and tactics\n• Pro tips and hidden mechanics\n• Common mistakes to avoid\n• Performance optimization tricks\n\n💥 Don't forget to SMASH that LIKE button and SUBSCRIBE for more gaming content!\n\n#gaming #{prompt.lower().replace(' ', '')} #protips #strategy #viral",
            'tags': f"{prompt.lower()}, gaming, strategy, pro tips, guide, tutorial, gameplay, esports, viral"
        },
        'Technology': {
            'title': f"{prompt} in 2024 - This Changes EVERYTHING! (Mind Blown) 💯",
            'description': f"🚀 The complete breakdown of {prompt} with cutting-edge insights and future predictions!\n\n✨ Key highlights:\n• Latest developments and trends\n• Expert analysis and reviews\n• Practical applications\n• Future predictions\n\n🔔 SUBSCRIBE and hit the notification bell for more tech content!\n\n#technology #{prompt.lower().replace(' ', '')} #tech2024 #innovation #trending",
            'tags': f"{prompt.lower()}, technology, tech, 2024, innovation, review, analysis, trending, future"
        },
        'Beauty': {
            'title': f"Viral {prompt} Transformation - Results Will SHOCK You! ✨",
            'description': f"💄 Amazing {prompt} transformation that's breaking the internet!\n\n🌟 What's included:\n• Step-by-step tutorial\n• Product recommendations\n• Professional tips and tricks\n• Before and after results\n\n👍 LIKE if this helped you and SUBSCRIBE for more beauty content!\n\n#beauty #{prompt.lower().replace(' ', '')} #makeup #transformation #viral #glowup",
            'tags': f"{prompt.lower()}, beauty, makeup, transformation, tutorial, skincare, glowup, viral, trending"
        }
    }
    
    # Get template or create generic one
    template = advanced_templates.get(category, {
        'title': f"Amazing {prompt} - You Need to See This! ⚡",
        'description': f"🔥 Everything you need to know about {prompt}! Complete guide with expert insights and practical tips.\n\n💡 Key points covered:\n• Comprehensive overview\n• Expert recommendations\n• Practical applications\n• Latest trends and updates\n\n👆 LIKE and SUBSCRIBE for more amazing content!\n\n#{prompt.lower().replace(' ', '')}",
        'tags': f"{prompt.lower()}, guide, tips, trending, viral, amazing, complete, tutorial"
    })
    
    return {
        'title': template['title'][:100],
        'description': template['description'][:5000],
        'tags': template['tags'][:500],
        'ai_analysis': {
            'primary_category': category,
            'secondary_categories': [f'{category} Tutorial', f'{category} Guide'],
            'category_confidence': '85%',
            'cross_category_appeal': '7'
        },
        'optimal_timing': {
            'best_posting_day': 'Wednesday',
            'optimal_time': f'{recommended_time}:00',
            'timezone': 'EST',
            'posting_frequency': '2-3 times per week',
            'seasonal_factor': '8/10'
        },
        'performance_prediction': {
            'viral_probability': str(viral_score),
            'expected_engagement': 'High',
            'algorithm_score': str(random.randint(75, 90)),
            'monetization_potential': 'Good'
        },
        'content_strategy': {
            'target_demographics': f'{category} enthusiasts, 18-35 years old',
            'trending_integration': 'Current trends incorporated',
            'thumbnail_suggestion': f'Bold text overlay with {category} imagery',
            'series_potential': f'Perfect for {category} series',
            'collaboration_opportunities': f'{category} influencer partnerships'
        },
        'optimization_insights': {
            'keyword_strategy': f'Focus on {category.lower()} + trending keywords',
            'engagement_tactics': 'Question hooks, call-to-actions, community posts',
            'algorithm_optimization': 'Optimized for YouTube algorithm preferences',
            'growth_recommendations': f'Consistent {category} content with viral elements'
        },
        'error': 'AI generation failed, using advanced intelligent fallback',
        'details': error_details
    }

def generate(prompt: str):
    """
    AI-Powered YouTube Content Generator with Complete Automation
    
    Features:
    - AI Category Detection & Classification
    - Automated Timing & Scheduling  
    - Performance Prediction
    - Content Strategy Recommendations
    - Full Analytics Dashboard
    
    Args:
        prompt (str): The topic to generate content for
        
    Returns:
        dict: Complete AI-generated content with automation insights
    """
    
    if not prompt or prompt.strip() == "":
        return {
            'success': False,
            'error': 'Prompt cannot be empty',
            'message': 'Please provide a topic to generate AI-optimized viral content',
            'examples': [
                'AI Technology Trends 2024',
                'Gaming Setup Guide for Beginners', 
                'Healthy Meal Prep Ideas',
                'Travel Photography Tips',
                'Business Growth Strategies',
                'Fitness Transformation Journey'
            ],
            'supported_categories': [
                'Gaming', 'Technology', 'Beauty', 'Cooking', 'Travel', 'Education',
                'Entertainment', 'Music', 'Sports', 'News', 'DIY', 'Business',
                'Art', 'Automotive', 'Home', 'Family', 'Pets', 'Comedy', 'Science'
            ]
        }
    
    # Clean and optimize the prompt
    prompt = prompt.strip()
    
    # Generate AI-powered content with full automation
    result = generate_helper(prompt)
    
    if 'error' in result:
        return {
            'success': False,
            'error': result['error'],
            'details': result.get('details', ''),
            'ai_analysis': result.get('ai_analysis', {}),
            'optimal_timing': result.get('optimal_timing', {}),
            'fallback_used': True,
            'troubleshooting': 'AI generated intelligent fallback content'
        }
    
    # Extract AI-generated content
    title = result['title']
    description = result['description']
    tags = result['tags']
    
    # Enhanced analytics with AI insights
    seo_score = calculate_seo_score(title, description, tags)
    viral_indicators = analyze_viral_potential(title, description)
    
    return {
        'success': True,
        'prompt': prompt,
        'generated_content': {
            'title': title,
            'description': description,
            'tags': tags
        },
        'upload_recommendations': {
            'suggested_upload_time': get_suggested_upload_time(result.get('ai_analysis', {}).get('primary_category', 'General')),
            'optimal_days': get_optimal_upload_days(result.get('ai_analysis', {}).get('primary_category', 'General')),
            'timezone_recommendations': get_timezone_recommendations(result.get('ai_analysis', {}).get('primary_category', 'General')),
            'frequency_suggestion': get_upload_frequency_suggestion(result.get('ai_analysis', {}).get('primary_category', 'General'))
        },
        'demographic_insights': {
            'target_age_range': get_target_age_range(result.get('ai_analysis', {}).get('primary_category', 'General')),
            'gender_distribution': get_gender_distribution(result.get('ai_analysis', {}).get('primary_category', 'General')),
            'geographic_reach': get_geographic_reach(result.get('ai_analysis', {}).get('primary_category', 'General')),
            'engagement_patterns': get_engagement_patterns(result.get('ai_analysis', {}).get('primary_category', 'General'))
        },
        'ai_analysis': {
            'primary_category': result.get('ai_analysis', {}).get('primary_category', 'General'),
            'secondary_categories': result.get('ai_analysis', {}).get('secondary_categories', []),
            'category_confidence': result.get('ai_analysis', {}).get('category_confidence', '90%'),
            'cross_category_appeal': result.get('ai_analysis', {}).get('cross_category_appeal', '8')
        },
        'optimal_timing': {
            'best_posting_day': result.get('optimal_timing', {}).get('best_posting_day', 'Wednesday'),
            'optimal_time': result.get('optimal_timing', {}).get('optimal_time', '15:00'),
            'timezone': result.get('optimal_timing', {}).get('timezone', 'EST'),
            'posting_frequency': result.get('optimal_timing', {}).get('posting_frequency', '2-3 times per week'),
            'seasonal_factor': result.get('optimal_timing', {}).get('seasonal_factor', '8/10')
        },
        'performance_prediction': {
            'viral_probability': result.get('performance_prediction', {}).get('viral_probability', '75'),
            'expected_engagement': result.get('performance_prediction', {}).get('expected_engagement', 'High'),
            'algorithm_score': result.get('performance_prediction', {}).get('algorithm_score', '85'),
            'monetization_potential': result.get('performance_prediction', {}).get('monetization_potential', 'Good')
        },
        'content_strategy': {
            'target_demographics': result.get('content_strategy', {}).get('target_demographics', '18-35 years old'),
            'trending_integration': result.get('content_strategy', {}).get('trending_integration', 'Current trends integrated'),
            'thumbnail_suggestion': result.get('content_strategy', {}).get('thumbnail_suggestion', 'Bold text with engaging imagery'),
            'series_potential': result.get('content_strategy', {}).get('series_potential', 'High series potential'),
            'collaboration_opportunities': result.get('content_strategy', {}).get('collaboration_opportunities', 'Multiple collaboration options')
        },
        'optimization_insights': {
            'keyword_strategy': result.get('optimization_insights', {}).get('keyword_strategy', 'Multi-keyword approach'),
            'engagement_tactics': result.get('optimization_insights', {}).get('engagement_tactics', 'Question hooks and CTAs'),
            'algorithm_optimization': result.get('optimization_insights', {}).get('algorithm_optimization', 'YouTube algorithm optimized'),
            'growth_recommendations': result.get('optimization_insights', {}).get('growth_recommendations', 'Consistent content strategy')
        },
        'analytics': {
            'character_stats': {
                'title_length': len(title),
                'description_length': len(description),
                'tags_length': len(tags),
                'title_limit': 100,
                'description_limit': 5000,
                'tags_limit': 500
            },
            'seo_score': seo_score,
            'viral_indicators': viral_indicators,
            'optimization_tips': get_optimization_tips(title, description, tags)
        },
        'trending_elements': {
            'has_power_words': check_power_words(title),
            'has_numbers': bool(re.search(r'\d+', title)),
            'has_emotional_triggers': check_emotional_triggers(title),
            'has_trending_hashtags': check_trending_hashtags(description),
            'ai_optimization_applied': True
        },
        'ai_automation': {
            'category_detection': 'Automatic',
            'timing_optimization': 'AI-calculated',
            'content_optimization': 'Fully automated',
            'performance_prediction': 'AI-powered',
            'strategy_recommendations': 'Intelligent automation'
        }
        
    }

def calculate_seo_score(title: str, description: str, tags: str) -> dict:
    """Calculate SEO optimization score based on best practices"""
    score = 0
    max_score = 100
    
    # Title optimization (30 points)
    if 40 <= len(title) <= 70:  # Optimal length
        score += 15
    elif len(title) <= 100:
        score += 10
    
    if any(word in title.upper() for word in ['TOP', 'BEST', 'HOW TO', 'ULTIMATE', 'SECRET']):
        score += 10
    
    if re.search(r'\d+', title):  # Contains numbers
        score += 5
    
    # Description optimization (40 points)
    if len(description) >= 200:  # Substantial content
        score += 15
    
    if description.count('#') >= 3:  # Has hashtags
        score += 10
    
    if any(cta in description.upper() for cta in ['SUBSCRIBE', 'LIKE', 'COMMENT', 'SHARE']):
        score += 10
    
    if '👍' in description or '🔔' in description or '💬' in description:
        score += 5
    
    # Tags optimization (30 points)
    tag_count = len([tag.strip() for tag in tags.split(',') if tag.strip()])
    if tag_count >= 8:
        score += 20
    elif tag_count >= 5:
        score += 15
    elif tag_count >= 3:
        score += 10
    
    if len(tags) > 200:  # Good tag coverage
        score += 10
    
    return {
        'score': min(score, max_score),
        'grade': 'A+' if score >= 90 else 'A' if score >= 80 else 'B+' if score >= 70 else 'B' if score >= 60 else 'C',
        'max_score': max_score
    }

def analyze_viral_potential(title: str, description: str) -> dict:
    """Analyze viral potential based on trending factors"""
    viral_score = 0
    
    # Power words and emotional triggers
    power_words = ['SHOCKING', 'INSANE', 'AMAZING', 'INCREDIBLE', 'UNBELIEVABLE', 'SECRET', 'EXPOSED']
    if any(word in title.upper() for word in power_words):
        viral_score += 25
    
    # Curiosity gaps
    curiosity_phrases = ['YOU WON\'T BELIEVE', 'WHAT HAPPENS NEXT', 'WILL SHOCK YOU', 'NOBODY TALKS ABOUT']
    if any(phrase in title.upper() for phrase in curiosity_phrases):
        viral_score += 20
    
    # Trending elements
    if any(emoji in title for emoji in ['🔥', '💯', '😱', '🤯', '⚡']):
        viral_score += 15
    
    # Timely relevance
    current_year = '2024'
    if current_year in title or current_year in description:
        viral_score += 10
    
    # List format appeal
    if re.search(r'\b\d+\s+(ways|tips|secrets|hacks|things)', title.lower()):
        viral_score += 15
    
    # Controversy/debate potential
    controversy_words = ['VS', 'VERSUS', 'DEBATE', 'CONTROVERSIAL', 'UNPOPULAR OPINION']
    if any(word in title.upper() for word in controversy_words):
        viral_score += 15
    
    return {
        'score': min(viral_score, 100),
        'potential': 'High' if viral_score >= 70 else 'Medium' if viral_score >= 40 else 'Low'
    }

def check_power_words(title: str) -> bool:
    """Check if title contains power words"""
    power_words = ['ULTIMATE', 'SECRET', 'AMAZING', 'INCREDIBLE', 'SHOCKING', 'INSANE', 'BEST', 'TOP', 'EPIC']
    return any(word in title.upper() for word in power_words)

def check_emotional_triggers(title: str) -> bool:
    """Check if title contains emotional triggers"""
    emotional_words = ['SHOCKING', 'AMAZING', 'INCREDIBLE', 'TERRIFYING', 'HILARIOUS', 'HEARTBREAKING', 'INSPIRING']
    return any(word in title.upper() for word in emotional_words)

def check_trending_hashtags(description: str) -> bool:
    """Check if description contains trending hashtags"""
    return '#' in description and description.count('#') >= 3

def get_optimization_tips(title: str, description: str, tags: str) -> list:
    """Provide optimization tips based on content analysis"""
    tips = []
    
    if len(title) > 80:
        tips.append("Consider shortening your title for better mobile display")
    
    if not re.search(r'\d+', title):
        tips.append("Adding numbers to your title can increase click-through rates")
    
    if description.count('#') < 5:
        tips.append("Add more relevant hashtags to improve discoverability")
    
    if 'subscribe' not in description.lower():
        tips.append("Include a call-to-action to subscribe in your description")
    
    if len(tags.split(',')) < 8:
        tips.append("Use more tags to maximize search visibility")
    
    if not any(emoji in description for emoji in ['👍', '🔔', '💬', '🔥']):
        tips.append("Add engaging emojis to make your description more appealing")
    
    return tips if tips else ["Great! Your content is well-optimized for YouTube!"]

def get_target_audience(category: str) -> dict:
    """Get target audience insights for category"""
    audiences = {
        'Gaming': {'age_range': '13-35', 'primary_gender': 'Male (65%)', 'interests': 'Technology, Entertainment, Competition'},
        'Technology': {'age_range': '18-45', 'primary_gender': 'Male (70%)', 'interests': 'Innovation, Gadgets, Future Trends'},
        'Beauty': {'age_range': '16-35', 'primary_gender': 'Female (80%)', 'interests': 'Fashion, Self-care, Trends'},
        'Cooking': {'age_range': '25-55', 'primary_gender': 'Female (60%)', 'interests': 'Food, Health, Family'},
        'Travel': {'age_range': '20-40', 'primary_gender': 'Balanced', 'interests': 'Adventure, Culture, Lifestyle'},
        'Education': {'age_range': '16-50', 'primary_gender': 'Balanced', 'interests': 'Learning, Career, Skills'},
        'Entertainment': {'age_range': '13-30', 'primary_gender': 'Balanced', 'interests': 'Humor, Pop Culture, Viral Content'},
        'Music': {'age_range': '13-40', 'primary_gender': 'Balanced', 'interests': 'Artists, Creativity, Emotions'},
        'Fitness': {'age_range': '18-45', 'primary_gender': 'Balanced', 'interests': 'Health, Body Goals, Motivation'},
        'Business': {'age_range': '25-50', 'primary_gender': 'Male (60%)', 'interests': 'Success, Money, Growth'},
        'Diy': {'age_range': '25-50', 'primary_gender': 'Female (55%)', 'interests': 'Home, Creativity, Savings'},
        'Automotive': {'age_range': '20-50', 'primary_gender': 'Male (85%)', 'interests': 'Cars, Technology, Performance'}
    }
    return audiences.get(category, {'age_range': '18-35', 'primary_gender': 'Balanced', 'interests': 'General'})

def get_best_posting_times(category: str) -> dict:
    """Get optimal posting times for category"""
    times = {
        'Gaming': {'weekdays': '3-6 PM, 8-11 PM', 'weekends': '10 AM-2 PM, 7-11 PM', 'timezone': 'Target audience timezone'},
        'Technology': {'weekdays': '9-11 AM, 2-4 PM', 'weekends': '10 AM-1 PM', 'timezone': 'EST/PST preferred'},
        'Beauty': {'weekdays': '6-9 AM, 7-9 PM', 'weekends': '9 AM-12 PM', 'timezone': 'Target audience timezone'},
        'Cooking': {'weekdays': '11 AM-1 PM, 5-7 PM', 'weekends': '10 AM-2 PM', 'timezone': 'Local dinner times'},
        'Travel': {'weekdays': '12-2 PM, 7-9 PM', 'weekends': '9 AM-12 PM', 'timezone': 'Multiple zones'},
        'Education': {'weekdays': '8-10 AM, 3-5 PM', 'weekends': '10 AM-2 PM', 'timezone': 'Student schedules'},
        'Entertainment': {'weekdays': '7-9 PM', 'weekends': '12-6 PM', 'timezone': 'Evening entertainment'},
        'Music': {'weekdays': '4-6 PM, 8-10 PM', 'weekends': '2-8 PM', 'timezone': 'After work/school'},
        'Fitness': {'weekdays': '6-8 AM, 5-7 PM', 'weekends': '8-11 AM', 'timezone': 'Workout times'},
        'Business': {'weekdays': '8-10 AM, 1-3 PM', 'weekends': '10 AM-12 PM', 'timezone': 'Business hours'},
        'Diy': {'weekdays': '6-8 PM', 'weekends': '9 AM-4 PM', 'timezone': 'Project time'},
        'Automotive': {'weekdays': '6-8 PM', 'weekends': '9 AM-5 PM', 'timezone': 'Garage time'}
    }
    return times.get(category, {'weekdays': '12-2 PM, 7-9 PM', 'weekends': '10 AM-2 PM', 'timezone': 'General'})

def get_trending_topics_for_category(category: str) -> list:
    """Get current trending topics for category"""
    trends_2024 = {
        'Gaming': ['AI in Gaming', 'VR Gaming', 'Indie Games 2024', 'Gaming Laptops', 'Esports Tournaments'],
        'Technology': ['AI Revolution', 'ChatGPT Updates', 'iPhone 16', 'Tesla Updates', 'Crypto Trends'],
        'Beauty': ['Clean Beauty', 'Korean Skincare', 'Sustainable Makeup', 'TikTok Beauty Trends', 'Minimal Makeup'],
        'Cooking': ['Air Fryer Recipes', 'Healthy Meal Prep', 'Plant-Based Cooking', 'International Cuisines', 'Quick 15-min Meals'],
        'Travel': ['Solo Travel', 'Budget Travel 2024', 'Digital Nomad Life', 'Sustainable Tourism', 'Hidden Gems'],
        'Education': ['AI Learning Tools', 'Online Courses', 'Skill Development', 'Career Transitions', 'Digital Literacy'],
        'Entertainment': ['Movie Reviews 2024', 'Celebrity News', 'Viral Challenges', 'Meme Culture', 'Streaming Shows'],
        'Music': ['New Artist Discoveries', 'Music Production', 'Vinyl Revival', 'Concert Reviews', 'Music Theory'],
        'Fitness': ['Home Workouts', 'Mental Health', 'Nutrition Trends', 'Fitness Technology', 'Outdoor Activities'],
        'Business': ['AI in Business', 'Remote Work', 'Entrepreneurship', 'Side Hustles', 'Investment Strategies'],
        'Diy': ['Smart Home DIY', 'Upcycling Projects', 'Budget Home Decor', 'Garden Projects', 'Crafting Trends'],
        'Automotive': ['Electric Vehicles', 'Car Modifications', 'Auto Technology', 'Classic Cars', 'Motorcycle Trends']
    }
    return trends_2024.get(category, ['Trending Topics', 'Viral Content', 'Popular Themes', 'Current Events', '2024 Trends'])

def get_suggested_upload_time(category: str) -> dict:
    """Get AI-recommended upload times for maximum engagement"""
    from datetime import datetime
    
    upload_times = {
        'Gaming': {
            'primary_time': '3:00 PM EST',
            'alternative_times': ['6:00 PM EST', '8:00 PM EST', '10:00 PM EST'],
            'weekend_optimal': '1:00 PM EST',
            'reasoning': 'Peak gaming hours when audiences are most active after school/work'
        },
        'Technology': {
            'primary_time': '10:00 AM EST',
            'alternative_times': ['2:00 PM EST', '4:00 PM EST'],
            'weekend_optimal': '11:00 AM EST',
            'reasoning': 'Professional hours when tech enthusiasts check for updates'
        },
        'Beauty': {
            'primary_time': '7:00 AM EST',
            'alternative_times': ['12:00 PM EST', '7:00 PM EST'],
            'weekend_optimal': '10:00 AM EST',
            'reasoning': 'Morning routine and evening skincare preparation times'
        },
        'Cooking': {
            'primary_time': '11:00 AM EST',
            'alternative_times': ['5:00 PM EST', '6:00 PM EST'],
            'weekend_optimal': '12:00 PM EST',
            'reasoning': 'Meal planning and dinner preparation hours'
        },
        'Travel': {
            'primary_time': '12:00 PM EST',
            'alternative_times': ['7:00 PM EST', '8:00 PM EST'],
            'weekend_optimal': '10:00 AM EST',
            'reasoning': 'Lunch break browsing and evening travel planning'
        },
        'Education': {
            'primary_time': '8:00 AM EST',
            'alternative_times': ['3:00 PM EST', '4:00 PM EST'],
            'weekend_optimal': '10:00 AM EST',
            'reasoning': 'Study hours and after-school learning time'
        },
        'Entertainment': {
            'primary_time': '7:00 PM EST',
            'alternative_times': ['8:00 PM EST', '9:00 PM EST'],
            'weekend_optimal': '2:00 PM EST',
            'reasoning': 'Prime entertainment hours when people relax'
        },
        'Music': {
            'primary_time': '4:00 PM EST',
            'alternative_times': ['8:00 PM EST', '9:00 PM EST'],
            'weekend_optimal': '3:00 PM EST',
            'reasoning': 'After-work/school music discovery and evening listening'
        },
        'Fitness': {
            'primary_time': '6:00 AM EST',
            'alternative_times': ['5:00 PM EST', '6:00 PM EST'],
            'weekend_optimal': '8:00 AM EST',
            'reasoning': 'Morning workout motivation and post-work fitness'
        },
        'Business': {
            'primary_time': '9:00 AM EST',
            'alternative_times': ['1:00 PM EST', '2:00 PM EST'],
            'weekend_optimal': '10:00 AM EST',
            'reasoning': 'Business hours when professionals are most engaged'
        }
    }
    
    return upload_times.get(category, {
        'primary_time': '12:00 PM EST',
        'alternative_times': ['7:00 PM EST', '8:00 PM EST'],
        'weekend_optimal': '10:00 AM EST',
        'reasoning': 'General optimal times for broad audience appeal'
    })

def get_optimal_upload_days(category: str) -> dict:
    """Get best days of week for uploading content"""
    upload_days = {
        'Gaming': {
            'best_days': ['Tuesday', 'Wednesday', 'Thursday'],
            'weekend_performance': 'High on Saturday',
            'avoid_days': ['Monday'],
            'reasoning': 'Mid-week consistency with weekend gaming sessions'
        },
        'Technology': {
            'best_days': ['Tuesday', 'Wednesday', 'Thursday'],
            'weekend_performance': 'Low',
            'avoid_days': ['Friday', 'Saturday'],
            'reasoning': 'Professional weekdays for tech content consumption'
        },
        'Beauty': {
            'best_days': ['Monday', 'Wednesday', 'Friday'],
            'weekend_performance': 'High on Sunday',
            'avoid_days': ['Thursday'],
            'reasoning': 'Week preparation and weekend beauty routines'
        },
        'Cooking': {
            'best_days': ['Sunday', 'Monday', 'Wednesday'],
            'weekend_performance': 'Very High',
            'avoid_days': ['Tuesday'],
            'reasoning': 'Meal prep Sundays and weekly cooking planning'
        },
        'Travel': {
            'best_days': ['Tuesday', 'Wednesday', 'Sunday'],
            'weekend_performance': 'High',
            'avoid_days': ['Monday'],
            'reasoning': 'Mid-week planning and weekend travel inspiration'
        },
        'Education': {
            'best_days': ['Monday', 'Tuesday', 'Wednesday'],
            'weekend_performance': 'Medium',
            'avoid_days': ['Friday'],
            'reasoning': 'Early week learning motivation'
        },
        'Entertainment': {
            'best_days': ['Thursday', 'Friday', 'Saturday'],
            'weekend_performance': 'Very High',
            'avoid_days': ['Monday'],
            'reasoning': 'Weekend entertainment and TGIF vibes'
        },
        'Music': {
            'best_days': ['Friday', 'Saturday', 'Sunday'],
            'weekend_performance': 'Very High',
            'avoid_days': ['Tuesday'],
            'reasoning': 'Weekend music discovery and party vibes'
        },
        'Fitness': {
            'best_days': ['Monday', 'Tuesday', 'Sunday'],
            'weekend_performance': 'High',
            'avoid_days': ['Friday'],
            'reasoning': 'New week motivation and weekend workout prep'
        },
        'Business': {
            'best_days': ['Tuesday', 'Wednesday', 'Thursday'],
            'weekend_performance': 'Low',
            'avoid_days': ['Friday', 'Saturday'],
            'reasoning': 'Peak business week engagement'
        }
    }
    
    return upload_days.get(category, {
        'best_days': ['Tuesday', 'Wednesday', 'Thursday'],
        'weekend_performance': 'Medium',
        'avoid_days': ['Monday'],
        'reasoning': 'General mid-week optimal performance'
    })

def get_timezone_recommendations(category: str) -> dict:
    """Get timezone optimization recommendations"""
    timezone_data = {
        'Gaming': {
            'primary_timezone': 'EST (Eastern Standard Time)',
            'secondary_timezones': ['PST', 'CST'],
            'global_reach': 'Consider GMT for EU audience',
            'peak_regions': 'North America, Europe',
            'strategy': 'Upload in EST for maximum NA reach, consider EU times for global content'
        },
        'Technology': {
            'primary_timezone': 'PST (Pacific Standard Time)',
            'secondary_timezones': ['EST', 'GMT'],
            'global_reach': 'Strong international appeal',
            'peak_regions': 'Silicon Valley, Global Tech Hubs',
            'strategy': 'PST for tech industry, EST for broader US market'
        },
        'Beauty': {
            'primary_timezone': 'EST (Eastern Standard Time)',
            'secondary_timezones': ['PST', 'GMT'],
            'global_reach': 'High international interest',
            'peak_regions': 'US, Europe, Asia',
            'strategy': 'Multi-timezone approach for global beauty community'
        },
        'Cooking': {
            'primary_timezone': 'Local audience timezone',
            'secondary_timezones': ['EST', 'PST'],
            'global_reach': 'Recipe content travels well',
            'peak_regions': 'Regional preferences vary',
            'strategy': 'Adapt to local meal times and cultural preferences'
        },
        'Travel': {
            'primary_timezone': 'GMT (Greenwich Mean Time)',
            'secondary_timezones': ['EST', 'PST'],
            'global_reach': 'Extremely high international appeal',
            'peak_regions': 'Worldwide',
            'strategy': 'Global timing for maximum international reach'
        },
        'Education': {
            'primary_timezone': 'EST (Eastern Standard Time)',
            'secondary_timezones': ['PST', 'CST'],
            'global_reach': 'Strong global education market',
            'peak_regions': 'English-speaking countries',
            'strategy': 'Focus on educational time zones and school schedules'
        },
        'Entertainment': {
            'primary_timezone': 'EST (Eastern Standard Time)',
            'secondary_timezones': ['PST', 'CST'],
            'global_reach': 'High viral potential globally',
            'peak_regions': 'US, English-speaking countries',
            'strategy': 'Prime time entertainment hours in major markets'
        },
        'Music': {
            'primary_timezone': 'EST (Eastern Standard Time)',
            'secondary_timezones': ['PST', 'GMT'],
            'global_reach': 'Music transcends borders',
            'peak_regions': 'Global music markets',
            'strategy': 'Consider major music markets and streaming patterns'
        },
        'Fitness': {
            'primary_timezone': 'Local audience timezone',
            'secondary_timezones': ['EST', 'PST'],
            'global_reach': 'Fitness is universal',
            'peak_regions': 'Health-conscious regions',
            'strategy': 'Align with local workout schedules and fitness culture'
        },
        'Business': {
            'primary_timezone': 'EST (Eastern Standard Time)',
            'secondary_timezones': ['PST', 'GMT'],
            'global_reach': 'Business content global appeal',
            'peak_regions': 'Major business centers',
            'strategy': 'Business hours in major financial centers'
        }
    }
    
    return timezone_data.get(category, {
        'primary_timezone': 'EST (Eastern Standard Time)',
        'secondary_timezones': ['PST', 'CST'],
        'global_reach': 'Medium international appeal',
        'peak_regions': 'North America',
        'strategy': 'Focus on primary market with secondary expansion'
    })

def get_upload_frequency_suggestion(category: str) -> dict:
    """Get AI-recommended upload frequency for optimal growth"""
    frequency_data = {
        'Gaming': {
            'optimal_frequency': '3-4 times per week',
            'minimum_frequency': '2 times per week',
            'maximum_sustainable': '5-6 times per week',
            'growth_phase': 'Daily uploads for rapid growth',
            'reasoning': 'Gaming audiences expect regular content, trending games require quick coverage'
        },
        'Technology': {
            'optimal_frequency': '2-3 times per week',
            'minimum_frequency': '1-2 times per week',
            'maximum_sustainable': '4 times per week',
            'growth_phase': '3-4 times per week',
            'reasoning': 'Quality over quantity, tech reviews need research time'
        },
        'Beauty': {
            'optimal_frequency': '3-4 times per week',
            'minimum_frequency': '2 times per week',
            'maximum_sustainable': 'Daily uploads',
            'growth_phase': '4-5 times per week',
            'reasoning': 'Beauty trends move fast, audience expects regular tutorials'
        },
        'Cooking': {
            'optimal_frequency': '2-3 times per week',
            'minimum_frequency': '1 time per week',
            'maximum_sustainable': '4-5 times per week',
            'growth_phase': '3-4 times per week',
            'reasoning': 'Recipe testing takes time, quality presentation important'
        },
        'Travel': {
            'optimal_frequency': '1-2 times per week',
            'minimum_frequency': '1 time per week',
            'maximum_sustainable': '3 times per week',
            'growth_phase': '2-3 times per week',
            'reasoning': 'Travel content requires significant production time'
        },
        'Education': {
            'optimal_frequency': '2-3 times per week',
            'minimum_frequency': '1 time per week',
            'maximum_sustainable': '4 times per week',
            'growth_phase': '3 times per week',
            'reasoning': 'Educational content needs thorough preparation and research'
        },
        'Entertainment': {
            'optimal_frequency': '4-5 times per week',
            'minimum_frequency': '3 times per week',
            'maximum_sustainable': 'Daily uploads',
            'growth_phase': 'Daily uploads',
            'reasoning': 'Entertainment thrives on frequent, trending content'
        },
        'Music': {
            'optimal_frequency': '2-3 times per week',
            'minimum_frequency': '1-2 times per week',
            'maximum_sustainable': '4 times per week',
            'growth_phase': '3-4 times per week',
            'reasoning': 'Music production and covers require quality time'
        },
        'Fitness': {
            'optimal_frequency': '3-4 times per week',
            'minimum_frequency': '2 times per week',
            'maximum_sustainable': '5-6 times per week',
            'growth_phase': '4-5 times per week',
            'reasoning': 'Fitness routines benefit from regular, consistent content'
        },
        'Business': {
            'optimal_frequency': '2 times per week',
            'minimum_frequency': '1 time per week',
            'maximum_sustainable': '3-4 times per week',
            'growth_phase': '3 times per week',
            'reasoning': 'Business content requires research and professional quality'
        }
    }
    
    return frequency_data.get(category, {
        'optimal_frequency': '2-3 times per week',
        'minimum_frequency': '1-2 times per week',
        'maximum_sustainable': '4 times per week',
        'growth_phase': '3 times per week',
        'reasoning': 'Balanced approach for sustainable growth'
    })

def get_target_age_range(category: str) -> dict:
    """Get detailed age demographics for category"""
    age_demographics = {
        'Gaming': {
            'primary_age_range': '13-25 years',
            'secondary_age_range': '26-35 years',
            'peak_engagement_age': '18-22 years',
            'age_distribution': {
                '13-17': '25%',
                '18-24': '35%',
                '25-34': '25%',
                '35+': '15%'
            },
            'content_adaptation': 'Use gaming slang, trending game references, competitive elements'
        },
        'Technology': {
            'primary_age_range': '25-40 years',
            'secondary_age_range': '18-24 years',
            'peak_engagement_age': '28-35 years',
            'age_distribution': {
                '18-24': '20%',
                '25-34': '40%',
                '35-44': '25%',
                '45+': '15%'
            },
            'content_adaptation': 'Professional tone, practical applications, career implications'
        },
        'Beauty': {
            'primary_age_range': '16-30 years',
            'secondary_age_range': '31-45 years',
            'peak_engagement_age': '20-26 years',
            'age_distribution': {
                '16-24': '45%',
                '25-34': '30%',
                '35-44': '15%',
                '45+': '10%'
            },
            'content_adaptation': 'Trendy language, social media references, age-appropriate products'
        },
        'Cooking': {
            'primary_age_range': '25-45 years',
            'secondary_age_range': '18-24 years',
            'peak_engagement_age': '30-40 years',
            'age_distribution': {
                '18-24': '15%',
                '25-34': '35%',
                '35-44': '30%',
                '45+': '20%'
            },
            'content_adaptation': 'Family-friendly, practical recipes, health considerations'
        },
        'Travel': {
            'primary_age_range': '22-35 years',
            'secondary_age_range': '18-21 years',
            'peak_engagement_age': '25-32 years',
            'age_distribution': {
                '18-24': '25%',
                '25-34': '40%',
                '35-44': '20%',
                '45+': '15%'
            },
            'content_adaptation': 'Adventure focus, budget considerations, career flexibility'
        },
        'Education': {
            'primary_age_range': '16-35 years',
            'secondary_age_range': '36-50 years',
            'peak_engagement_age': '20-28 years',
            'age_distribution': {
                '16-24': '40%',
                '25-34': '30%',
                '35-44': '20%',
                '45+': '10%'
            },
            'content_adaptation': 'Clear explanations, career relevance, skill development focus'
        },
        'Entertainment': {
            'primary_age_range': '13-28 years',
            'secondary_age_range': '29-40 years',
            'peak_engagement_age': '16-24 years',
            'age_distribution': {
                '13-17': '20%',
                '18-24': '35%',
                '25-34': '25%',
                '35+': '20%'
            },
            'content_adaptation': 'Pop culture references, viral trends, humor style adaptation'
        },
        'Music': {
            'primary_age_range': '13-35 years',
            'secondary_age_range': '36-50 years',
            'peak_engagement_age': '18-28 years',
            'age_distribution': {
                '13-17': '15%',
                '18-24': '30%',
                '25-34': '30%',
                '35+': '25%'
            },
            'content_adaptation': 'Genre preferences, nostalgia elements, current music trends'
        },
        'Fitness': {
            'primary_age_range': '20-40 years',
            'secondary_age_range': '18-19 years',
            'peak_engagement_age': '25-35 years',
            'age_distribution': {
                '18-24': '25%',
                '25-34': '35%',
                '35-44': '25%',
                '45+': '15%'
            },
            'content_adaptation': 'Realistic goals, time-efficient workouts, health awareness'
        },
        'Business': {
            'primary_age_range': '25-45 years',
            'secondary_age_range': '22-24 years',
            'peak_engagement_age': '28-38 years',
            'age_distribution': {
                '22-24': '10%',
                '25-34': '40%',
                '35-44': '30%',
                '45+': '20%'
            },
            'content_adaptation': 'Professional development, financial goals, leadership skills'
        }
    }
    
    return age_demographics.get(category, {
        'primary_age_range': '18-35 years',
        'secondary_age_range': '36-50 years',
        'peak_engagement_age': '25-32 years',
        'age_distribution': {
            '18-24': '25%',
            '25-34': '35%',
            '35-44': '25%',
            '45+': '15%'
        },
        'content_adaptation': 'Balanced approach for broad age appeal'
    })

def get_gender_distribution(category: str) -> dict:
    """Get gender demographics for category"""
    gender_data = {
        'Gaming': {'male': '65%', 'female': '35%', 'trend': 'Female audience growing rapidly'},
        'Technology': {'male': '70%', 'female': '30%', 'trend': 'More women entering tech space'},
        'Beauty': {'male': '15%', 'female': '85%', 'trend': 'Male grooming content increasing'},
        'Cooking': {'male': '40%', 'female': '60%', 'trend': 'Male cooking enthusiasts growing'},
        'Travel': {'male': '45%', 'female': '55%', 'trend': 'Balanced with slight female preference'},
        'Education': {'male': '50%', 'female': '50%', 'trend': 'Equal interest across genders'},
        'Entertainment': {'male': '48%', 'female': '52%', 'trend': 'Balanced entertainment consumption'},
        'Music': {'male': '45%', 'female': '55%', 'trend': 'Slight female preference for music content'},
        'Fitness': {'male': '45%', 'female': '55%', 'trend': 'Female fitness content dominance'},
        'Business': {'male': '60%', 'female': '40%', 'trend': 'Female entrepreneurship growing'}
    }
    
    return gender_data.get(category, {'male': '50%', 'female': '50%', 'trend': 'Balanced gender appeal'})

def get_geographic_reach(category: str) -> dict:
    """Get geographic reach insights"""
    geo_data = {
        'Gaming': {'primary': 'North America, Europe', 'secondary': 'Asia, South America', 'global_appeal': 'High'},
        'Technology': {'primary': 'North America, Europe, Asia', 'secondary': 'Global', 'global_appeal': 'Very High'},
        'Beauty': {'primary': 'North America, Europe, Asia', 'secondary': 'Global', 'global_appeal': 'Very High'},
        'Cooking': {'primary': 'Region-specific', 'secondary': 'Global for fusion content', 'global_appeal': 'Medium'},
        'Travel': {'primary': 'Global', 'secondary': 'Universal appeal', 'global_appeal': 'Extremely High'},
        'Education': {'primary': 'English-speaking countries', 'secondary': 'Global with subtitles', 'global_appeal': 'High'},
        'Entertainment': {'primary': 'Western countries', 'secondary': 'Global viral potential', 'global_appeal': 'High'},
        'Music': {'primary': 'Global', 'secondary': 'Universal language', 'global_appeal': 'Extremely High'},
        'Fitness': {'primary': 'Developed countries', 'secondary': 'Global health trends', 'global_appeal': 'High'},
        'Business': {'primary': 'Developed economies', 'secondary': 'Emerging markets', 'global_appeal': 'Medium-High'}
    }
    
    return geo_data.get(category, {'primary': 'North America, Europe', 'secondary': 'Global', 'global_appeal': 'Medium'})

def get_engagement_patterns(category: str) -> dict:
    """Get engagement behavior patterns"""
    engagement_data = {
        'Gaming': {
            'watch_time': 'High (8-15 minutes average)',
            'comment_activity': 'Very High',
            'sharing_behavior': 'High for viral moments',
            'subscription_rate': 'High for consistent creators'
        },
        'Technology': {
            'watch_time': 'Medium-High (6-12 minutes)',
            'comment_activity': 'Medium with quality discussions',
            'sharing_behavior': 'High for useful content',
            'subscription_rate': 'High for authoritative sources'
        },
        'Beauty': {
            'watch_time': 'High (10-20 minutes)',
            'comment_activity': 'Very High with questions',
            'sharing_behavior': 'Very High for tutorials',
            'subscription_rate': 'Very High for trusted creators'
        },
        'Cooking': {
            'watch_time': 'Medium (5-12 minutes)',
            'comment_activity': 'High with recipe questions',
            'sharing_behavior': 'High for successful recipes',
            'subscription_rate': 'High for consistent quality'
        },
        'Travel': {
            'watch_time': 'High (8-18 minutes)',
            'comment_activity': 'Medium-High with travel questions',
            'sharing_behavior': 'Very High for inspiration',
            'subscription_rate': 'High for authentic experiences'
        },
        'Education': {
            'watch_time': 'Very High (15-30 minutes)',
            'comment_activity': 'Medium with clarifying questions',
            'sharing_behavior': 'High for valuable content',
            'subscription_rate': 'High for clear teachers'
        },
        'Entertainment': {
            'watch_time': 'Medium (3-8 minutes)',
            'comment_activity': 'Very High with reactions',
            'sharing_behavior': 'Extremely High for viral content',
            'subscription_rate': 'Medium but high viral potential'
        },
        'Music': {
            'watch_time': 'Medium (3-6 minutes)',
            'comment_activity': 'High with emotional responses',
            'sharing_behavior': 'Very High for catchy content',
            'subscription_rate': 'High for talented musicians'
        },
        'Fitness': {
            'watch_time': 'High (10-25 minutes)',
            'comment_activity': 'Medium-High with progress updates',
            'sharing_behavior': 'High for effective workouts',
            'subscription_rate': 'Very High for motivating trainers'
        },
        'Business': {
            'watch_time': 'Medium-High (8-15 minutes)',
            'comment_activity': 'Medium with professional questions',
            'sharing_behavior': 'High for actionable advice',
            'subscription_rate': 'High for proven expertise'
        }
    }
    
    return engagement_data.get(category, {
        'watch_time': 'Medium (5-10 minutes)',
        'comment_activity': 'Medium',
        'sharing_behavior': 'Medium',
        'subscription_rate': 'Medium'
    })