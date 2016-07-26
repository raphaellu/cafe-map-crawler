# -*- coding: utf-8 -*-
from pymongo import MongoClient
from re import *

client = MongoClient()
db = client.restaurants
pudong = db.pudong.find({'title':  {'$regex': '小杨生煎'}})

for restaurant in pudong:
	print restaurant['title']

