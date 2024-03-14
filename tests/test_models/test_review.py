#!/usr/bin/python3
"""Unittest for BaseModel"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.review import Review


class TestReview(unittest.TestCase):
    """test BaseModel"""

    def test_init(self):
        """test blank basemodel init"""
        snapshot = datetime.now()
        rm1 = Review()
        snapshot2 = datetime.now()

        self.assertIsInstance(rm1.id, str)
        self.assertTrue(len(rm1.id) > 0)
        self.assertTrue('Review.' + rm1.id in storage.all().keys())

        self.assertIsInstance(rm1.created_at, datetime)
        self.assertLess(rm1.created_at, snapshot2)
        self.assertGreater(rm1.created_at, snapshot)
        
        self.assertIsInstance(rm1.updated_at, datetime)
        self.assertLess(rm1.updated_at, snapshot2)
        self.assertGreater(rm1.updated_at, snapshot)
        
        rm1.save()
        self.assertIsInstance(rm1.updated_at, datetime)
        self.assertGreater(rm1.updated_at, snapshot)
        self.assertGreater(rm1.updated_at, snapshot2)
        del rm1
        
    def test_init_dict(self):
        """test dict basemodel init"""
        test_dict = {'updated_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        rm2 = Review(**test_dict)

        self.assertIsInstance(rm2.id, str)
        self.assertTrue(len(rm2.id) > 0)
        self.assertTrue(rm2.id == test_dict['id'])
        
        self.assertIsInstance(rm2.created_at, datetime)
        self.assertTrue(rm2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(rm2.updated_at, datetime)
        self.assertTrue(rm2.updated_at.isoformat('T') == test_dict['updated_at'])
        rm2.save()
        self.assertGreater(rm2.updated_at, rm2.created_at)
        del rm2

    def test_attribute(self):
        """asdad"""
        rm3 = Review()

        self.assertTrue(hasattr(rm3, "place_id"))
        self.assertTrue(hasattr(rm3, "user_id"))
        self.assertTrue(hasattr(rm3, "text"))

        self.assertIsInstance(rm3.place_id, str)
        self.assertIsInstance(rm3.user_id, str)
        self.assertIsInstance(rm3.text, str)
