
import requests
from flask import Flask, render_template, request
import logging  # Import logging module

app = Flask(__name__)


API_KEY = '<youtube_api_token>'

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', 'Python tutorial')  # Default search query if none provided
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

    response = requests.get(url, params=params)
    
    # Log the response status and content for debugging
    logging.debug(f'Response Status Code: {response.status_code}')
    logging.debug(f'Response Content: {response.text}')

    # Check if the response was successful
    if response.status_code != 200:
        return []  # Return an empty list if there's an error

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
