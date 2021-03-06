# -*- coding:utf-8 -*-

# import system
from cryptography.fernet import Fernet

# import local
from darwin.security import unicode_dados


class SecurityToken(object):
    _fernet = None

    @classmethod
    def config(cls, password_secret_key):
        cls._fernet = Fernet(password_secret_key)

    @classmethod
    def encrypt(cls, key):
        key = unicode_dados(key)
        return cls.fernet().encrypt(key)

    @classmethod
    def decrypt(cls, token, ttl=None):
        token = unicode_dados(token)
        return cls.fernet().decrypt(token, ttl)

    @classmethod
    def verify(cls, token, key, ttl=None):
        key = unicode_dados(key)
        return cls.decrypt(token, ttl) == key

    @classmethod
    def fernet(cls):
        if cls._fernet is None:
            return ValueError("Configure o password secret key")
        return cls._fernet


