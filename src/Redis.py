import redis
import sys

class Redis:
    client = None
    pubsub = None
    isSub = False
    host = '127.0.0.1'
    password = ''
    # host = '10.19.3.24'
    # password = 'Ccnkbq9V4KDVCyT5FfYpH7ZPhcvisYCf'

    def __init__(self): 
        # self.client = redis.Redis(host=self.host, port=6379, password=self.password)
        self.client = redis.Redis(host=self.host, port=6379)

    def getClient(self):
        return self.client

    def getValue(self, key):
        return self.client.get(key)