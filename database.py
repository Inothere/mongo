from settings import DATABASES as db_config
from pymongo import MongoClient
from functools import wraps


class Config(object):
    uri = 'mongodb://{}:{}'.format(db_config.get('host'), db_config.get('port'))
    client = None
    db = None


def conn_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            client = MongoClient(Config.uri)
            Config.db = client[db_config.get('name')]
            return func(*args, **kwargs)
        finally:
            if Config.client:
                Config.client.close()
                Config.client = None
            Config.db = None
    return wrapper


@conn_required
def test_insert():
    r = Config.db.user.insert_one({
        '名字': 'chendi',
        'id': 'S51498'
    })
    print(r.inserted_id)


@conn_required
def test_fetch():
    cursor = Config.db.Price.find()
    for doc in cursor:
        print(doc)

if __name__ == '__main__':
    test_fetch()
