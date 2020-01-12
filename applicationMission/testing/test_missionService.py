import unittest

from flask import url_for
from flask_testing import TestCase
from application import app, routes

class TestBase(TestCase):

    def create_app(self):
        config_name = "testing"
        return app

class UnitTest(TestBase):

    def test_mission(self):
        # Test mission service is accessible
        response = self.client.get(url_for('mission'))
        self.assertEqual(response.status_code, 200)

    def test_targetResponse(self):
        # Test mission service gives dictionary length 1 - should be message
        mission = routes.mission().json()
        self.assertEqual(len(mission), 1)
