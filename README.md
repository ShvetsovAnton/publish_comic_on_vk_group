# О проекте
Проект построен на большой любви к комиксам автора xkcd и практики библиотеки `requests`

[![imageup.ru](https://imageup.ru/img188/4135152/xkcd_angular_momentum.jpg)](https://imageup.ru/img188/4135152/xkcd_angular_momentum.jpg.html)


## Цель проекта:
- качать случайный комикс xkcd 
- каждый день постить случайный комикс xkcd в группе в [vk.com](https://vk.com/club217927528)

### Подробное описание проекта
Проект содержит три файла:
1. `main.py` - содержит в себе логику программы, переменные и переменные окружения.
2. `down_load_tools.py` - файл содержит инструменты для:
   - загрузки комикса в корневую папу проекта,
   - получения названия комикса и комментария автора к комиксу
   - удаления загруженного комикса из корневой папки проекта, чтобы не засорять проект.
3. `vk_load_tools.py` - файл содержит инструменты для:
    - получения id сервера на который можно загрузить комикс,
    - загрузки комикса на сервер,
    - сохранения комикса в альбом,
    - публикации комикса на стене сообщества в [vk.com](https://vk.com/feed).

***

# Подготовка к запуску проекта

#### Для запуска проекта нам понадобиться:

0. Авторизоваться в [vk.com](https://vk.com/login) или создать аккаунт.
1. [Создать группу](https://vk.com/groups_create) в [vk.com](https://vk.com/feed).
2. [Создать приложение](https://dev.vk.com/) в [vk.com](https://vk.com/feed) и получить id группы.
3. [Получить](https://imageup.ru/img115/4136101/chrome_oqsze2voot.png) id приложения,.
4. [Получить](https://replit.com/@AntonShvetsov1/getvkaccesstoken#main.py) `access_token`.
5. Создать файл `.env` положить в корневую папку проекта.
6. Добавить чувствительные данные в `.env`.

### Подробнее как создать приложение и получить `access_token`

#### При создании приложения необходимо указать тип "Standalone-приложение"

[![imageup.ru](https://imageup.ru/img258/4136122/chrome_ptyffpepjo.png)](https://imageup.ru/img258/4136122/chrome_ptyffpepjo.png.html)

#### После создания приложения нам понадобиться его id, он необходим для получения `access_token`

[![imageup.ru](https://imageup.ru/img86/4136186/chrome_lnvdx1piqr.png)](https://imageup.ru/img86/4136186/chrome_lnvdx1piqr.png.html)

#### Полученный id передать скрипт в [скрипт](https://replit.com/@AntonShvetsov1/getvkaccesstoken#main.py) и выдать разрешения на доступы.

[![imageup.ru](https://imageup.ru/img166/4136185/video-bez-nazvaniia-sdelano-v-clipchamp.gif)](https://imageup.ru/img166/4136185/video-bez-nazvaniia-sdelano-v-clipchamp.gif.html)

Из адресной строки скопировать`access_token`, он начинается с "vk1.a." и находиться в адресной строке между "access_token=" и "&expires_in="

Полученный токен добавляем в `.env`.

```python
VK_ACCESS_TOKEN="полученный токен"
```
### Как получить id группы

1. Зайдите в созданную группу.
2. Из адресной строки скопируйте всё что находится после "club".

[![imageup.ru](https://imageup.ru/img178/4136199/chrome_xsjdrpvpnf.png)](https://imageup.ru/img178/4136199/chrome_xsjdrpvpnf.png.html)

3. Полученный id добавить в `.env`

```python
VK_GROUP_ID="полученный id группы"
```

***

Пример запуска:
```python
python main.py
```

## Требования к окружению

Python3 должен быть уже установлен.
Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:

```python
pip install -r requirements.txt
```