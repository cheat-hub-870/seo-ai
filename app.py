import os
import sys
import time
import json
from datetime import datetime, timedelta
from flask import Flask, request, jsonify


def check_and_install_generativeai():
    """Check if google-generativeai is installed, and install it if needed."""
    try:
        import google.generativeai as genai
        return genai
    except ImportError:
        print("google-generativeai not found. Installing...")
        import subprocess
        subprocess.check_call([sys.executable, "-m", "pip", "install", "google-generativeai"])
        
        # After installation, import again
        import google.generativeai as genai
        return genai


def calculate_eta(start_time, current_progress, total_items):
    """
    Calculate estimated time of arrival (ETA) for a process
    
    Args:
        start_time: When the process started (timestamp)
        current_progress: Number of items processed so far
        total_items: Total number of items to process
    
    Returns:
        Estimated time of completion (datetime object)
    """
    if current_progress == 0:
        return None
    
    elapsed_time = time.time() - start_time
    time_per_item = elapsed_time / current_progress
    remaining_items = total_items - current_progress
    eta_seconds = time_per_item * remaining_items
    
    return datetime.now() + timedelta(seconds=eta_seconds)


# Initialize Flask app
app = Flask(__name__)

# Load configuration
config_path = os.path.join(os.path.dirname(__file__), 'config.json')
with open(config_path) as f:
    config = json.load(f)

KEY = config['API_KEY']
OWNER = config['owner']
INSTAGRAM = config['instagram']
DISCORD = config['discord']

# Configure Gemini AI
genai = check_and_install_generativeai()
genai.configure(api_key=KEY)

# Get available models to use the best one
available_models = []
try:
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            available_models.append(model.name.replace('models/',))
except Exception as e:
    print(f"Could not list models: {e}")
    # Fallback models that are commonly available
    available_models = ['gemini-2.5-flash', 'gemini-2.5-pro', 'gemini-2.0-flash', 'gemini-pro-latest']

# Determine which models are available - prioritize newer models first
content_model_options = ['gemini-2.5-flash', 'gemini-2.5-pro', 'gemini-2.0-flash', 'gemini-pro-latest', 'gemini-flash-latest']
kgr_model_options = ['gemini-2.5-flash', 'gemini-2.5-pro', 'gemini-2.0-flash', 'gemini-pro-latest', 'gemini-flash-latest']

# Select the first available model from our preferred options
DEFAULT_CONTENT_MODEL = None
for model in content_model_options:
    if model in available_models:
        DEFAULT_CONTENT_MODEL = model
        break

# If no preferred model is found, use the first available one
if DEFAULT_CONTENT_MODEL is None:
    DEFAULT_CONTENT_MODEL = available_models[0] if available_models else 'gemini-2.5-flash'

DEFAULT_KGR_MODEL = None
for model in kgr_model_options:
    if model in available_models:
        DEFAULT_KGR_MODEL = model
        break

# If no preferred model is found, use the first available one
if DEFAULT_KGR_MODEL is None:
    DEFAULT_KGR_MODEL = available_models[0] if available_models else 'gemini-2.5-flash'

print(f"Available models: {available_models}")
print(f"Using content model: {DEFAULT_CONTENT_MODEL}")
print(f"Using KGR model: {DEFAULT_KGR_MODEL}")

# Import the modules that contain the core functionality
import get_content
import extract_tags
import kgr

# Update the modules with the appropriate models
get_content.MODEL_NAME = DEFAULT_CONTENT_MODEL
kgr.MODEL_NAME = DEFAULT_KGR_MODEL


@app.route('/')
def home():
    """Home endpoint with API information"""
    return jsonify({
        "message": "SEO AI Backend API",
        "endpoints": {
            "/content": "Generate YouTube content (title, description, tags)",
            "/tags": "Extract tags from a YouTube video URL", 
            "/kgr": "Calculate YouTube Keyword Golden Ratio"
        },
        "developer": OWNER,
        "contact": {
            "instagram": INSTAGRAM,
            "discord": DISCORD
        },
        "available_models": available_models,
        "active_models": {
            "content_model": DEFAULT_CONTENT_MODEL,
            "kgr_model": DEFAULT_KGR_MODEL
        }
    })


@app.route('/content', methods=['GET', 'POST'])
def generate_content():
    """Generate YouTube content (title, description, tags) based on a prompt"""
    try:
        # Support both GET (query parameters) and POST (JSON body)
        if request.method == 'GET':
            prompt = request.args.get('prompt')
        else:  # POST request
            data = request.get_json()
            prompt = data.get('prompt') if data else None
        
        if not prompt:
            return jsonify({
                'success': False,
                'error': 'Prompt is required as query parameter (GET) or in request body (POST)',
                'message': 'Please provide a prompt to generate content'
            }), 400
        
        # Generate content using the imported module
        result = get_content.generate(prompt)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Error generating content'
        }), 500


@app.route('/tags', methods=['GET', 'POST'])
def extract_video_tags():
    """Extract tags from a YouTube video URL"""
    try:
        # Support both GET (query parameters) and POST (JSON body)
        if request.method == 'GET':
            video_url = request.args.get('video_url')
        else:  # POST request
            data = request.get_json()
            video_url = data.get('video_url') if data else None
        
        if not video_url:
            return jsonify({
                'success': False,
                'error': 'Video URL is required as query parameter (GET) or in request body (POST)',
                'message': 'Please provide a YouTube video URL to extract tags'
            }), 400
        
        # Extract tags using the imported module
        result = extract_tags.extract_youtube_tags(video_url)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Error extracting tags'
        }), 500


@app.route('/kgr', methods=['GET', 'POST'])
def calculate_kgr():
    """Calculate YouTube Keyword Golden Ratio for a keyword"""
    try:
        # Support both GET (query parameters) and POST (JSON body)
        if request.method == 'GET':
            keyword = request.args.get('keyword')
        else:  # POST request
            data = request.get_json()
            keyword = data.get('keyword') if data else None
        
        if not keyword:
            return jsonify({
                'success': False,
                'error': 'Keyword is required as query parameter (GET) or in request body (POST)',
                'message': 'Please provide a keyword to calculate KGR'
            }), 400
        
        # Calculate KGR using the imported module
        result = kgr.KGR(keyword)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e),
            'message': 'Error calculating KGR'
        }), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)