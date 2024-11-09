import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, request
import logging  # Import logging module

app = Flask(__name__)

# Replace this with your actual API key
load_dotenv()
API_KEY = os.getenv('API_KEY')
if not API_KEY:  # Check if API_KEY is set
    logging.error("API_KEY is not set. Please set the environment variable.")
    raise ValueError("API_KEY is not set.")

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', 'Python tutorial')  # Default search query if none provided
    logging.debug(f'Search query: {query}')  # Log the search query
    youtube_data = fetch_youtube_data(query)
    return render_template('search_results.html', videos=youtube_data)

def fetch_youtube_data(query):
    url = f'https://www.googleapis.com/youtube/v3/search'
    params = {
        'q': query,
        'key': API_KEY,
        'part': 'snippet',
        'maxResults': 15
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an error for bad responses
    except requests.exceptions.RequestException as e:
        logging.error(f'Error fetching data from YouTube API: {e}')
        return []  # Return an empty list if there's an error

    # Log the response status and content for debugging
    logging.debug(f'Response Status Code: {response.status_code}')
    logging.debug(f'Response Content: {response.text}')

    data = response.json()

    # Parse the results and return the list of videos
    videos = []
    if 'items' in data:  # Check if 'items' exists in the response
        for item in data['items']:
            video = {
                'title': item['snippet']['title'],
                'description': item['snippet']['description'],
                'video_id': item['id'].get('videoId'),  # Use get to avoid KeyError
                'thumbnail_url': item['snippet']['thumbnails']['high']['url']
            }
            videos.append(video)

    return videos

if __name__ == '__main__':
    app.run(debug=True)
