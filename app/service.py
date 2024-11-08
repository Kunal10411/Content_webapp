from abc import ABC, abstractmethod
from dotenv import load_dotenv
import requests
import logging
import os

load_dotenv()


class GlobalSearch(ABC):
    @abstractmethod
    def search(self):
        pass

class YoutubeSearch(GlobalSearch):
    def __init__(self, keywords:str) -> None:
        self.keywords = keywords
        self.API_KEY = os.getenv('API_KEY')

    def search(self):
        """ Search in Youtube using keywords"""
        url = f'https://www.googleapis.com/youtube/v3/search'
        params = {
            'q': self.keywords,
            'key': self.API_KEY,
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
        result = []
        if 'items' in data:  # Check if 'items' exists in the response
            for item in data['items']:
                video = {
                    'title': item['snippet']['title'],
                    'description': item['snippet']['description'],
                    'video_id': item['id'].get('videoId'),  # Use get to avoid KeyError
                    'thumbnail_url': item['snippet']['thumbnails']['high']['url']
                }
                result.append(video)
        return result

class InstagramSearch(GlobalSearch):
    def __init__(self, keywords:str) -> None:
        self.keywords = keywords

    def search(self):
        """Search in Instagram using keywords"""
        ## TODO : Implement the business logic
        pass

class SearchFactory:
    @staticmethod
    def create_search(application:str, **kwargs):
        if application == "youtube":
            return YoutubeSearch(
                keywords=kwargs.get('keywords')
            )
        
        if application == "instagram":
            return InstagramSearch(
                keywords=kwargs.get('keywords')
            )

        raise ValueError("Application is not valid !!")
    