from flask import Flask, render_template, jsonify
from fetch import fetch, return_frontend_config
from os import listdir
from random import choice

app = Flask(__name__)

# Add default cover img logic
dir, ext = 'static/default_covers', ('.png','jpg','jpeg','webp')

default_covers = []

for file in listdir(dir):
  if file.endswith(ext):
    default_covers.append(f'../static/default_covers/{file}')
  continue

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/ajax/fetch')
def return_data():
  try:
    current_details = fetch()
    # Get song details
    song_id = current_details["id"]
    song_name = current_details["name"]
    song_cover = current_details["cover"] if song_id != None else choice(default_covers)
    song_artists = current_details["artists"]

  except:
    song_id, song_name, song_cover, song_artists = None, "Wait a moment...", choice(default_covers), "Wait a moment..."
  return jsonify(song_id=song_id,song_name=song_name,song_cover=song_cover,song_artists=song_artists)

@app.route('/ajax/onload')
def on_load():
  frontend_config = return_frontend_config()
  artist_color = frontend_config["artist_color"]
  title_color = frontend_config["title_color"]
  background_color = frontend_config["background_color"]
  width = frontend_config["width"]
  flip = "row-reverse" if frontend_config["flip"] else "row"
  cover = choice(default_covers)
  return jsonify(artist_color=artist_color,title_color=title_color,background_color=background_color,width=width,flip=flip,cover=cover)

if __name__ == '__main__':
  app.run()