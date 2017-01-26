"""
File IO utils
"""

import os
import json
import io


def write2file(s_io, file_path, mode):
    full_path = os.path.abspath(file_path)
    dir_name = os.path.dirname(full_path)
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)
    with open(file_path, mode) as f:
        f.write(s_io.getvalue())


def save2json(dict_, file_path):
    s_io = io.StringIO()
    json.dump(dict_, s_io)
    write2file(s_io, file_path, 'w')
