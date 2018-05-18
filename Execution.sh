sudo pip install virtualenv
cd api
virtualenv venv
source venv/bin/activate
pip install flask flask-jsonpify flask-sqlalchemy flask-restful
python songsearchapi.py