from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    import os
    port = int(os.getenv("PORT", 5000))  # Use Render's PORT env variable
    app.run(host='0.0.0.0', port=port)
