### technical-challenge-beenverified

# Installation Proccess
This API uses Virtual Environment to perform the search, this allows to keep separate the dependencies in this project and the other
dependencies installed in the computer.

To install Virtual Environment:
```bash
    $ sudo pip install virtualenv
```

Then go to the directory where you have the project
```bash
	$ cd path_to_my_project
```

Now setup the environment in this directory
```bash
	$ virtualenv venv
```

In this point you have the enviroment ready to use it, just now activate it
```bash
	$ source venv/bin/activate
```

You can know if you have correctly activated the environment because before your user name in the command line you can see the indicator (env).

Install the necessary dependencies into the activated environment
```bash
	$ pip install flask flask-jsonpify flask-sqlalchemy flask-restful
```

# API REST Execution

Now just execute
```bash
	$ python songsearchapi.py
```

Finally to search the information just go to the web browser and type something like

	http://127.0.0.1:5000/genre=Rock

This will return a result with the data in JSON format.
Search by genre:  http://127.0.0.1:5000/genre=genre
Search by song:   http://127.0.0.1:5000/song=name
Search by artist: http://127.0.0.1:5000/artist=artist

Note: The current port is the 5000 but if you have problems with it, you can change it to an unused port.

# Deactivating Environment
When you finish using the API, to deactivate the environment just execute
```bash
	$ deactivate
```

# Resume of bash commands
In your computer
```bash
    $ sudo pip install virtualenv
    $ cd path_to_my_project
    $ virtualenv venv
    $ source venv/bin/activate
```
In the active environment
```bash
    $ pip install flask flask-jsonpify flask-sqlalchemy flask-restful
    $ $ python songsearchapi.py
```
To deactivate the environment
```bash
    $ pip install flask flask-jsonpify flask-sqlalchemy flask-restful
    $ $ python songsearchapi.py
```