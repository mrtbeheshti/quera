all_users = {}
all_albums = {}


def add_user(username, age, city, albums, all_users, all_albums):
    all_users[username] = {"age": age, "city": city, "albums": albums}


def add_album(name, artist_name, genre, tracks, all_users, all_albums):
    all_albums[name] = {"artist_name": artist_name, "genre": genre, "tracks": tracks}


def query_user_artist(username, artist_name, all_users, all_albums):
    tracks = int()
    for album in all_users[username]["albums"]:
        if all_albums[album]["artist_name"] == artist_name:
            tracks += all_albums[album]["tracks"]
    return tracks


def query_user_genre(username, genre, all_users, all_albums):
    tracks = int()
    for album in all_users[username]["albums"]:
        if all_albums[album]["genre"] == genre:
            tracks += all_albums[album]["tracks"]
    return tracks


def query_age_artist(age, artist_name, all_users, all_albums):
    tracks = int()
    for user in all_users:
        if all_users[user]["age"] == age:
            for album in all_users[user]["albums"]:
                if all_albums[album]["artist_name"] == artist_name:
                    tracks += all_albums[album]["tracks"]
    return tracks


def query_age_genre(age, genre, all_users, all_albums):
    tracks = int()
    for user in all_users:
        if all_users[user]["age"] == age:
            for album in all_users[user]["albums"]:
                if all_albums[album]["genre"] == genre:
                    tracks += all_albums[album]["tracks"]
    return tracks


def query_city_artist(city, artist_name, all_users, all_albums):
    tracks = int()
    for user in all_users:
        if all_users[user]["city"] == city:
            for album in all_users[user]["albums"]:
                if all_albums[album]["artist_name"] == artist_name:
                    tracks += all_albums[album]["tracks"]
    return tracks


def query_city_genre(city, genre, all_users, all_albums):
    tracks = int()
    for user in all_users:
        if all_users[user]["city"] == city:
            for album in all_users[user]["albums"]:
                if all_albums[album]["genre"] == genre:
                    tracks += all_albums[album]["tracks"]
    return tracks
