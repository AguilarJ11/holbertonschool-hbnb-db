#!/usr/bin/python3

from abc import ABC
import uuid
from datetime import datetime

class Basic_data(ABC):
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()
