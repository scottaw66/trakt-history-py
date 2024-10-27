#!/Users/scott/Scripts/python/venv/bin/python
import os
import argparse
from dotenv import load_dotenv
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
        exit()
        
    from trakt.users import User
    me = User(USERNAME_ID)
    print(f"Me: {me}\n\n")
    print(f"Watched shows: {me.watched_shows}\n\n")
    print(f"Show watchlist: {me.watchlist_shows}\n\n")
    print(f"Movie watchlist: {me.watchlist_movies}\n\n")
    print(f"Stats: {me.get_stats}\n\n")


if __name__ == "__main__":
    main()
