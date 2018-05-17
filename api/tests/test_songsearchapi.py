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
