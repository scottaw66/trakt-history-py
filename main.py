#!/Users/scott/Scripts/python/venv/bin/python
import os
import argparse
import pyperclip
from dotenv import load_dotenv
from datetime import datetime, timedelta
from constants import *
from api.core import init
import api.core

def main():
    load_dotenv()
    
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    APPLICATION_ID = os.getenv("APPLICATION_ID")
    USERNAME_ID = os.getenv("USERNAME_ID")
    
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--auth', action='store_true', help='Perform OAuth authorization')
    args = parser.parse_args()
    
    api.core.AUTH_METHOD = api.core.OAUTH_AUTH  # Set the auth method to OAuth
    api.APPLICATION_ID = APPLICATION_ID
    
    if args.auth:
        init(USERNAME_ID, client_id=CLIENT_ID, client_secret=CLIENT_SECRET, store=True)
        
    from api.users import User
    me = User(USERNAME_ID)
    
    start_from_date = (datetime.now() - timedelta(days=MOVIE_HISTORY_DAYS)).strftime("%Y-%m-%d")
    movie_history = me.get_history_movies(start_date=start_from_date)
    
    output = "### Movies\n\n"
    
    for entry in movie_history:
        title = entry['title']
        ids = entry['ids']
        tmdb_id = ids['tmdb']
        slug = ids['slug']
        watched_at = entry['watched_at']
        
        # Convert watched_at to a datetime object
        watched_at_date = datetime.fromisoformat(watched_at.replace("Z", "+00:00"))
        
        # Format the output string
        output += f"- [{title}](https://www.themoviedb.org/movie/{tmdb_id}-{slug})\n"
        
    output += "\n### TV Shows\n\n"
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
        
        # Convert watched_at to a datetime object
        watched_at_date = datetime.fromisoformat(watched_at.replace("Z", "+00:00"))

        # Format the output string
        output += f"- [{title} Season {season} Episode {number} – {episode_title}](https://www.themoviedb.org/tv/{tmdb_id}-{slug}/season/{season}/episode/{number})\n"

    print(output)
    pyperclip.copy(output)

if __name__ == "__main__":
    main()
