from flask import Flask, render_template, jsonify
from fetch import fetch

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ajax/fetch')
def return_data():
  try:
    current_details = fetch()
    print(current_details)
    # Get song details
    song_id = current_details["id"]
    song_name = current_details["name"]
    song_cover = current_details["cover"]
    song_artists = current_details["artists"]
  except:
    song_id, song_name, song_cover, song_artists = ["error" for i in range(4)]
  print(song_id,song_name,song_cover,song_artists)
  return jsonify(song_id=song_id,song_name=song_name,song_cover=song_cover,song_artists=song_artists)


if __name__ == '__main__':
  app.run()