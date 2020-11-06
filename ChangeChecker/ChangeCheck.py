import requests
from bs4 import BeautifulSoup
import time
from twilio.rest import Client
import os
import tweepy as tw
import json

# Code is terrible, thrown together even. Do a PR and fix if you want. 

json_settings_name = "config.json"
watch_url = ""
twilio_account_sid = ""
twilio_auth_token = ""
twilio_phone_number = ""
target_phone_number = ""


def setup():
    with open(json_settings_name) as jsonDataFile:
        jsonData = json.load(jsonDataFile)
    
    # I've never used global in python before cause I usually pass everything
    # around in functions. If there's a cleaner way PLEASE tell me or
    # make a PR (Doesn't help I only use python for lambda usually)
    global watch_url
    global watch_term
    global twilio_account_sid
    global twilio_auth_token
    global twilio_phone_number
    global target_phone_number

    watch_url = jsonData["watchUrl"]
    watch_term = jsonData["watchTerm"]
    twilio_account_sid = jsonData["twilioAccountSID"]
    twilio_auth_token = jsonData["twilioAccountToken"]
    twilio_phone_number = jsonData["twilioPhoneNumber"]
    target_phone_number = jsonData["yourPhoneNumber"]

# Responsible for sending a text message. 
def send_text(message_text):
    twilio_client = Client(twilio_account_sid, twilio_auth_token) 
    twilio_client.messages.create(to=target_phone_number, from_=twilio_phone_number, body=message_text)

def main():
    setup()
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    instances_found = 0

    while True:
        print("URL: " + watch_url)
        response = requests.get(watch_url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")

        if str(soup).find(watch_term) != instances_found:
            message_text = str(watch_term) + " changed from " + str(instances_found) + " to " + str(str(soup).find(watch_term)) + "."
            send_text(message_text)
            instances_found = str(soup).find(watch_term)
            print(message_text)

        time.sleep(300)

main()