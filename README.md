# Neverless Discord Bot - README

This bot allows you to respond to user messages and publish announcements in a designated Discord channel using simple commands like `!announce`.

## Project Structure

```
Neverless Discord Bot/
├── main.py               # Main bot script (message handling + announcements)
├── responses.py          # Custom responses to user messages
├── .env                  # Environment variables file
└── README.md             # This usage guide
```

## Requirements

Install required packages:

```
pip install discord.py python-dotenv
```

Alternatively, create a `requirements.txt` file with:

```
discord.py
python-dotenv
```

And install them using:

```
pip install -r requirements.txt
```

## Environment Setup (.env File)

Create a `.env` file in the root directory:

```
DISCORD_TOKEN=your_discord_bot_token
GUILD_ID=your_channel_id_for_announcements
```

Replace `your_discord_bot_token` with your actual bot token. Replace `your_channel_id_for_announcements` with the actual channel ID where you want the bot to send `!announce` messages.

To get the channel ID:

- Enable Developer Mode in Discord → User Settings → Advanced → Developer Mode.
- Right-click your desired channel → Copy Channel ID.

## Running the Bot

In the project directory, run:

```
python main.py
```

You should see output like:

```
Neverless Bot#xxxx is now online
```

## Bot Usage

1. Respond to messages

The bot will reply to keywords like `hello`, `how are you`, or `roll dice`.

2. Publish announcements

In any text channel, type:

```
!announce Your message content
```

The bot will post that message in the channel defined by `GUILD_ID`.

Example:

```
!announce Tomorrow at 8 PM, we will host a community AMA. Join us in <#your_general_channel_id>
```

## Custom Responses

Edit `responses.py` to change how the bot responds to regular messages.

```python
elif 'goodbye' in lowered:
    return 'See you later!'
```

## Troubleshooting

- Make sure `.env` is in the same directory as `main.py`.
- Ensure the bot has "Send Messages" permission in both the input and announcement channels.
- Double-check your `GUILD_ID` is correct and is actually a channel ID, not a server ID.

