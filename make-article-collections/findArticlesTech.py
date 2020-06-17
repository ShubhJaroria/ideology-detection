import pymongo
from pymongo import MongoClient
from collections import Counter

# ---------- Fixed Params ------------
art_client = MongoClient('mongodb://10.237.26.159:27017/')
client = MongoClient('mongodb://10.237.26.159:27017/')
art_db = art_client['media-db']
my_db = client['media-db']
# -----------------------------------

print("Finding articles...")

# Enter the base set of keywords in the regex below, separated by |
# |telecommunication network|technicians|computing|Telecommunication|technology|transformational AI|
# Smart Cities|Smart Mobility|TRAI|DoT|scientific research|programming|algorithms|Information and Broadcasting|

x = art_db.articles.find({'$and':[{'text': {'$regex': ' Artificial Intelligence|Internet of Things|\
	net neutrality|Information Technology|Internet Services ', '$options': 'i'}}]},no_cursor_timeout=True)

# x = art_db.articles.find({'$and':[{'text': {'$regex': ' Digital India|Artificial Intelligence|\
# 	AI|technological|digitisation|digitization|Internet of Things|internet connectivity|\
# 	Social Media|net neutrality|data protection|data privacy|Information Technology|Information Security|\
# 	Personal Data Protection|Internet Shutdown|Internet Services ', '$options': 'i'}}]},
#                      no_cursor_timeout=True)

#articles = input('Enter name of collection to store resultant articles: ')
articles = "tech-all"

print("Storing articles now...")
coll = my_db[articles]
art_map = {}
count = 0

for art in x:
	count+=1
	print('Doing for '+str(count)+' relevant article')
	url = art['articleUrl']
	if url not in art_map:
		art_map[url] = 1
		coll.insert_one(art)
	# try:
	# 	cat = str(art['category'])
	# 	print('category attribute found')
	# 	if url not in art_map:
	# 		art_map[url] = 1
	# 		coll.insert_one(art)
	# except KeyError as err1:
	# 	print('category attribute not found')
		
	# try:
	# 	lis = art['categories']
	# 	print('categories attribute found')
	# 	if url not in art_map and 'OPINION' in lis:
	# 		art_map[url] = 1
	# 		coll.insert_one(art)
	# except KeyError as err2:
	# 	print('categories attribute not found')
	# 