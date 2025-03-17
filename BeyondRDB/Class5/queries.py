import redis

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

lausanne_id = r.get('idx:city_by_name:Lausanne')

cities_range = r.georadiusbymember('geo:cities', lausanne_id, 100, 'km')

for city_id in cities_range:
    name, population = r.hmget(f'city_id:{city_id}', 'name', 'population')
    print(f"City: {name}, Population: {population}")

