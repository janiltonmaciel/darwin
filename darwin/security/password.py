# -*- coding:utf-8 -*-

# import system
import random
import string
from passlib.hash import pbkdf2_sha256

# import local
from darwin.security import unicode_dados


class SecurityPassword(object):
    ROUNDS = 10000

    @staticmethod
    def encrypt(password):
        password = unicode_dados(password)
        return pbkdf2_sha256.encrypt(password, rounds=SecurityPassword.ROUNDS)

    @staticmethod
    def verify(password, password_verify):
        password = unicode_dados(password)
        return pbkdf2_sha256.verify(password, password_verify)

    @staticmethod
    def generate(length_password=8):
        return ''.join(random.choice(string.ascii_letters+string.digits) for _ in range(length_password))
