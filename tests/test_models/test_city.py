#!/usr/bin/python3
"""Unittest for BaseModel"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.city import City


class TestCity(unittest.TestCase):
    """test BaseModel"""

    def test_init(self):
        """test blank basemodel init"""
        snapshot = datetime.now()
        cm1 = City()
        snapshot2 = datetime.now()

        self.assertIsInstance(cm1.id, str)
        self.assertTrue(len(cm1.id) > 0)
        self.assertTrue('City.' + cm1.id in storage.all().keys())

        self.assertIsInstance(cm1.created_at, datetime)
        self.assertLess(cm1.created_at, snapshot2)
        self.assertGreater(cm1.created_at, snapshot)
        
        self.assertIsInstance(cm1.updated_at, datetime)
        self.assertLess(cm1.updated_at, snapshot2)
        self.assertGreater(cm1.updated_at, snapshot)
        
        cm1.save()
        self.assertIsInstance(cm1.updated_at, datetime)
        self.assertGreater(cm1.updated_at, snapshot)
        self.assertGreater(cm1.updated_at, snapshot2)
        del cm1
        
    def test_init_dict(self):
        """test dict basemodel init"""
        test_dict = {'updated_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        cm2 = City(**test_dict)

        self.assertIsInstance(cm2.id, str)
        self.assertTrue(len(cm2.id) > 0)
        self.assertTrue(cm2.id == test_dict['id'])
        
        self.assertIsInstance(cm2.created_at, datetime)
        self.assertTrue(cm2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(cm2.updated_at, datetime)
        self.assertTrue(cm2.updated_at.isoformat('T') == test_dict['updated_at'])
        cm2.save()
        self.assertGreater(cm2.updated_at, cm2.created_at)
        del cm2

    def test_attribute(self):
        """asdad"""
        cm3 = City()

        self.assertTrue(hasattr(cm3, "state_id"))
        self.assertTrue(hasattr(cm3, "name"))

        self.assertIsInstance(cm3.state_id, str)
        self.assertIsInstance(cm3.name, str)
