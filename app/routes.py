import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, request
import logging  # Import logging module

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()
API_KEY = os.getenv('API_KEY')
if not API_KEY:  # Check if API_KEY is set
    logging.error("API_KEY is not set. Please set the environment variable.")
    raise ValueError("API_KEY is not set.")

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    # Fetch trending videos on initial load
    trending_videos = fetch_youtube_data("Trending")
    return render_template('index.html', videos=trending_videos)

@app.route('/search', methods=['GET'])
def search():
    # Get the search query from the URL, default to 'Python tutorial' if no query is provided
    query = request.args.get('query', 'Python tutorial')  
    logging.debug(f'Search query: {query}')  # Log the search query for debugging

    # Fetch YouTube data based on the search query
    youtube_data = fetch_youtube_data(query)

    # Render the search results page and pass the YouTube data to it
    return render_template('search_results.html', videos=youtube_data)

def fetch_youtube_data(query):
    url = f'https://www.googleapis.com/youtube/v3/search'
    params = {
        'q': query,
        'key': API_KEY,
        'part': 'snippet',
        'maxResults': 6  # Fetch top 6 trending videos for simplicity
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        logging.error(f'Error fetching data from YouTube API: {e}')
        return []  # Return an empty list if there's an error

    data = response.json()

    videos = []
    if 'items' in data:
        for item in data['items']:
            video = {
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'video_id': item['id'].get('videoId'),
                'thumbnail_url': item['snippet']['thumbnails']['high']['url']
            }
            videos.append(video)

    return videos

if __name__ == '__main__':
    app.run(debug=True)
