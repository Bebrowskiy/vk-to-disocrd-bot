<p align="center">Discord Бот, который пересылает самый последний пост со страницы сообщества VK в Discord канал</p>


<p align="center"><img alt="image" src="pictures/image.png" /></p>

## Описание
Бот берет самый последний пост с ленты сообщества ВК и публикует в дискорд канал(`Поддерживает только одно изображение к отправке`)

### Использование
`/ping` - команда для проверки работоспособности бота
`/post` - публикует пост со страницы ВК в формате `embed`

### Настройка

Настройка бота осуществляется в файле `config.json`

`token` - токен [Disocrd Бота](https://discord.com/developers/applications/)
`vk_token` - [токен приложения VK](https://dev.vk.com/ru/admin/apps-list)
`app_id` - [id приложения VK](https://dev.vk.com/ru/admin/apps-list)
`group_id` - id сообщества ВК
`prefix` -  префикс для бота
`channel_id` - id дискорд канала, куда будет отправляться пост
## Установка и запуск

### Установка

```bash
git clone https://github.com/Bebrowskiy/vk-to-disocrd-bot.git
```

### Зависимости

- disnake
- vk_api

```bash
cd vk-to-disocrd-bot/
```

```bash
pip install -r requirements.txt
```

### Запуск

```bash
cd Posting-Bot
python bot.py
```

<p align="center"> <a href="https://vk.com/bebrow2021">Моя страница в VK</a></p>
