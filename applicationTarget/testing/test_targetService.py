import unittest

from flask import url_for
from flask_testing import TestCase
from application import app, routes

class TestBase(TestCase):

    def create_app(self):
        config_name = "testing"
        return app

class UnitTest(TestBase):

    def test_target(self):
        # Test target service is accessible
        response = self.client.get(url_for('target'))
        self.assertEqual(response.status_code, 200)

    def test_targetResponse(self):
        # Test target service gives dictionary length 2 - should be target and points
        target = routes.target().json()
        self.assertEqual(len(target), 2)
