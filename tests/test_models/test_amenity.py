#!/usr/bin/python3
"""Unittest for Amenity"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """test Amenity"""

    def test_init(self):
        """test blank amenity init"""
        snapshot = datetime.now()
        am1 = Amenity()
        snapshot2 = datetime.now()

        self.assertIsInstance(am1.id, str)
        self.assertTrue(len(am1.id) > 0)
        self.assertTrue('Amenity.' + am1.id in storage.all().keys())

        self.assertIsInstance(am1.created_at, datetime)
        self.assertLess(am1.created_at, snapshot2)
        self.assertGreater(am1.created_at, snapshot)
        
        self.assertIsInstance(am1.updated_at, datetime)
        self.assertLess(am1.updated_at, snapshot2)
        self.assertGreater(am1.updated_at, snapshot)
        
        am1.save()
        self.assertIsInstance(am1.updated_at, datetime)
        self.assertGreater(am1.updated_at, snapshot)
        self.assertGreater(am1.updated_at, snapshot2)
        del am1

    def test_init_dict(self):
        """test dict basemodel init"""
        test_dict = {'updated_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        am2 = Amenity(**test_dict)

        self.assertIsInstance(am2.id, str)
        self.assertTrue(len(am2.id) > 0)
        self.assertTrue(am2.id == test_dict['id'])
        
        self.assertIsInstance(am2.created_at, datetime)
        self.assertTrue(am2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(am2.updated_at, datetime)
        self.assertTrue(am2.updated_at.isoformat('T') == test_dict['updated_at'])
        am2.save()
        self.assertGreater(am2.updated_at, am2.created_at)
        del am2

    def test_attribute(self):
        """asdad"""
        am3 = Amenity()

        self.assertTrue(hasattr(am3, "name"))
        self.assertIsInstance(am3.name, str)
