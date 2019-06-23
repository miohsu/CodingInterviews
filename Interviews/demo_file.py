"""
读取A文件内容中的key字段，比较他与B文件的md5是否相同
"""
import hashlib


def get_key(filename):
    with open(filename, 'r', encoding='utf8') as fp:
        data = fp.readline()
        while data:
            if data.startswith('key'):
                key = data.split(':')[1].strip()
                return key
            data = fp.readline()
        return None


def get_md5(filename):
    md = hashlib.md5()
    with open(filename, 'r', encoding='utf8') as fp:
        data = fp.read(1024)
        while data:
            md.update(data.encode('utf8'))
            data = fp.read(1024)
        return md.hexdigest()


if __name__ == '__main__':
    key = get_key('files/A')
    print(key)
    md = get_md5('files/B')
    print(md)
    if key == md:
        print('equal')
    else:
        print('Not equal')
