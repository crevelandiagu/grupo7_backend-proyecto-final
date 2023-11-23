from app import app
from datetime import datetime, timedelta
from faker import Faker
from unittest.mock import patch

import json

fake = Faker()

def test_ping():
    response = app.test_client().get('/contracts/ping')

    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'pong'

