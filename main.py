#!/Users/scott/Scripts/python/venv/bin/python
import os
import argparse
from dotenv import load_dotenv
from datetime import datetime, timedelta
from constants import *
from trakt import init
import trakt.core
from trakt.movies import get_recommended_movies

def main():
    load_dotenv()
    
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    APPLICATION_ID = os.getenv("APPLICATION_ID")
    USERNAME_ID = os.getenv("USERNAME_ID")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--auth', action='store_true', help='Perform OAuth authorization')
    args = parser.parse_args()
    
    trakt.core.AUTH_METHOD = trakt.core.OAUTH_AUTH  # Set the auth method to OAuth
    trakt.APPLICATION_ID = APPLICATION_ID
    
    if args.auth:
        init(USERNAME_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, store=True)
        
    from trakt.users import User
    me = User(USERNAME_ID)
    
    start_from_date = (datetime.now() - timedelta(days=MOVIE_HISTORY_DAYS)).strftime("%Y-%m-%d")

    print(f"Movie history: {me.get_history_movies(start_date=start_from_date)}\n")

    start_from_date = (datetime.now() - timedelta(days=SHOW_HISTORY_DAYS)).strftime("%Y-%m-%d")
    
    show_history = me.get_history_shows(start_date=start_from_date)
    
    # Iterate over each entry and format the output
    for entry in show_history:
        title = entry['title']
        ids = entry['ids']
        slug = ids['slug']
        episode = entry['episode']
        season = episode['season']
        number = episode['number']
        episode_title = episode['title']
        watched_at = entry['watched_at']
        tmdb_id = ids['tmdb']

        # Format the output string
        output = f"[{title} Season {season} Episode {number} – {episode_title}](https://www.themoviedb.org/tv/{tmdb_id}-{slug}/season/{season}/episode/{number}) {watched_at}"
        
        # Print the formatted output
        print(output)

if __name__ == "__main__":
    main()
