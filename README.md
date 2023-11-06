# About

This project is a selfbot designed to spam a song you choose.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

1. You will need to have [Python 3.6 or later](https://www.python.org/downloads/release/python-360/) installed.

### Installing

1. Download the source code from the repository.
2. Open a terminal in the directory you downloaded the source code to.
3. Run `pip install -r requirements.txt` to install the dependencies.
4. Run `python main.py` to start the bot.
5. Enjoy!

## Deployment
I use [Heroku](https://www.heroku.com/) to host my bot. You can use whatever you want.
If you want to use Heroku, you can follow [this guide](https://github.com/talet1/spam-selfbot/tree/main#heroku) to get started.

### Heroku
1. Create a new app.
2. Go to the `Deploy` tab.
3. Connect your GitHub account.
4. Search for the forked repository.
5. Click `Deploy Branch` to deploy the 'heroku' branch.
6. Go to the `Resources` tab.
7. Disable the `web` dyno and enable the `worker` dyno.
8. Go to the `Settings` tab.
9. Click `Reveal Config Vars`.
10. Add a new variable with the key 'TOKEN', 'CHANNEL', and 'SONG_INDEX'.
11. Click `Add`.
12. Go to the `Overview` tab.
13. Click `Configure Dynos`.
14. Set the `worker` dyno to `ON`.
15. Enjoy!

## Example 
![Example](https://i.imgur.com/5Z3Z3ZP.png)
