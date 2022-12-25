### Discord Utility Bot in Python written by DEFCON, GitHub: https://github.com/DEFCON-1 ###

import discord
import requests
import random
import socket
import os
import sys
import asyncio
import xml.etree.ElementTree as ET

client = discord.Client(intents=discord.Intents.all())

owner = 000000000000000000 #Owner's Discord ID here
bot = 000000000000000000 #Bot's own Discord ID here

def get_ip_details(ip_address):
    # Send a request to the IPInfo API
    url = f'https://ipinfo.io/{ip_address}/json'
    response = requests.get(url)

    # Extract the relevant information from the API response
    data = response.json()
    country = data['country']
    region = data['region']
    city = data['city']
    location = data['loc']
    org = data['org']

    # Format the information as a message
    message = f'Country: {country}\nRegion: {region}\nCity: {city}\nLocation: {location}\nOrganization: {org}'

    return message

@client.event
async def on_message(message):

    if message.author == client.user:
        return

### Listen and respond to !Help command ###
    elif message.content == '!help':
#        example_commands = [
#            '!host <hostname/domain> - will resolve the IP address of given hostname',
#            '!ip <IP address> - will display the details of the given IP address',
#            '!bin <number> - will search and display the result of BIN (Bank Identification Number) of the given 6 digit BIN',
#            '!dice - will roll a dice',
#            '!restart - (Owner only) will restart the bot',
#            '!kill - (Owner only) will shutdown the bot instantly',
#        ]
#        response = '\n'.join(example_commands)
#        await message.channel.send(response)
         embedVar = discord.Embed(title="Unix Bot Commands", description="The detailed information of all the commands", color=0x00ff00)
         embedVar.add_field(name="!status", value="Gives out the status of the bot if it's UP.", inline=True)
         embedVar.add_field(name="!host <hostname/domain>", value="will resolve the IP address of given hostname", inline=True)
         embedVar.add_field(name="!ip <IP address>", value="will display the details of the given IP address", inline=True)
         embedVar.add_field(name="!bin <number>", value="will search and display the result of BIN (Bank Identification Number) of the given 6 digit BIN", inline=True)
         embedVar.add_field(name="!dice", value="will roll a dice", inline=True)
         embedVar.add_field(name="!restart", value="(Owner only) will restart the bot", inline=True)
         embedVar.add_field(name="!kill", value="(Owner only) will shutdown the bot instantly", inline=True)
         await message.channel.send(embed=embedVar)

### BOT Status ###
    elif message.content == '!status':
        embedVar = discord.Embed(title="UnixIRC Bot is UP!", description="Type !help to see the commands", color=0x00ff00)
        await message.channel.send(embed=embedVar)

### Host resolver ###
    elif message.content.startswith('!host'):
        hostname = message.content[6:] # Get the hostname by slicing the message content
        try:
             ip_address = socket.gethostbyname(hostname) # Resolve the hostname to an IP address
#            await message.channel.send(f'{hostname} has IP address {ip_address}') # Send the result to the same channel
             embedVar = discord.Embed(title="UnixIRC", description="", color=0x00ff00)
             embedVar.add_field(name="IP address of {}".format(hostname), value="Resolves to: {}".format(ip_address), inline=False)
             await message.channel.send(embed=embedVar)
        except socket.gaierror:
             await message.channel.send(f'Could not resolve hostname {hostname}') # If the hostname could not be resolved, send an error message

### IP Script ###
    # Check if the message starts with the !ip command
    elif message.content.startswith('!ip'):
        # Extract the IP address from the message
        ip_address = message.content[4:]

        # Get the details of the IP address
        ip_result = get_ip_details(ip_address)

        # Send the IP details to the user
        embedVar = discord.Embed(title="UnixIRC", description="", color=0x00ff00)
        embedVar.add_field(name="IP Lookup Results for {}".format(ip_address), value="{}".format(ip_result), inline=True)
        await message.channel.send(embed=embedVar)
#        await message.channel.send(ip_result)

### BIN Search ###
    # Check if the message starts with the !bin command
    elif message.content.startswith('!bin'):
        # get the BIN number from the message
        bin_number = message.content[5:]

        # send a request to the BIN lookup API
        r = requests.get(f'https://lookup.binlist.net/{bin_number}')

        # check if the request was successful
        if r.status_code == 200:
            # get the data from the response
            data = r.json()

            # create the response message
            response = f'Bank: {data["bank"]["name"]}\n' \
                       f'Country: {data["country"]["name"]}\n' \
                       f'Card Company: {data["scheme"]}\n' \
                       f'Card Type: {data["type"]}\n'
            if "category" in data:
                response += f'Card Category: {data["category"]}'
            else:
                response += "Card Category: Unknown"

            # send the response message
#            await message.channel.send(response)
            embedVar = discord.Embed(title="UnixIRC", description="", color=0x00ff00)
            embedVar.add_field(name="Bank Identification Number (BIN) Search Results for {}:".format(bin_number), value="{}".format(response), inline=False)
            await message.channel.send(embed=embedVar)
        else:
            # the request was unsuccessful, so send an error message
            await message.channel.send('An error occurred while looking up the BIN.')
            
### Dice Game ###    

    # Check if the message starts with the !dice command
    elif message.content.startswith('!dice'):
        # Get the user's ID from the message object
        user_id = message.author.id
        # Get the user object using the user's ID
        user = client.get_user(user_id)
        # Roll the dice and send the result to the Discord channel
        result = roll_dice()
        await message.channel.send(f'{user.mention} just rolled a dice: {result}')

### KILL ###
        
    elif message.content.startswith('!kill'):
        killer = message.author.id
        if killer == owner:
            await message.channel.send("Shutting Down...")
            await client.close()
        else:
            await message.channel.send("**Error:** You are not the owner")

### RESTART ###
        
    elif message.content.startswith('!restart'):
        killer = message.author.id
        if killer == owner:
            await message.channel.send("Alert: Restarting, please wait...")
            await asyncio.sleep(3)
            await message.channel.send("Succesfully Restarted")
            os.execv(sys.executable, ['python'] + sys.argv)
        else:
            await message.channel.send("**Error:** You are not the owner")

def roll_dice():
    return random.randint(1, 6)

client.run('YOUR-BOT-TOKEN-HERER')

### Discord Utility Bot in Python written by DEFCON, GitHub: https://github.com/DEFCON-1 ###