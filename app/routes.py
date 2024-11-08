from dotenv import load_dotenv
from flask import Blueprint, render_template, request
from app.service import SearchFactory
import logging

main = Blueprint('main', __name__)

# Set up logging configuration
logging.basicConfig(level=logging.DEBUG)

@main.route('/', methods=['GET'])
def index():
    return "<h2>The app is up</h2>"

@main.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', 'Python tutorial')  # Default search query if none provided
    logging.debug(f'Search query: {query}')  # Log the search query

    # Youtube search
    youtube_search = SearchFactory.create_search(application="youtube", keywords=query)
    data = youtube_search.search()

    return render_template('search_results.html', videos=data)
