#!/usr/bin/python3
"""unittest for filestorage"""
import unittest
import os
import json
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class TestFileStorage(unittest.TestCase):
    """class to test FileSTorage"""
    def test_class_variables(self):
        """class var test"""
        fs1 = FileStorage()
        list_app = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        for exists in fs1.all().keys():
            list_app.append(fs1.all()[exists])
        for exists in list_app:
            del fs1.all()[exists.__class__.__name__ + '.' + exists.id]

        self.assertFalse(hasattr(FileStorage, '__file_path'))
        self.assertFalse(hasattr(FileStorage, '__objects'))
        self.assertFalse(hasattr(fs1, '__file_path'))
        self.assertFalse(hasattr(fs1, '__objects'))
        del fs1
        if os.path.exists('file.json'):
            print('file still exists')
            os.remove('file.json')

    def test_all(self):
        """test all"""
        fs2 = FileStorage()
        list_app = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        for exists in fs2.all().keys():
            list_app.append(fs2.all()[exists])
        for exists in list_app:
            del fs2.all()[exists.__class__.__name__ + '.' + exists.id]

        self.assertIsInstance(fs2.all(), dict)
        self.assertEqual(fs2.all(), {})
        bm1, bm2 = BaseModel(), BaseModel()
        fs2.new(bm1)
        fs2.new(bm2)
        self.assertEqual(fs2.all(), {'BaseModel.' + bm1.id : bm1,
                                     'BaseModel.' + bm2.id : bm2})

        del bm1, bm2, fs2

    def test_new(self):
        """ test new """
        dic = {"id": "8d8b4200-z106-469d-aec9-70zae1224150",
               "__class__": "BaseModel",
               "updated_at": "2020-07-01T16:47:21.260793",
               "created_at": "2020-07-01T16:47:21.260752"}
        fs3 = FileStorage()
        list_app = []
        if os.path.exists('file.json'):
            os.remove('file.json')
        for exists in fs3.all().keys():
            list_app.append(fs3.all()[exists])
        for exists in list_app:
            del fs3.all()[exists.__class__.__name__ + '.' + exists.id]
        classes = [Amenity(**dic), BaseModel(**dic), City(**dic), Place(**dic),
                   Review(**dic), State(**dic), User(**dic)]

        for cls in classes:
            fs3.new(cls)
            self.assertIn(cls.__class__.__name__ + '.' + cls.id,
                          fs3.all())

        for cls in classes:
            name = cls.__class__.__name__
            self.assertTrue(name + '.' + cls.id in fs3.all().keys())

        for i in range(len(fs3.all().keys())):
            self.assertIn(fs3.all()[list(fs3.all().keys())[i]],
                          classes)
        for exists in classes:
            del exists
        del fs3
