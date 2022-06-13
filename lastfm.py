import requests 
import sys
from PIL import Image, ImageFont, ImageDraw 
import urllib.request
import os

def lastfm_request(payload):
    headers = {"user-agent": os.getenv("LASTFM_USER")}
    payload["api_key"] = os.getenv("LASTFM_API_KEY")
    payload["format"] = "json"
    payload["user"] = os.getenv("LASTFM_USER")
    response = requests.get("https://ws.audioscrobbler.com/2.0/",
                            headers=headers, params=payload)
    return response

def get_weekly_album_chart():
    payload = {"method": "user.getweeklyalbumchart"}
    data = lastfm_request(payload).json()["weeklyalbumchart"]["album"]
    artist_and_album = []
    for i in range(len(data)):
        artist_and_album.append([data[i]["artist"]["#text"],
                                data[i]["name"]])
    return artist_and_album


def get_album_covers(artist_and_album):
    images = []
    for album in artist_and_album:
        payload = {"method": "album.getinfo",
                   "artist": album[0],
                   "album": album[1]}
        request_response = lastfm_request(payload).json()
        url = request_response["album"]["image"][int(os.getenv("IMAGE_SIZE"))]["#text"]
        link_to_album = request_response["album"]["url"]
        if (url != ""):
            images.append([album[0], album[1], url, link_to_album]) 
    return images


def update_readme(images):
    with open("README.md", "r", encoding="utf-8") as file:
        readme = file.readlines()
    lastfm_line_index = readme.index("<!-- lastfm -->\n") + 1
    lastfm_line = '<p align="center">'
    i = 0
    for img in images:
        if (i < int(os.getenv("IMAGE_COUNT"))):
            if (requests.get(img[2]).status_code == 200):   

                list = ["album-covers", "album-covers-finished"]
                for items in list:
                    os.makedirs(items, exist_ok=True)

                urllib.request.urlretrieve(img[2], f"./album-covers/album-cover_{i}.png")
                my_image = Image.open(f"./album-covers/album-cover_{i}.png")  
                image_editable = ImageDraw.Draw(my_image) 
                image_editable.text((1,1), f"{img[0]}\n{img[1]}", (252, 255, 250), font=ImageFont.truetype("./fonts/basic_sans_serif_7.ttf", 10)) 
                my_image.save(f"./album-covers-finished/album-cover_final_{i}.png")
                
                lastfm_line += f'<a href="{img[3]}"><img src="./album-covers-finished/album-cover_final_{i}.png" title="{img[0]} - {img[1]}"></a> '
                i = i + 1
            else:
                pass
        else:
            break
    if (readme[lastfm_line_index] == lastfm_line):
        sys.exit(0)
    else:
        lastfm_line = lastfm_line + "</p>\n"
        readme[lastfm_line_index] = lastfm_line
    with open("README.md", "w", encoding="utf-8") as file:
        file.writelines(readme)

update_readme(get_album_covers(get_weekly_album_chart()))
