#!/Users/scott/Scripts/python/venv/bin/python
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    
    CLIENT_ID = os.getenv("CLIENT_ID")
    CLIENT_SECRET = os.getenv("CLIENT_SECRET")
    APPLICATION_ID = os.getenv("APPLICATION_ID")
    USERNAME_ID = os.getenv("USERNAME_ID")
    
    print(f'{CLIENT_ID}\n{CLIENT_SECRET}\n{APPLICATION_ID}\n{USERNAME_ID}')
    

if __name__ == "__main__":
    main()
