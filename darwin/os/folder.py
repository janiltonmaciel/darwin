# -*- coding:utf-8 -*-

# Import system
import os
import sys
from datetime import datetime
from tornado.options import options


def import_folder(folder_name, ends_with=".py", base_path=None):
    if base_path is None:
        base_path = options.root_path

    folder = os.path.join(base_path, folder_name)
    sys.path.insert(0, folder)
    for filename in os.listdir(folder):
        if filename.endswith(ends_with) and not filename.startswith('.'):
            __import__(os.path.splitext(filename)[0], globals(), locals(), [], -1)
