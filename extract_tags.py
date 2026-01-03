import requests
from bs4 import BeautifulSoup
import re

def extract_youtube_tags(video_url):
    """
    Extract tags from a YouTube video using web scraping.
    
    Args:
        video_url (str): The URL of the YouTube video
        
    Returns:
        dict: Dictionary containing success status and tags/message
    """
    # Extract video ID from URL
    video_id = None
    patterns = [
        r'(?:youtube\.com/\S*[?&]v=|youtu\.be/)([^&\n?#]*)',
        r'youtube\.com/shorts/([^?&#]*)',
        r'youtube\.com/embed/([^?&#]*)'
    ]
    
    for pattern in patterns:
        match = re.search(pattern, video_url)
        if match:
            video_id = match.group(1)
            break
    
    if not video_id:
        return {'success': False, 'message': 'Invalid YouTube URL'}
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(f'https://www.youtube.com/watch?v={video_id}', headers=headers)
        if response.status_code != 200:
            return {'success': False, 'message': f'Failed to fetch video page: {response.status_code}'}
        
        # Look for tags in the page content
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Try to find tags in the JSON-LD data
        script_tags = soup.find_all('script')
        for script in script_tags:
            if script.string and '"keywords":[' in script.string:
                try:
                    # Extract the JSON data
                    json_data = script.string
                    start = json_data.find('"keywords":[') + 11
                    end = json_data.find(']', start)
                    if start > 10 and end > start:
                        tags_str = json_data[start:end].strip('"')
                        tags = [tag.strip('" ') for tag in tags_str.split(',')]
                        if tags and len(tags) > 0 and tags[0]:
                            return {'success': True, 'tags': tags}
                except Exception as e:
                    print(f"Error parsing JSON-LD: {str(e)}")
        
        # Fallback to meta tags
        meta_keywords = soup.find("meta", attrs={"name": "keywords"})
        if meta_keywords and 'content' in meta_keywords.attrs:
            tags = [tag.strip() for tag in meta_keywords['content'].split(',')]
            return {'success': True, 'tags': tags}
            
        return {'success': False, 'message': 'No tags found in video metadata'}
        
    except Exception as e:
        return {'success': False, 'message': f'Error extracting tags: {str(e)}'}

