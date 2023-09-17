#!/usr/bin/python3
"""Defines unittests for console.py."""

import os
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models.engine.db_storage import DBStorage
from models.engine.file_storage import FileStorage

class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the HBNB command interpreter."""

    @classmethod
    def setUpClass(cls):
        """Set up the testing environment.

        This method is called once before running any test methods.
        It renames any existing 'file.json' to 'tmp', resets the
        FileStorage objects dictionary, and creates an instance
        of the HBNBCommand class.
        """
        try:
            os.rename("file.json", "tmp")
        except IOError:
            pass
        cls.HBNB = HBNBCommand()

    @classmethod
    def tearDownClass(cls):
        """Tear down the testing environment.

        This method is called once after running all test methods.
        It restores the original 'file.json', deletes the test
        HBNBCommand instance, and closes the DBStorage session if used.
        """
        try:
            os.rename("tmp", "file.json")
        except IOError:
            pass
        del cls.HBNB
        if type(models.storage) == DBStorage:
            models.storage._DBStorage__session.close()

    def setUp(self):
        """Set up before each test method.

        This method is called before each individual test method.
        It resets the FileStorage objects dictionary.
        """
        FileStorage._FileStorage__objects = {}

    def tearDown(self):
        """Clean up after each test method.

        This method is called after each individual test method.
        It deletes any created 'file.json'.
        """
        try:
            os.remove("file.json")
        except IOError:
            pass


if __name__ == "__main__":
    unittest.main()
