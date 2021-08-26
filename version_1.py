import pymongo

db_client = pymongo.MongoClient('db', 27017)
db = db_client["SmartDesign"]
cl = db["items"]

a = {'_id': 1, 'title': 'Asus', 'desc': 'Superbook',
     'parameters': [{'RAM': '16GB', 'GPU': '1050TI', 'CPU': 'Core i7 8th Gen', 'price': 73000}]}
b = {'_id': 2, 'title': 'Dell', 'desc': 'Megarbook',
     'parameters': [{'RAM': '32GB', 'GPU': '1060TI', 'CPU': 'Core i5 9th Gen', 'price': 98000}]}
c = {'_id': 3, 'title': 'Acer', 'desc': 'Ultrabook',
     'parameters': [{'RAM': '8GB', 'GPU': '1050', 'CPU': 'Core i5 7th Gen', 'price': 65000}]}
d = {'_id': 4, 'title': 'Acer', 'desc': 'Nanobook',
     'parameters': [{'RAM': '24GB', 'GPU': '1080', 'CPU': 'Core i5 8th Gen', 'price': 82000}]}
e = {'_id': 5, 'title': 'ASUS', 'desc': 'Mybook',
     'parameters': [{'RAM': '32GB', 'GPU': '1080TI', 'CPU': 'Core i5 8th Gen', 'price': 125000}]}
f = {'_id': 6, 'title': 'DELL', 'desc': 'Notebook',
     'parameters': [{'RAM': '24GB', 'GPU': '1080', 'CPU': 'Core i7 8th Gen', 'price': 118000}]}
cl.insert_many([a, b, c, d, e, f])


def find_by_id(id):
    item = cl.find_one({'_id': id})
    return item


def find_all():
    items = cl.find()
    return items


def find_by_parameter(param, value, flag: bool = False):
    if flag:

        items = cl.find({"parameters": {"$elemMatch": {param: {"$gt": value}}}})
    else:
        items = cl.find({"parameters": {"$elemMatch": {param: {"$lt": value}}}})

    return items


def find_by_name(title):
    items = cl.find({"title": {"$regex": title, "$options": "$i"}})
    return items
