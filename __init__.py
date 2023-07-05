#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os

type_storage = os.getenv('HBNB_TYPE_STORAGE')

if type_storage == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()
elif type_storage == 'fs':
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
