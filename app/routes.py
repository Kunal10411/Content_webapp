from flask import Flask, render_template
import requests  # or any other library to fetch YouTube data

app = Flask(__name__)

# Example YouTube data (you can replace this with actual API calls)
youtube_data = "<youtube_api_token>"

@app.route('/search')
def search():
    # Pass youtube_data to the template
    print(youtube_data)
    return render_template('search_results.html', videos=youtube_data)

if __name__ == '__main__':
    app.run(debug=True)
