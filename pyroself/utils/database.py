import redis

db = redis.StrictRedis(host='localhost', port=6379, db=1,charset='UTF-8', decode_responses=True)

def seted(a,b):
    db.set(a,b)

def delete(a):
    db.dalete(a)
