import redis
import csv

r = redis.Redis(host='127.0.0.1', port=6379, decode_responses=True)

with open('BeyondRDB/Class5/test.csv', newline='') as file: 
    reader = csv.DictReader(file, delimiter=',')
    for row in reader: 
        r.hset('city_id:'+row['id'], mapping={
            "name": row['city_ascii'],
            "country": row['country'], 
            "population": row['population']
        })

        r.hset('idx:city_by_name', mapping={
            "city_id": row['id'],
            "city_name": row['city_ascii']
        })