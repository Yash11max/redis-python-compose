import redis
import time

time.sleep(3)

r = redis.Redis(host='redis', port=6379)

r.set('name', 'Yash')
value = r.get('name')

print("Stored value from Redis:", value.decode())




