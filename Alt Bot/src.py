import random
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pystyle
import time
import psutil

alts = [
    # Put the .rbxcookie's of your alts here.
]

def find():
    return alts[random.randint(0, len(alts) - 1)]

attempt = 0

def join(session, game, job):
    if attempt > 5:
        print("Rate limit has been reached! Please fix your Roblox player before trying again.")
        return
    global attempt
    attempt = 0

    session.add_cookie({'name': '.ROBLOSECURITY', 'value': find()})
    session.get(f"roblox://game/PlaceLauncher.aspx?placeId={str(game)}&gameId={str(job) or 0}")
    try:
        WebDriverWait(session, 10).until(EC.presence_of_element_located((By.ID, "game-container")))
        print("Joined game!")
    except:
        print("Alt Bot could not join the game! Please retry")

    while True:
        if "RobloxPlayerBeta.exe" not in [program.name() for program in psutil.process_iter()]:
            res = int(input(pystyle.Center.XCenter("""
            You have closed the game!
            Do you want to rejoin?
            [1] Yes
            [2] No
            """)))
            if res == 1:
                return
            else:
                break

def main():
    print(pystyle.Center.XCenter("""
    =============================
    ALT-BOT V1
    Made by Alto
    =============================
    """))

    option = int(input(pystyle.Center.XCenter("""
    Please input the game you want to join >>>
    """)))
    server = int(input(pystyle.Center.XCenter("""
    Do you want to join a specific server?
    [1] Yes
    [2] No
    """)))

    session = webdriver.Chrome()

    if server == 2:
        join(session, option, 0)
    else:
        srv = input(pystyle.Center.XCenter("What server?"))
        join(session, option, srv)

    session.quit()

main()
