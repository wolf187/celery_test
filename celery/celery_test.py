import redis
r = redis.Redis(host='127.0.0.1', port=6379)
#print(r.ping())
r.set('foo', 'Bar')
print(r.get('foo'))
