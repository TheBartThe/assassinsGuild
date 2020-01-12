import unittest

from flask import url_for
from flask_testing import TestCase
from application import app, routes

class TestBase(TestCase):

    def create_app(self):
        config_name = "testing"
        return app

class UnitTest(TestBase):

    def test_home(self):
        # Test home page is accessible
        response = self.client.get(url_for('home'))
        self.assertEqual(response.status_code, 200)

    def test_mission(self):
        # Test mission page is accessible
        response = self.client.get(url_for('mission'))
        self.assertEqual(response.status_code, 200)
