import redis
import csv

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

with open('BeyondRDB/Class5/worldcities.csv', newline='') as file: 
    reader = csv.DictReader(file, delimiter=',')
    for row in reader: 
        r.hset('city_id:'+row['id'], mapping={
            "name": row['city_ascii'],
            "country": row['country'], 
            "population": row['population']
        })

        r.set(f'idx:city_by_name:{row["city_ascii"]}', row['id'])

        r.geoadd('geo:cities', (float(row['lng']), float(row['lat']), row['id']))


