#!/usr/bin/python3
"""Unittest for BaseModel"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.place import Place


class TestPlace(unittest.TestCase):
    """test BaseModel"""

    def test_init(self):
        """test blank basemodel init"""
        snapshot = datetime.now()
        pm1 = Place()
        snapshot2 = datetime.now()

        self.assertIsInstance(pm1.id, str)
        self.assertTrue(len(pm1.id) > 0)
        self.assertTrue('Place.' + pm1.id in storage.all().keys())

        self.assertIsInstance(pm1.created_at, datetime)
        self.assertLess(pm1.created_at, snapshot2)
        self.assertGreater(pm1.created_at, snapshot)
        
        self.assertIsInstance(pm1.updated_at, datetime)
        self.assertLess(pm1.updated_at, snapshot2)
        self.assertGreater(pm1.updated_at, snapshot)
        
        pm1.save()
        self.assertIsInstance(pm1.updated_at, datetime)
        self.assertGreater(pm1.updated_at, snapshot)
        self.assertGreater(pm1.updated_at, snapshot2)
        del pm1
        
    def test_init_dict(self):
        """test dict basemodel init"""
        test_dict = {'updated_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        pm2 = Place(**test_dict)

        self.assertIsInstance(pm2.id, str)
        self.assertTrue(len(pm2.id) > 0)
        self.assertTrue(pm2.id == test_dict['id'])
        
        self.assertIsInstance(pm2.created_at, datetime)
        self.assertTrue(pm2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(pm2.updated_at, datetime)
        self.assertTrue(pm2.updated_at.isoformat('T') == test_dict['updated_at'])
        pm2.save()
        self.assertGreater(pm2.updated_at, pm2.created_at)
        del pm2

    def test_attribute(self):
        """asdad"""
        pm3 = Place()

        self.assertTrue(hasattr(pm3, "city_id"))
        self.assertTrue(hasattr(pm3, "user_id"))
        self.assertTrue(hasattr(pm3, "name"))
        self.assertTrue(hasattr(pm3, "description"))
        self.assertTrue(hasattr(pm3, "number_rooms"))
        self.assertTrue(hasattr(pm3, "number_bathrooms"))
        self.assertTrue(hasattr(pm3, "max_guest"))
        self.assertTrue(hasattr(pm3, "price_by_night"))
        self.assertTrue(hasattr(pm3, "latitude"))
        self.assertTrue(hasattr(pm3, "longitude"))
        self.assertTrue(hasattr(pm3, "amenity_ids"))

        self.assertIsInstance(pm3.city_id, str)
        self.assertIsInstance(pm3.user_id, str)
        self.assertIsInstance(pm3.name, str)
        self.assertIsInstance(pm3.description, str)
        self.assertIsInstance(pm3.number_rooms, int)
        self.assertIsInstance(pm3.number_bathrooms, int)
        self.assertIsInstance(pm3.max_guest, int)
        self.assertIsInstance(pm3.price_by_night, int)
        self.assertIsInstance(pm3.latitude, float)
        self.assertIsInstance(pm3.longitude, float)
        self.assertIsInstance(pm3.amenity_ids, list)

