from flask import Flask, render_template, jsonify
import fetch

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ajax/fetch')
def fetch():
  # Get song details
  song_id = ""
  song_name = ""
  song_cover = ""
  song_artists = ""
  return jsonify(song_id=song_id,song_name=song_name,song_cover=song_cover,song_artists=song_artists)


if __name__ == '__main__':
  app.run()