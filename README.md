# ChangeChecker

A quick, dirty, and barely functional website change detector. 

## Setup

Setup is ezpz. First, setup Python https://www.python.org/

Once you have it installed, check by opening a command window and type `python --version`

If you got something like `Python 3.8.1` then you're good. 

## Configuration

For twilio text messages to work, you'll need to make a new twilio account and get a twilio phone number. https://www.twilio.com/docs/wireless/tutorials/communications-guides/how-to-send-and-receive-text-messages

After that, open up "config.json" and plop the numbers, url of the site you want watched, and the search term you want to use into the config and then save it. 

Once you've got that saved, open up a command window, navigate to the directory, and run `python ChangeCheck.py`

## Contrib

I'll accept basically any change to the repo so long as it's clean and makes sense. I'm not actively maintaining this so changes beyond this from me are unlikely. 