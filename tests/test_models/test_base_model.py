#!/usr/bin/python3
"""Unittest for BaseModel"""
import os
import time
import unittest
from datetime import datetime
from models import storage
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """test BaseModel"""

    def test_init(self):
        """test blank basemodel init"""
        snapshot = datetime.now()
        bm1 = BaseModel()
        snapshot2 = datetime.now()

        self.assertIsInstance(bm1.id, str)
        self.assertTrue(len(bm1.id) > 0)
        self.assertTrue('BaseModel.' + bm1.id in storage.all().keys())

        self.assertIsInstance(bm1.created_at, datetime)
        self.assertLess(bm1.created_at, snapshot2)
        self.assertGreater(bm1.created_at, snapshot)
        
        self.assertIsInstance(bm1.updated_at, datetime)
        self.assertLess(bm1.updated_at, snapshot2)
        self.assertGreater(bm1.updated_at, snapshot)
        
        bm1.save()
        self.assertIsInstance(bm1.updated_at, datetime)
        self.assertGreater(bm1.updated_at, snapshot)
        self.assertGreater(bm1.updated_at, snapshot2)
        del bm1
        
    def test_init_dict(self):
        """test dict basemodel init"""
        test_dict = {'updated_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')
                     , 'id': 'z3854b62-93fa-fbbe-27de-630706f8313c', 'created_at': datetime(1963, 11, 22, 12, 30, 00, 716921).isoformat('T')}
        bm2 = BaseModel(**test_dict)

        self.assertIsInstance(bm2.id, str)
        self.assertTrue(len(bm2.id) > 0)
        self.assertTrue(bm2.id == test_dict['id'])
        
        self.assertIsInstance(bm2.created_at, datetime)
        self.assertTrue(bm2.created_at.isoformat('T') == test_dict['created_at'])
        self.assertIsInstance(bm2.updated_at, datetime)
        self.assertTrue(bm2.updated_at.isoformat('T') == test_dict['updated_at'])
        bm2.save()
        self.assertGreater(bm2.updated_at, bm2.created_at)
        del bm2
