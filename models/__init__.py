#!/usr/bin/python3

"""Initialize the module"""


from .engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
