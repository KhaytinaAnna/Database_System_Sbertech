from pymongo import MongoClient
import csv
import pprint


with open('/Users/urijhajtin/Desktop/Database_System_Sbertech/JEOPARDY_CSV.csv', 'r') as input_file:
    answer = [i for i in csv.DictReader(input_file)]
    #print(answer)

client = MongoClient()
db = client['database']
db.posts.delete_many({})
result = db.posts.insert_many(answer)

# Запросы на выборку
print([i for i in db.posts.find({" Value": {"$gt": "$100"}})])
print([i for i in db.posts.find({" Round": "Double Jeopardy!"})])

# Запросы на обновление
db.posts.update_one({" Answer": "Voldemort"}, {"$set": {" Answer": "Tom Riddle"}})
db.posts.update_many({" Category": "3-LETTER WORDS"}, {"$set": {" Answer": "XXX"}})

# Запросы на удаление
db.posts.delete_many({" Air Date": "2000-12-18"})
db.posts.delete_many({"Show Number": "4680"})
db.posts.delete_many({" Round": "Jeopardy!"})
#db.posts.delete_many({" Round": "Double Jeopardy!"})
#db.posts.delete_many({" Round": "Final Jeopardy!"})
#db.posts.delete_many({" Round": "Tiebreaker"})

# Сравним производительность запросов выборки при использовании индекса
print(db.posts.find({" Value": {"$gt": "$100"}}).explain())# 'executionTimeMillisEstimate': 7
db.posts.create_index([(" Value", 1)])
print(db.posts.find({" Value": {"$gt": "$100"}}).explain())# 'executionTimeMillisEstimate': 1