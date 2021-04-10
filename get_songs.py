import requests
import json

client_id = "zuo60iNcVNsA5BmyfHL64nzVMAfZ-suiFONibf8_EjOPXeUQgrIqX-w3CA-RRji8"
client_secret = "KsD2On2pG2zR7vgvTLkp7zW5i3LHoKuIB8OqyN0uV-AAIocMwwi8JQTeaolFozKSvQpiQkH6V0wGh6Jr7qSW1w"
token = "_Q2Mi2ftYFYIkFAUPY9lfkROyNXdj5ML8_6riblV-YCcfHvEvhy5k5Ax5zcWvd-E"
artist_name = 'taylor swift'

def make_call():
    # https://api.genius.com/search?access_token=styMFOz0rwFWW8jVUpCpGCmEnPdJkyLJFZwSKPqu_72SDVN0tynZxfFN7qsM6Fxs&q=Taylor+Swift
    url = "https://api.genius.com/search"
    payload = {'access_token': token,
               'q': artist_name}
    r = requests.get(url, params=payload)
    # print(json.dumps(resp.json(),indent=2))
    search_response = r.json()

    do_get_artist_id = False
    if do_get_artist_id:
        artist_id = search_response['response']['hits'][0]['result']['primary_artist']['id']
        print(artist_id)

    do_get_song_names_ids = False
    if do_get_song_names_ids:
        page_number = 1
        song_names_ids = []
        while True:
            # api.genius.com/artists/1177/songs?per_page=50
            url2 = "https://api.genius.com/artists/"
            payload2 = {'access_token': token,
                        'sort': 'popularity',
                        'per_page': 50,
                        'page': page_number}
            r2 = requests.get(url2 + str(artist_id) + "/songs", params=payload2)
            artist_songs_response = r2.json()
            songs = artist_songs_response['response']['songs']

            for song in songs:
                new_song = {}
                new_song['title'] = song['title']
                new_song['song_id'] = song['id']
                song_names_ids.append(new_song)

            if len(songs) < 50:
                break
            page_number += 1
            # print(json.dumps(artist_songs_resp_json,indent=2))
        print('done')
        #song_names_numbered = enumerate(song_names)
        for number, song in enumerate(song_names_ids):
            print(str(number) + ") " + str(song))

        filename = 'get_songs.json'
        with open(filename, 'w') as f_obj:
            json.dump(song_names_ids, f_obj)

    do_get_album_names = False
    if do_get_album_names:
        songs_and_albums = []
        filename = 'get_songs.json'
        with open(filename) as f_obj:
            song_names_ids = json.load(f_obj)

        for song in song_names_ids:
            new_song = {}
            url3 = "https://api.genius.com/songs/"
            payload3 = {'access_token': token}
            r3 = requests.get(url3 + str(song['song_id']), params=payload3)
            if r3.status_code == 200:
                song_album_response = r3.json()
                new_song['song'] = song_album_response['response']['song']['title']
                try:
                    new_song['album'] = song_album_response['response']['song']['album']['name']
                except:
                    new_song['album'] = "Unknown"
                print(new_song)
                songs_and_albums.append(new_song)

        print('done')

        for number, song in enumerate(songs_and_albums):
            print(str(number) + ") " + str(song))

        filename = 'song_and_album_names.json'
        with open(filename, 'w') as f_obj:
            json.dump(songs_and_albums, f_obj)


# if __name__ == "__main__":
#     make_call()


## format song and album titles and save to new .json file ##
do_format_titles = False
if do_format_titles:
    filename = 'song_and_album_names.json'
    with open(filename) as f_obj:
        song_album_list = json.load(f_obj) # old_titles holds a list of dicts
    new_song_album_list = []
    print(song_album_list)
    for song_album in song_album_list: # for dict in list
        # new_title = old_title.encode('ascii', 'ignore').decode() # need to change for dict??
        # new_titles.append(new_title)
        new_song_album = {"song": song_album["song"].encode('ascii', 'ignore').decode(),
                          "album": song_album["album"].encode('ascii', 'ignore').decode()}

        # old_title.encode('ascii', 'ignore').decode()

        new_song_album_list.append(new_song_album)

    data = {"new_song_album_list": new_song_album_list}

    with open("good_song_and_album_names.json", 'w') as f:
        json.dump(data, f)


## run code to add album names to dict as keys ##
do_add_album_keys = True
if do_add_album_keys:
    albums = ["Taylor Swift", "Fearless", "Speak Now", "Red (Deluxe Edition)", "1989", "reputation", "Lover", "folklore", "evermore"]
    album_song_dict = {}
    for album in albums:
        album_song_dict[album] = []


## load formatted song and album titles ##
do_load_titles = True
if do_load_titles:
    print(album_song_dict)
    with open("good_song_and_album_names.json") as f:
        in_json = json.load(f)
        song_album_list = in_json["new_song_album_list"]
        #song_list = []
        for song_album in song_album_list:
            if song_album["album"] in album_song_dict.keys():
                album_song_dict[song_album["album"]].append(song_album["song"])
        print(album_song_dict)
        with open("album_song_dict.json", 'w') as f:
            json.dump(album_song_dict, f)

    # song_titles = in_json["new_song_album_list"]["song"]
    # album_titles = in_json["new_song_album_list"]["album"]
