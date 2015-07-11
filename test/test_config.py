from unittest import TestCase
from gitsync.config import Config

__author__ = 'wenqiushi'


class TestConfig(TestCase):
    def test_config_immutability(self):
        config = Config()
        expected = config.view_path_mapping()
        expected["new_key"] = "new_value"

        self.assertTrue("new_key" in expected)
        self.assertFalse("new_key" in config.view_path_mapping())
