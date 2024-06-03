<p align="center">A Discord Bot that forwards the latest post from a VK community page to a Discord channel</p>

<p align="center"><img alt="image" src="pictures/image.png" /></p>

## Description
The bot fetches the latest post from a VK community feed and publishes it to a Discord channel (supports sending only one image).

### Usage
`/ping` - command to check if the bot is working

`/post` - publishes a post from the VK page in an embed format

### Configuration

The bot is configured in the `config.json` file.

- `token` - [Discord Bot Token](https://discord.com/developers/applications/)
- `vk_token` - [VK Application Token](https://dev.vk.com/ru/admin/apps-list)
- `app_id` - [VK Application ID](https://dev.vk.com/ru/admin/apps-list)
- `group_id` - VK community ID
- `prefix` - bot prefix
- `channel_id` - Discord channel ID where the post will be sent

## Installation and Launch

### Installation

```bash
git clone https://github.com/Bebrowskiy/vk-to-discord-bot.git
```

### Dependencies

```bash
cd vk-to-discord-bot/
```
```bash
pip install -r requirements.txt
```

### Launch

```bash
cd Posting-Bot/
```
```bash
python bot.py
```

<p align="center"><a href="https://vk.com/bebrow2021">My VK Page</a></p>
