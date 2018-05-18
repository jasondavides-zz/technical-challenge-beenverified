import flask
from json import loads
import requests

app = flask.Flask(__name__)


def test_songs_by_name():

    with app.test_request_context():
        songs = requests.get('http://127.0.0.1:5000/song=Gala')

    result = loads(songs.text)
    expected = {"data": [{"song": "Gala", "artist": "424", "duration": 189,
                         "genre name": "Indie Rock"}]}

    assert(expected == result)


def test_songs_by_genre():

    with app.test_request_context():
        songs = requests.get('http://127.0.0.1:5000/genre=Rock')

    result = loads(songs.text)
    expected = {"data": [{"artist": "Bobby Darin", "duration": 245,
                          "genre name": "Rock", "song": "Mack the Knife"}]}

    assert(expected == result)


def test_songs_by_artist():

    with app.test_request_context():
        songs = requests.get('http://127.0.0.1:5000/artist=424')

    result = loads(songs.text)
    expected = {"data": [{"song": "Gala", "artist": "424", "duration": 189,
                         "genre name": "Indie Rock"}]}

    assert(expected == result)


def test_songs_by_length():

    with app.test_request_context():
        songs = requests.get(
            'http://127.0.0.1:5000/song/minimum=200&maximum=300')

    result = loads(songs.text)
    expected = {"artist": "Bobby Darin", "duration": 245,
                          "genre name": "Rock", "song": "Mack the Knife"}

    assert(expected in result['data'])


def test_get_genre_info():

    with app.test_request_context():
        songs = requests.get(
            'http://127.0.0.1:5000/genre/info')

    result = loads(songs.text)
    expected = {"genre name": "Classic Rock", "number of songs": 2,
                "total length": 407}

    assert(expected in result['data'])


def test_empty_data_response():

    with app.test_request_context():
        songs = requests.get(
            'http://127.0.0.1:5000/song=Buddy Holly')

    result = loads(songs.text)
    expected = {"data": []}

    assert(expected == result)


def test_wrong_url():

    with app.test_request_context():
        songs = requests.get(
            'http://127.0.0.1:5000/song+Rock')

    result = songs.status_code
    expected = 404

    assert(expected == result)
