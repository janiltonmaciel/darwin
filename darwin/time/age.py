# -*- coding:utf-8 -*-

# Import system
import re
from datetime import time

re_apat = re.compile("([0-9]+([.][0-9]+)?)\s*([dhms])?\s*$")

def parse_age(age):
    """
    Uso:
      parse_age("8s")  >> 1*8   = 8s
      parse_age("5m")  >> 5*60  = 300s
      parse_age("1h")  >> 1*60*60 = 3600s
      parse_age("1d")  >> 1*24*60*60 = 86400s
    """
    mat = re_apat.match(age)
    if mat is None:
        raise ValueError("invalid age spec: " + age)

    n = int(mat.group(1))
    units = mat.group(3) or "s"
    if units == "s":
        pass
    elif units == "m":
        n = n * 60
    elif units == "h":
        n = n * 60*60
    elif units == "d":
        n = n * 24*60*60

    return n


def timedelta_to_time(value):
    seconds = value.seconds
    minutes = seconds / 60
    return time(minutes / 60, minutes % 60, seconds - minutes * 60, value.microseconds)
