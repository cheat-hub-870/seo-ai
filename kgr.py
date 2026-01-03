import google.generativeai as genai
import re
import os
import json

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

def fetch_youtube_data(keyword):
    """
    Use Gemini to get rough YouTube results count and search volume.
    """
    model = genai.GenerativeModel(MODEL_NAME)  # Use the model set by app.py or default
    
    prompt = f"""
    Estimate the number of YouTube videos and the monthly search volume
    for the keyword: "{keyword}".
    Return as: results=<number>, search_volume=<number>
    """
    
    try:
        response = model.generate_content(prompt)
        response_text = response.text
        
        # Parse Gemini's response
        try:
            parts = response_text.split(",")
            results = int(parts[0].split("=")[1].strip())
            search_volume = int(parts[1].split("=")[1].strip())
        except:
            results = 0
            search_volume = 0
        
        return results, search_volume
    except Exception as e:
        print(f"Error in fetch_youtube_data: {str(e)}")
        return 0, 0

def KGR(keyword):
    """
    Calculate YouTube Keyword Golden Ratio (KGR) for a single keyword using Gemini estimates.
    Args:
        keyword (str): The keyword string
    Returns:
        dict: Structured result with success status and KGR value for the keyword
    """
    yt_results, yt_search_volume = fetch_youtube_data(keyword)
    if yt_search_volume == 0:
        kgr_value = None
    else:
        kgr_value = yt_results / yt_search_volume
    return {
        'success': True,
        'keyword': keyword,
        'youtube_results': yt_results,
        'youtube_search_volume': yt_search_volume,
        'youtube_kgr': kgr_value
    }