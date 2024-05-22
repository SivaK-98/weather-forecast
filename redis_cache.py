import redis

r = redis.Redis(host='redis-18590.c212.ap-south-1-1.ec2.redns.redis-cloud.com',
                port=18590,
                password='Siva1798*')
data = {"key3": {"temperatuire": "100"}}
r.mset(data)
r.expire(list(data.keys())[0], 300)
print(r.get(list(data.keys())[0]))
