import requests
import json

TOKEN = "8876892182:AAHvOW3SLOTH5OAB3-Zb35oxfwUVpJCXWWs"

url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
response = requests.get(url)
data = response.json()

if data.get('ok') and data.get('result'):
    for message in data['result']:
        if 'message' in message:
            chat_id = message['message']['chat']['id']
            print(f"Chat ID found: {chat_id}")
            
            # Save to bot.py
            with open('bot.py', 'r') as f:
                bot_content = f.read()
            
            bot_content = bot_content.replace('CHAT_ID = "YOUR_CHAT_ID"', f'CHAT_ID = "{chat_id}"')
            
            with open('bot.py', 'w') as f:
                f.write(bot_content)
            
            print("✓ Chat ID updated in bot.py")
            break
else:
    print("No messages found. Please send a message to your bot first on Telegram.")
    print("\nTo get your chat ID:")
    print("1. Open Telegram and search for your bot")
    print("2. Send any message to the bot")
    print("3. Run this script again")