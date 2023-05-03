# SIATAlevelChecker

> A Python based solution to review and watch graphically the river levels using the SIATA API 
> 
[![DownloadAMD64](https://img.shields.io/docker/image-size/02loveslollipop/discordgptchatbot/1.0.0amd64?label=AMD64&logo=docker&style=for-the-badge)](https://hub.docker.com/layers/02loveslollipop/discordgptchatbot/1.0.0amd64/images/sha256-c68b237e7b0340fc5eab7a1f016f8de3b650458e38f95e74e2af2638a3897c87)
[![DownloadARM64](https://img.shields.io/docker/image-size/02loveslollipop/discordgptchatbot/1.0.0arm64?label=ARM64&logo=docker&style=for-the-badge)](https://hub.docker.com/layers/02loveslollipop/discordgptchatbot/1.0.0arm64/images/sha256-391617d8318032a290c6ad942fb6819b96146297e61ad09186200958bb17b18c)
[![Replit](https://img.shields.io/badge/Run%20it%20on-Replit-orange?style=for-the-badge&logo=replit)](https://replit.com/@02loveslollipop/DiscordGPTChatBot)

## Intro
SIATA have an API that allows to recieve information about all of their services, this solution allows to use this information to have an easier undestanding of this data.

## Requirements

1. A linux based system

# Quick Setup

The repo have an autosetup.py, that allows and help the process of deploy of the services, if you want, it's also possible to manually deploy every container.

1. Install Python 3.9 in your device.

2. Clone the repository: 

```bash
git clone https://github.com/02loveslollipop/DiscordGPTChatBot.git
```

3. Install FFmpeg on your device, FFmpeg can be install [here](https://ffmpeg.org/)


4. Create a copy of ``example_config.yml`` and rename it as ``config.yml``, then open it and paste your Discord and OpenAI keys and change the role of the chat bot (Full description of [config.yml](https://github.com/02loveslollipop/DiscordGPTChatBot/wiki/Structure-of-config.yml)):

```yaml
bot:
  token: "YOUR_DISCORD_KEY" # Paste here the token you got from Discord Developer Portal

open_ai:
  token: "YOUR_OPEN_AI_KEY" # Paste here the OpenAI secret key you got from OpenAI platform
  role: "You are a helpful assistant." # Change here chatbot's role, this will change it's behavior answering questions
```

5. Install requirements:

```bash
pip -r /path/to/your/repo/requirements.txt
```

6. Run the bot:

```bash
python main.py
```


# Discord Commands
[Full list of commands here](https://github.com/02loveslollipop/DiscordGPTChatBot/wiki/Discord-commands)

# Configuration of config.yml
[Config.yml configuration guide](https://github.com/02loveslollipop/DiscordGPTChatBot/wiki/Structure-of-config.yml)