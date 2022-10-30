import os
import discord

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

    if userMessage[0:3] == ",p ":
        playerOrClanTag = userMessage[4:]
        await message.channel.send(
            f"https://fwa.chocolateclash.com/cc_n/member.php?tag={playerOrClanTag}")

    if userMessage[0:3] == ",c ":
        playerOrClanTag = userMessage[4:]
        await message.channel.send(
            f"https://fwa.chocolateclash.com/cc_n/clan.php?tag={playerOrClanTag}")


client.run(myToken)
