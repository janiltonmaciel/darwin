# -*- coding:utf-8 -*-

# Import system
import uuid


class SecurityUUID(object):

    @staticmethod
    def generate_uuid():
        return str(uuid.uuid4())
