# -*- coding:utf-8 -*-

# Import system
from datetime import datetime


def create_date(data_str):
    return datetime.strptime(data_str, '%Y-%m-%d').date()

def create_date_month(mes_str):
    return datetime.strptime(mes_str, '%Y-%m').date()
