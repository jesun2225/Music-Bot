
# 🎵 Discord Music Bot

A feature-rich Discord music bot built using `discord.py` and `wavelink`, designed for seamless music playback using a Lavalink node.

## 🚀 Features

- Slash command support
- Lavalink integration for high-quality music streaming
- Presence status customization
- Modular cog loading system
- Easy configuration using a config file

## 📁 Folder Structure

.
├── main.py               # Main entry point of the bot
├── requirements.txt      # Python dependencies
├── config/
│   └── config.py         # Bot and Lavalink configuration
└── cogs/
    └── music.py          # Music-related commands and logic

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/jesun2225/Music-Bot.git
cd discord-music-bot
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment

Edit `config/config.py` and fill in the required configuration:

```python
DISCORD_TOKEN = "your-bot-token"
BOT_PREFIX = "!"
APPLICATION_ID = 123456789012345678

LAVALINK_HOST = "localhost"
LAVALINK_PORT = 2333
LAVALINK_PASSWORD = "youshallnotpass"
LAVALINK_NAME = "MainNode"
LAVALINK_SECURE = False
```

Make sure you are running a Lavalink server matching your configuration.

### 4. Run the bot

```bash
python main.py
```

## 📦 Requirements

- Python 3.8+
- A running Lavalink server
- Discord bot token

## 📄 License

This project is licensed under the MIT License.

---

> Made with ❤️ by JESUN2225
