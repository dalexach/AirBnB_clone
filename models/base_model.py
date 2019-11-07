#!/usr/bin/python3
from datetime import datetime
from uuid import uuid4
""" Module of base_model file
"""


class BaseModel(object):
    """BaseModel class: parent class of all child classes
    """

    def __init__(self):
        """Constructor of BaseModel
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.update_at = datetime.now()

    def __str__(self):
        """
        """
        return("[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """
        """
        self.update_at = datetime.now()

    def to_dict(self):
        """
        """
        class_dict = self.__dict__.copy()
        class_dict.update({'__class__': self.__class__.__name__})
        class_dict.update({'created_at': datetime.isoformat(self.created_at)})
        class_dict.update({'update_at': datetime.isoformat(self.update_at)})
        return class_dict
