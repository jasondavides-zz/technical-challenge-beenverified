"""Code for BeenVerified Engineer Technical Challenge.

This API expose the songs information in JSON format using the database located
in the folder db/"""
from flask import Flask
from flask import jsonify
from flask_restful import Api, Resource
from sqlalchemy import create_engine

# Database connection in folder db/
db_connect = create_engine('sqlite:///db/bvde.db')
app = Flask(__name__)
api = Api(app)


# This query is used as a base to create the final sql statement for each
# request, allowing us to get the different data as appropriate
_QUERY_SQL = '''SELECT S.title AS song, S.artist, G.name AS [genre name], S.duration
        FROM songs AS S
        INNER JOIN genres AS G
        ON S.genre = G.id'''.replace('\n', '')


def _auxiliar_sql_creator(field_to_compare, value_to_compare):
    """Function to create the query and call the getter function for the
    respective request"""
    params = (value_to_compare)
    query = \
        _QUERY_SQL + ''' and {field} = ?;'''.format(field=field_to_compare)
    return _auxiliar_get_result(query, params)


def _auxiliar_get_result(query, params=()):
    """Receiving the query and the parameters allows to perform the request
    and return the data as JSON data file"""
    conn = db_connect.connect()
    query = conn.execute(query, params)
    result = {'data': [
        dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    return jsonify(result)


class SongsByName(Resource):
    def get(self, song_name):
        return _auxiliar_sql_creator('S.title', song_name)


class SongsByGenre(Resource):
    def get(self, genre_name):
        return _auxiliar_sql_creator('G.name', genre_name)


class SongsByArtist(Resource):
    def get(self, artist_name):
        return _auxiliar_sql_creator('S.artist', artist_name)


class SongsByLength(Resource):
    def get(self, minimum_length, maximum_length):
        params = (minimum_length, maximum_length)
        query = _QUERY_SQL + ''' and S.duration between ? and ?;'''
        return _auxiliar_get_result(query, params)


class GenreInformation(Resource):
    def get(self):
        query = '''SELECT G.name AS [genre name], count(S.title) AS [number of songs],
            sum(S.duration) AS [total length]
            FROM songs AS S
            INNER JOIN genres AS G
            ON S.genre = G.id
            GROUP BY G.name;'''
        return _auxiliar_get_result(query)


api.add_resource(SongsByGenre, '/genre=<genre_name>')
api.add_resource(SongsByName, '/song=<song_name>')
api.add_resource(SongsByArtist, '/artist=<artist_name>')
api.add_resource(
    SongsByLength, '/song/minimum=<minimum_length>&maximum=<maximum_length>')
api.add_resource(GenreInformation, '/genre/info')


if __name__ == '__main__':
    # If the port 5000 is being used change this line to something like
    # app.run(port='another_port')
    app.run(host='0.0.0.0', port=5000, debug=True)
