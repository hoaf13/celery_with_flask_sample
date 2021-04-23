import redis

red = redis.StrictRedis(host='localhost', port=6379, db=0)

for key in red.keys():
    try:
        k = key.decode('utf-8')
        value = red[k]
        print(k, value)
    except Exception:
        print(k, "khong lay duoc value")
    print()
    print()
# print(red.keys())