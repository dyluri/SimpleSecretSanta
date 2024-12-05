from dotenv import load_dotenv
import discord
import responses
import os

async def send_message(username, message, user_message, is_private):
    try:
        if is_private:
            response = responses.get_private_response(user_message, username)
            await message.author.send(response)
        else:
            response = responses.get_response(user_message, username)
            if response:
                await message.channel.send(response)
    except Exception as e:
        print(e)
        
def run_discord_bot():
    load_dotenv()
    TOKEN = os.getenv('TOKEN')
    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents = intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f'{username} said: "{user_message}" ({channel})')
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(username, message, user_message, is_private=True)
        else:
            await send_message(username, message, user_message, is_private=False)

    client.run(TOKEN)