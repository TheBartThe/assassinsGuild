import unittest

from flask import url_for
from flask_testing import TestCase
from application import app, routes, mission

class TestBase(TestCase):

    def create_app(self):
        config_name = "testing"
        return app

class UnitTest(TestBase):

    def test_missionService(self):
        # Test mission service gives dictionary length 1 - should be message
        targetList = {"target": "testtarget", "targetPoints": 10}
        weaponList = {"weapon": "testweapom", "weaponPoints": 10}
        missiontest = mission.getMission(targetList, weaponList)
        self.assertEqual(len(missiontest), 1)
