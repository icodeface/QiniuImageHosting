# -*- coding: utf-8 -*-
"""
__author__ = 'CodeFace'
"""
import os
import hashlib
import qiniu
from config import QINIU_ACCESS_KEY, QINIU_SECRET_KEY, ALLOWED_EXTENSIONS, BUCKET_NAME, PREFIX
import time
import random
import string

q = qiniu.Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)


def push(file, file_name):
    suffix = os.path.splitext(file_name)[1]
    key = PREFIX + generate_name() + suffix
    token = q.upload_token(BUCKET_NAME, key, 3600)
    ret, info = qiniu.put_data(token, key, file)
    return ret, info


def generate_name():
    m = hashlib.md5()
    t = str(time.time()) + ''.join(random.choice(string.ascii_letters) for _ in range(4))
    m.update(t.encode())
    return m.hexdigest()


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


if __name__ == '__main__':
    print(generate_name())
