import requests
import json


## format song titles and save to new .json file ##
do_format_titles = False
if do_format_titles:
    filename = 'song_and_album_names.json'
    with open(filename) as f_obj:
        old_song_titles = json.load(f_obj)
    new_song_titles = []
    print(old_song_titles)
    for old_song_title in old_song_titles:
        new_song_title = {"song": old_song_title["song"].encode('ascii', 'ignore').decode(),
                          "album": old_song_title["album"].encode('ascii', 'ignore').decode()}
        #old_song_title.encode('ascii', 'ignore').decode()
        new_song_titles.append(new_song_title)

    data = {"titles": [new_song_title["song"] for new_song_title in new_song_titles]}
    with open("good_song_titles.json", 'w') as f:
        json.dump(data, f)


## load formatted song titles ##
do_load_titles = False
if do_load_titles:
    with open("good_song_titles.json") as f:
        in_json = json.load(f)
    song_titles = in_json['titles']


## function to call API, format lyric response, create file of cleaned API responses ##
## need to get lyrics for evermore songs now only
def get_lyrics(song_titles):
    data = {}
    for i, song_title in enumerate(song_titles):
        print(f'$Loading lyrics for: {song_title} , {i+1} / {len(song_titles)}')
        api_url = 'https://api.lyrics.ovh/v1/Taylor Swift/' + song_title
        api_response = requests.get(api_url)
        if api_response.status_code == 200:
            song_lyrics = json.loads(api_response.text)['lyrics']
            ascii_song_lyrics = song_lyrics.encode('ascii', 'replace').decode()
            separated_song_lyrics = ascii_song_lyrics.replace("\n", " ").replace("\r", " ").replace(',', ' ').replace('?', ' ').replace('(', ' ').replace(')', ' ').replace('.', ' ').lower()
            lyric_words = [word for word in separated_song_lyrics.split(" ") if word != ""]
            data[song_title.lower()] = lyric_words
    return data


do_save_lyrics = False
if do_save_lyrics:
    lyrics = get_lyrics(song_titles)
    with open('lyrics.json', 'w') as f:
        json.dump(lyrics, f)
    print(lyrics)


do_load_lyrics = True
if do_load_lyrics:
    with open('lyrics.json') as f:
        lyrics = json.load(f)

## convert lyrics.json to have lowercase song names ##
do_lower = False
if do_lower:
    new_lyric_dic = {}
    for song_name, lyrics in lyrics.items():
        new_lyric_dic[song_name.lower()] = lyrics

    with open('lyrics.json', 'w') as f:
        json.dump(new_lyric_dic, f)


## load dict of songs grouped by album ##
do_load_grouped_titles = True
if do_load_grouped_titles:
    with open('album_song_dict.json') as f:
        album_song_dict = json.load(f)
    # print(album_song_dict)


## group lyrics by album ##
do_group_lyrics = True
if do_group_lyrics:
    album_lyrics = {}
    for album, song_names in album_song_dict.items():
        album_lyrics[album] = []
        for song_name in song_names:
            try:
                lyrics_found = lyrics[song_name.lower()]
            except:
                lyrics_found = []
            album_lyrics[album].extend(lyrics_found)
    print(album_lyrics)

    with open('album_lyrics.json', 'w') as f:
        json.dump(album_lyrics, f)


## filter lyrics ##
import io
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

do_stopwords = True
if do_stopwords:
    data = {}
    stop_words = set(stopwords.words('english'))
    for album, lyrics in album_lyrics.items():
        data[album] = []
        lyrics_str = json.dumps(lyrics)
        # print(lyrics_str)
        print(type(lyrics_str))
        word_tokens = word_tokenize(lyrics_str)
        filtered_lyrics = [w for w in word_tokens if not w in stop_words]
        print(type(filtered_lyrics))
        while ',' in filtered_lyrics:
            filtered_lyrics.remove(',')
        while "''" in filtered_lyrics:
            filtered_lyrics.remove("''")
        while "``" in filtered_lyrics:
            filtered_lyrics.remove("``")
        print(filtered_lyrics)
        data[album].extend(filtered_lyrics)

    with open('filtered_lyrics.json', 'w') as f:
        json.dump(data, f)
