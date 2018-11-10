import pymongo



def main():
    client = pymongo.MongoClient('localhost')
    db = client['newtestdb']
    collection = db['table']
#    insert(collection)
    update(collection)
    find(collection)




def insert(collection):
    collection.insert({"name":"Bob","age":"21","addres":"shenzhen","hobbies":["吃饭","睡觉","打豆豆"]})
    collection.insert({"name":"Alice","age":"18", "addres": "beijing", "hobbies": ["读书", "跑步", "弹吉他"]})

def update(collection):
    #{"hobbies":["听歌","撸猫","打data"]}
    bob = collection.find_one({"name": "Bob"})
    print(bob)
    bob["age"] = "25"
    bob["addres"] = "shanghai"
    bob["hobbies"] = ["听歌","撸猫","打data"]
    collection.update({"name":bob["name"]},bob)

def remove(collection):
    collection.remove({"name":"Bob"})

def find(collection):
    alice = collection.find_one({"name": "Alice"})
    bob = collection.find_one({"name": "Bob"})
    all = collection.find({})
    for i in all:
        print(i)

if __name__ == '__main__':
    main()