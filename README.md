# Spotify-scraper-app
A webapp to scrape songs different metrics and make custom playlists

## Setup

1. Clone the repository:
   ```
   git clone https://github.com/ThorvaldWvS/Spotify-scraper-app.git
   cd Spotify-scraper-app
   ```

2. Create a virtual environment and activate it:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Obtain your Spotify API key and client secret:
   - Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications)
   - Log in with your Spotify account
   - Click on "Create an App"
   - Fill in the required details and click "Create"
   - You will find your Client ID and Client Secret on the app's dashboard

5. Set up environment variables:
   ```
   export SPOTIFY_CLIENT_ID='your_client_id'
   export SPOTIFY_CLIENT_SECRET='your_client_secret'
   ```

6. Run the webapp:
   ```
   flask run
   ```

## Usage

1. Open your web browser and go to `http://127.0.0.1:5000`
2. Enter your Spotify API key and client secret
3. Select the filter for scraping songs (e.g., top listened songs from short, medium, or long periods, liked songs, listening profiles)
4. Click "Fetch Songs" to display the fetched songs and information
