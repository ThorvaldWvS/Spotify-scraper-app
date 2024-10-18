from flask import Flask, request, render_template, redirect, url_for, session
import spotipy
from spotipy.oauth2 import SpotifyOAuth

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# Initialize Spotify API client
sp = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/set_credentials', methods=['POST'])
def set_credentials():
    global sp
    client_id = request.form['client_id']
    client_secret = request.form['client_secret']
    redirect_uri = url_for('redirect_uri', _external=True)
    sp_oauth = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
    session['sp_oauth'] = sp_oauth
    return "Credentials set successfully"

@app.route('/redirect_uri')
def redirect_uri():
    global sp
    sp_oauth = session.get('sp_oauth')
    code = request.args.get('code')
    token_info = sp_oauth.get_access_token(code)
    sp = spotipy.Spotify(auth=token_info['access_token'])
    return redirect(url_for('index'))

@app.route('/fetch_songs', methods=['POST'])
def fetch_songs():
    filter_type = request.form['filter_type']
    if filter_type == 'top_short':
        results = sp.current_user_top_tracks(time_range='short_term')
    elif filter_type == 'top_medium':
        results = sp.current_user_top_tracks(time_range='medium_term')
    elif filter_type == 'top_long':
        results = sp.current_user_top_tracks(time_range='long_term')
    elif filter_type == 'liked_songs':
        results = sp.current_user_saved_tracks()
    elif filter_type == 'listening_profile':
        results = sp.current_user_recently_played()
    else:
        return "Invalid filter type"

    songs = []
    for item in results['items']:
        song = {
            'name': item['name'],
            'artist': item['artists'][0]['name'],
            'album': item['album']['name'],
            'release_date': item['album']['release_date']
        }
        songs.append(song)

    return render_template('index.html', songs=songs)

if __name__ == '__main__':
    app.run(debug=True)
