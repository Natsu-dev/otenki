import psycopg2
import os
import json
from datetime import datetime as dt

from dotenv import load_dotenv

load_dotenv()


# connect postgreSQL
conn = psycopg2.connect(dbname=os.getenv('DB_NAME'), user=os.getenv('DB_USER'), password=os.getenv('DB_PASS'), host=os.getenv('DB_HOST'), port=os.getenv('DB_PORT'))


t = open('tenki.json', 'r', encoding='utf-8')
tenki_dic = json.load(t)
timeDefines = []


# excexute sql
cur = conn.cursor()
print(cur)


for n in range(7):
    rd = tenki_dic[0]['week']['reportDatetime']
    reportDatetime = dt.strptime(rd, '%Y-%m-%dT%H:%M:%S+09:00')
    td = tenki_dic[0]['week']['timeSeries'][0]['timeDefines'][n]
    timeDefines = dt.strptime(td, '%Y-%m-%dT%H:%M:%S+09:00')
    weatherCodes = tenki_dic[0]['week']['timeSeries'][0]['areas']['weatherCodes'][n]
    cur.execute('''
        INSERT INTO kushiro (report_datetime, date_define, weather_code)
        VALUES (%s, %s, %s)
        ON CONFLICT (date_define)
        DO UPDATE SET (report_datetime, weather_code, updated_at)
                    = ROW(EXCLUDED.report_datetime, EXCLUDED.weather_code, %s);
        ''', [reportDatetime, timeDefines, weatherCodes, dt.now()])

conn.commit()


#cur.execute('INSERT INTO kushiro (date_define, weather_code) VALUES (%s, %s)', [datetime.datetime.now(), '200'])
#cur.execute('INSERT INTO kushiro (weather_code) VALUES (%s);', 200)
cur.execute("SELECT * FROM kushiro;")
print(cur)
hey = cur.fetchall()
print(hey)

cur.close()
conn.close()