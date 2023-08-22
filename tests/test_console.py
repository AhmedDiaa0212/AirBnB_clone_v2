#!/usr/bin/python3
"""Unittest module for the console"""

import unittest
import os
import json
import pycodestyle
from io import StringIO
from console import HBNBCommand
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestCommand(unittest.TestCase):
    """Class that tests the console"""

    def setUp(self):
        """Function empties file.json"""
        FileStorage._FileStorage__objects = {}
        FileStorage().save()