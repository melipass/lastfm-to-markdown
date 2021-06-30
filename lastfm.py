import requests
import os
import sys

def lastfm_request(payload):
    headers = {'user-agent': os.getenv('LASTFM_USER')}
    payload['api_key'] = os.getenv('LASTFM_API_KEY')
    payload['format'] = 'json'
    payload['user'] = os.getenv('LASTFM_USER')
    response = requests.get('https://ws.audioscrobbler.com/2.0/',
                            headers=headers, params=payload)
    return response


def get_weekly_album_chart():
    payload = {'method': 'user.getweeklyalbumchart'}
    data = lastfm_request(payload).json()['weeklyalbumchart']['album']
    artist_and_album = []
    for i in range(len(data)):
        artist_and_album.append([data[i]['artist']['#text'],
                                data[i]['name']])
    return artist_and_album


def get_album_covers(artist_and_album):
    images = []
    i = 0
    for album in artist_and_album:
        if (i < os.getenv('IMAGE_COUNT')):
            payload = {'method': 'album.getinfo',
                       'artist': album[0],
                       'album': album[1]}
            images.append([album[0], album[1],
                          lastfm_request(payload).json()['album']['image'][1]['#text']])
            i = i + 1
        else:
            break
    return images


def update_readme(images):
    with open('README.md', 'r', encoding='utf-8') as file:
        readme = file.readlines()
    lastfm_line_index = readme.index('<!-- lastfm -->\n') + 1
    lastfm_line = '<p align="center">'
    for img in images:
        print(img[0])
        print(img[1])
        if (requests.get(img[2]).status_code == 200):
            lastfm_line = lastfm_line + '<img src="' + img[2] + '" title="' + img[0] + ' - ' + img[1] + '"> '
            # lastfm_line = lastfm_line + '![' + img[0] + ' - ' + img[1] + '](' + img[2] + ') '
        else:
            pass
    if (readme[lastfm_line_index] == lastfm_line):
        sys.exit(0)
    else:
        lastfm_line = lastfm_line + '</p>\n'
        readme[lastfm_line_index] = lastfm_line
    with open('README.md', 'w', encoding='utf-8') as file:
        file.writelines(readme)


update_readme(get_album_covers(get_weekly_album_chart()))
