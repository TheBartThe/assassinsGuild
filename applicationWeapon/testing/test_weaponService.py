import unittest

from flask import url_for
from flask_testing import TestCase
from application import app

class TestBase(TestCase):

    def create_app(self):
        config_name = "testing"
        return app

class UnitTest(TestBase):

    def test_weapon(self):
        # Test weapon service is accessible
        response = self.client.get(url_for('correctAnswer'))
        self.assertEqual(response.status_code, 200)

    def test_weaponResponse(self):
        # Test weapon service gives dictionary length 2 - should be weapon and points
        weapon = routes.correctAnswer().json()
        self.assertEqual(len(weapon), 2)
