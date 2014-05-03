#!/usr/bin/python

import json
import sqlite3

conn = sqlite3.connect('gmgdb')
items = json.load(open("gmggames_old.json"))

for i in range(0, len(items)):
	conn.execute("INSERT INTO GAMES (GAMETITLE,GAMELINK,RRP) VALUES (?, ?, ?)", (items[i]['gameTitle'], items[i]['gameLink'], items[i]['rrp']))

conn.commit()
print "Insert operation successful"
conn.close()
