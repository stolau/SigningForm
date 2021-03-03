import os
import pytest
import tempfile
import time
from datetime import datetime
from sqlalchemy.engine import Engine
from sqlalchemy import event
from sqlalchemy.exc import IntegrityError #, StatementError

from formapp import create_app, db
from formapp import User, Form, Attendance

@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()

@pytest.fixture
def app():
    db_fd, db_fname = tempfile.mkstemp()
    config = {
        "SQLALCHEMY_DATABASE_URI": "sqlite:///" + db_fname,
        "TESTING": True
    }

    app = create_app(config)

    with app.app_context():
        db.create_all()
        
    yield app
    
    os.close(db_fd)
    os.unlink(db_fname)

def _get_user():
    return User(
        role='guest',
        fname='Who',
        lname='Doctor',
        email='timetraveller@tardis.net',
        #phone=''
    )

def _get_form():
    return Form(
        name='Extermination',
        sitepath='here'
    )

"""
def _get_attandance():
    
"""