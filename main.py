import redis
import json
import time

def countTime(function):
    def wrapper(*args, **kwargs):
        start = time.time()
        ans = function(*args, **kwargs)
        end = time.time()
        print(f"To {args[0]} JSON as {function.__name__[:-4]}: {end - start} seconds")
        return ans
    return wrapper

with open('train.json') as dataFile:
    data = json.load(dataFile)

pool = redis.ConnectionPool(host='localhost', port=6379, db=0)
r = redis.Redis(connection_pool=pool)

command = "save"

@countTime
def stringSave(command):
    r.set(name='json_str', value=len(data))

@countTime
def hsetSave(command):
    r.hset(name='json_hset', key='hset', value=len(data))

value = {}
for i in range(len(data)):
    value[i] = i
@countTime
def zsetSave(command):
    r.zadd(name='json_zset', mapping=value)

values=[]
for i in range(len(data)):
    values.append(i)
@countTime
def listSave(command):
    r.lpush('json_list', *values)

stringSave(command)
hsetSave(command)
zsetSave(command)
listSave(command)

command = "get"

@countTime
def stringTake(command):
    r.get(name='json_str')

@countTime
def hsetTake(command):
    r.hget(name='json_hset', key='hset')

@countTime
def zsetTake(command):
    r.zrangebyscore(name='json_zset', min=0, max=r.zadd(name='json_zset', mapping=value))

@countTime
def listTake(command):
    r.lrange(name='json_list', start=0, end=r.lpush('json_list', *values))

stringTake(command)
hsetTake(command)
zsetTake(command)
listTake(command)