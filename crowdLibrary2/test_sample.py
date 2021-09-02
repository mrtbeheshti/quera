import os, sys, inspect
import time

from django.test import TestCase, Client
import requests
from ans import process
from qrequest.models import Book
import os

class TestBook(TestCase):

    def test_1(self):
        os.system('python manage.py makemigrations&')
        os.system('python manage.py migrate&')
        os.system('python manage.py runserver &')
        time.sleep(10)
        link = "http://127.0.0.1:8000/chess/"
        data = {'name':'test_1', 'category':'chess'}
        process(data)
        response = requests.get(link)
        for book in response.json():
            if book['name'] == 'test_1':
                return self.assertEqual(0, 0)
        return self.assertEqual(0, 1)

    