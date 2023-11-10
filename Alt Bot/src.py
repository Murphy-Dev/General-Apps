import random
from selenium import webdriver
from typing import Any
import pystyle
import time
import psutil
alts: list[str] = [
  # Put the .rbxcookie's of your alts here.
]

def find():
  return alts[random.randint(0, len(alts) - 1)]

attempt: int = 0

async def join(game: int, job: int) -> None:
  if (attempt > 5):
    print("Rate limit has been reached! Please fix your roblox player before trying again.")
  session = webdriver.Chrome()
  session.get("https://roblox.com")
  session.add_cookie({'name': '.ROBLOSECURITY', 'value': find()})
  session.get(f"roblox://game/PlaceLauncher.aspx?placeId={str(game)}&gameId={str(job) or 0}")
  time.sleep(1)
  if ("RobloxPlayerBeta.exe" not in list(psutil.process_iter())):
    print("Alt Bot could not open RobloxPlayer! Please retry")
    global attempt
    attempt += 1
    await join(game, job)
  session.close()

def makefile(fil: str, data: Any):
  with open(fil, 'w') as file:
    file.write(data)
    file.close()

def writefile(fil: str) -> str:
  with open(fil, 'r') as file:
    res = fil
    file.close()
    return res



print(pystyle.Center.XCenter("""
  =============================
  Roblox ALT-BOT V1
  Made by Alto
  =============================
"""))

async def main():

  option = int(input(pystyle.Center.XCenter("""
  Please input the game you want to join >>>
  """)))
  server = int(input(pystyle.Center.XCenter("""
  Do you want to join a specific server?
  [1] Yes
  [2] No
  """)))

  if (server == 2):
    await join(option, 0)
    print(pystyle.Center.XCenter("""
    Joined game!
    """))
    while True:
      does = False
      for program in psutil.process_iter():
        does = (program.name == "RobloxPlayerBeta.exe")
      if (not does):
        res = int(print(pystyle.Center.XCenter("""
        You have closed the game!
        Do you want to rejoin?
        [1] Yes
        [2] No
        """)))
        if (res == 1):
          await main()
  else:
      srv: int =  int(input(pystyle.Center.XCenter("What server?")))
      await join(option, srv)
      print(pystyle.Center.XCenter("""
      Joined game!
      """))
      while True:
        does = False
        for program in psutil.process_iter():
          does = (program.name == "RobloxPlayerBeta.exe")
        if (not does):
          res = int(print(pystyle.Center.XCenter("""
          You have closed the game!
          Do you want to rejoin?
          [1] Yes
          [2] No
          """)))
          if (res == 1):
            await main()
main()
