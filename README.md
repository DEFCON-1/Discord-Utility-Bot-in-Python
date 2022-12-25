# Discord Utility Bot in Python
This is a Discord Utility bot written in Python by DEFCON. It can be used to perform various tasks within a Discord server.

## Current Features:
* !status - Gives out the status of the bot if it's UP
* !host <hostname/domain> - Will resolve the IP address of given hostname
* !ip <IP address> - Will display the details of the given IP address
* !bin <number> - Will search and display the result of BIN (Bank Identification Number) of the given 6 digit BIN
* !dice - Fun command to roll a dice (random number between 1 - 6)
* !restart - (Owner only) Will restart the bot. Add your own Discord ID in the code on Line 14 to define owner variable.
* !kill - (Owner only) Will shutdown the bot instantly.
  
## Prerequisites
In order to run this bot, you will need the following:

* A Discord account and a server to run the bot on
* A Discord developer account and a bot token (instructions on how to get these can be found in the Discord Developer Guide below)
* Python 3.6 or higher
* The following Python libraries:
  - ***discord.py***
  - ***asyncio***
  - ***requests***
  - ***socket***
  - ***os***
  - ***sys***
  

## Setting up the bot
1. Clone this repository to your local machine using **``git clone https://github.com/DEFCON-1/Discord-Utility-Bot-in-Python.git``**
2. Navigate to the cloned repository in your terminal
3. Install the required libraries using ***python3 -m pip install -U discord.py***
4. Edit the ***utility.py*** and configure it by adding your own (Owner's) Discord ID on Line 14, Bot's Discord ID on Line 15 and lastly but most important, add your Bot's token on Line 165 that you will acquire from **<ins>[Discord Developer Portal](https://discord.com/developers/applications)</ins>**. It will be explained further down this README.
5. Run the bot using ***python utility.py***

## Discord Developer Guide
In order to run a Discord bot, you will need to have a Discord developer account and create a bot. Here are the steps to do so:

1. Go to the **<ins>[Discord Developer Portal](https://discord.com/developers/applications)</ins>** and sign in with your Discord account
2. Click the "New Application" button
3. Give your application a name and click "Create"
4. On the left side of the page, click the "Bot" tab
5. Click the "Add Bot" button
6. Click the "Copy" button next to the "Token" field to copy your bot's token. This is what you will use to authenticate your bot and allow it to connect to Discord servers. Make sure to keep this token secret and never share it with anyone
7. In order to add your bot to a server, you will need the server's ID. You can get this by enabling "Developer Mode" in the Discord app and right-clicking on the server's name. Click "Copy ID" to copy the server's ID

## Adding your bot to a server
In order to add your bot to a server, you will need to have the "Manage Server" permission on the server you want to add the bot to. Here are the steps to add your bot to a server:

1. Go to the **<ins>[Discord Developer Portal](https://discord.com/developers/applications)</ins>** and click on your application
2. On the left side of the page, click the "OAuth2" tab
3. Under "Scopes", select the "bot" scope
4. Under "Bot Permissions", select the permissions that your bot will need (e.g. "Send Messages", "Manage Server")
5. Click the "Copy" button next to the "URL" field to copy the OAuth2 URL
6. Paste the URL into your browser and select the server you want to add the bot to
7. Click "Authorize" to add the bot to the server

## Customizing the bot
You can customize the behavior of the bot by modifying the code in the ***utility.py*** file. The ***on_message()*** function is called whenever the bot receives a message, and you can add your own code to perform different actions based on the content of the message. For example, you could add a command that allows users to check the weather by sending a message like ***!weather city_name***.

You can also add additional functions to perform different tasks. For example, you could create a function that retrieves data from an API and sends it back to the user, or a function that allows users to play a game within the Discord server.

To access the Discord API and perform tasks such as sending messages, you will need to use the ***discord.py*** library. You can find the documentation for this library **<ins>[here](https://discordpy.readthedocs.io/en/latest/)</ins>**.

## Deploying the bot
Once you have customized your bot and tested it locally, you may want to deploy it so that it can run continuously and serve users in your Discord server. There are a few different options for deploying a Discord bot, including:

* Running the bot on a personal computer or server that is always on
* Using a service like **<ins>[Heroku](https://www.heroku.com/)</ins>** to host the bot
* Using a service like **<ins>[AWS Lambda](https://aws.amazon.com/lambda/)</ins>** to host the bot

Each of these options has its own pros and cons, and you will need to choose the one that best fits your needs.

## Additional resources

* **<ins>[Discord API documentation](https://discord.com/developers/docs/intro)</ins>**
* **<ins>[*discord.py* documentation](https://discordpy.readthedocs.io/en/latest/)</ins>**
* **<ins>[Python documentation](https://docs.python.org/)</ins>**

#### Created by DEFCON
<sub>Donate (ETH): 0x3D2d605DE86cAf188f7b06595D14fC6ce1eeC71d</sub>
