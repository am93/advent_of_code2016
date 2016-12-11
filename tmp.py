from pymongo import MongoClient
import random, string
from timeit import default_timer as timer

client = MongoClient('192.168.1.149', 27017)
collection = client.test.advent
keys = []

#t1 = timer()
for x in range(100):
     key = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(41))
#    collection.insert_one({'key': key})
#    if x % 1000 == 0:
     keys.append(key)
#t2 = timer()
#print("Time: {0} seconds".format(t2 -t1))

t3 = timer()
for x in keys:
    collection.find({'key': x}).limit(1)
    collection.find({'key': 'cungalunga'}).limit(1)
t4 = timer()
print("Time: {0} seconds".format(t4 -t3))