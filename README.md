# trakt-history-py

Python version of Trakt history grabber for updating my /now page at <https://scottwillsey.com/now/>

## Configuration

trakt-history-py requires you to [register an API app with Trakt](https://trakt.tv/oauth/applications/new). When creating your app, use the device authentication URI for Redirect URI.

You will need your app's Client ID, Client Secret, App ID, and your username. Create a .env file based on .env.tpl, and substitute the values of those four items in for the values in the .env file.

## Acknowledgments

The code in the modules and API portion of this application is from [glensc/python-pytrakt](https://github.com/glensc/python-pytrakt), which I forked to add history functionality, and then later decided to integrate directly into trakt-history-py.
