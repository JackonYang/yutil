import hashlib


def md5(s):
    m = hashlib.md5()
    m.update(s.encode('utf8'))
    return m.hexdigest()
