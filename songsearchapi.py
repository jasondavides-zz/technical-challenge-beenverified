"""Code for BeenVerified Engineer Technical Challenge.

This API expose the songs information in JSON format using the database located
in the folder db/"""
from flask import Flask
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from flask import jsonify

# Database connection in folder db/
db_connect = create_engine('sqlite:///db/bvde.db')
app = Flask(__name__)
api = Api(app)


class SongsByName(Resource):
    def get(self, song_name):
        conn = db_connect.connect()
        params = (song_name)
        query = conn.execute(
            '''SELECT S.title AS Song, S.artist, G.name AS [genre name], S.duration
            FROM songs AS S
            INNER JOIN genres AS G
            ON S.genre = G.id
            and S.title = ?;''', params)
        result = {'data': [
            dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class SongsByGenre(Resource):
    def get(self, genre_name):
        conn = db_connect.connect()
        params = (genre_name)
        query = conn.execute(
            '''SELECT S.title AS song, S.artist, G.name AS [genre name], S.duration
            FROM songs AS S
            INNER JOIN genres AS G
            ON S.genre = G.id
            and G.name = ?;''', params)
        result = {'data': [
            dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


class SongsByArtist(Resource):
    def get(self, artist_name):
        conn = db_connect.connect()
        params = (artist_name)
        query = conn.execute(
            '''SELECT S.title AS song, S.artist, G.name AS [genre name], S.duration
            FROM songs AS S
            INNER JOIN genres AS G
            ON S.genre = G.id
            and S.artist = ?;''', params)
        result = {'data': [
            dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
        return jsonify(result)


api.add_resource(SongsByGenre, '/genre=<genre_name>')
api.add_resource(SongsByName, '/song=<song_name>')
api.add_resource(SongsByArtist, '/artist=<artist_name>')


if __name__ == '__main__':
    # If the port 5000 is being used change this line for app.run(port='8000')
    app.run()
