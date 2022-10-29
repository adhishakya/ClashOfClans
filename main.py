import os
import discord
# import requests  # install requests module using 'pip install requests'

myToken = os.environ["TOKEN"]

intents = discord.Intents.all()
intents.messages = True

client = discord.Client(intents=intents)


@client.event
async def on_ready():
  print(f"{client.user} is online")


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  userMessage = str(message.content)

  # print(userMessage)

  if userMessage[0:3] == ",p ":
    playerOrClanTag = userMessage[4:]
    await message.channel.send(
      f"https://fwa.chocolateclash.com/cc_n/member.php?tag={playerOrClanTag}")

  if userMessage[0:3] == ",c ":
    playerOrClanTag = userMessage[4:]
    await message.channel.send(
      f"https://fwa.chocolateclash.com/cc_n/clan.php?tag={playerOrClanTag}")

  # if userMessage[0:3] == ",r ":
  #   assignRoles = userMessage[4:]
  #   url = "https://api.clashofclans.com/v1/players/%23" + assignRoles
  #   url = "https://api.clashofclans.com/v1/clans/%23" + assignRoles

  # headers = {"Accept": "application/json", "authorization": "Bearer %s" % key}

  # response = requests.request("GET", url, headers=headers)
  # data = response.json()
  # # print(data)
  # clanName = data['clan']['name']
  # townHall = data['townHallLevel']
  # clanRole = data['role']
  # print(clanName)
  # print(townHall)
  # print(clanRole)


client.run(myToken)
