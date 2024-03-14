#!/usr/bin/python3
"""Unittest for BaseModel"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.user import User


class TestUser(unittest.TestCase):
    """test BaseModel"""

    def test_ainit(self):
        """test blank basemodel init"""
        snapshot = datetime.now()
        um1 = User()
        snapshot2 = datetime.now()

        self.assertIsInstance(um1.id, str)
        self.assertTrue(len(um1.id) > 0)
        self.assertTrue('User.' + um1.id in storage.all().keys())

        self.assertIsInstance(um1.created_at, datetime)
        self.assertLess(um1.created_at, snapshot2)
        self.assertGreater(um1.created_at, snapshot)
        
        self.assertIsInstance(um1.updated_at, datetime)
        self.assertLess(um1.updated_at, snapshot2)
        self.assertGreater(um1.updated_at, snapshot)
        
        um1.save()
        self.assertIsInstance(um1.updated_at, datetime)
        self.assertGreater(um1.updated_at, snapshot)
        self.assertGreater(um1.updated_at, snapshot2)
        del um1
        
    def test_init_dict(self):
        """test dict basemodel init"""
        test_dict = {'updated_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        um2 = User(**test_dict)

        self.assertIsInstance(um2.id, str)
        self.assertTrue(len(um2.id) > 0)
        self.assertTrue(um2.id == test_dict['id'])
        
        self.assertIsInstance(um2.created_at, datetime)
        self.assertTrue(um2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(um2.updated_at, datetime)
        self.assertTrue(um2.updated_at.isoformat('T') == test_dict['updated_at'])
        um2.save()
        self.assertGreater(um2.updated_at, um2.created_at)
        del um2

    def test_attribute(self):
        """asdad"""
        um3 = User()

        self.assertTrue(hasattr(um3, "email"))
        self.assertTrue(hasattr(um3, "password"))
        self.assertTrue(hasattr(um3, "first_name"))
        self.assertTrue(hasattr(um3, "last_name"))

        self.assertIsInstance(um3.email, str)
        self.assertIsInstance(um3.password, str)
        self.assertIsInstance(um3.first_name, str)
        self.assertIsInstance(um3.last_name, str)
