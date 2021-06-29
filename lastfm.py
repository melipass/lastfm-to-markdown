import requests
import os
import json

def lastfm_request(payload):
    headers = {'user-agent': os.environ('LASTFM_USER')}
    payload['api_key'] = os.environ('LASTFM_API_KEY')
    payload['format'] = 'json'
    payload['user'] = os.environ('LASTFM_USER')
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
    for album in artist_and_album:
        payload = {'method': 'album.getinfo',
                   'artist': album[0],
                   'album': album[1]}
        images.append(lastfm_request(payload).json()['album']['image'][1]['#text'])
    return images


def update_readme(images):
    with open('README.md','r') as file:
        readme = file.readlines()
    lastfm_line_index = readme.index('<!-- lastfm -->\n') + 1
    lastfm_line = ''
    for url in images:
        lastfm_line = lastfm_line + '![lastfm' + str(images.index(url)) + '](' + url + ') '
    readme[lastfm_line_index] = lastfm_line
    with open('README.md', 'w') as file:
        file.writelines(readme)


update_readme(get_album_covers(get_weekly_album_chart()))
