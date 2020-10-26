import pymysql

with open('ip','r') as f:
    arr = f.readlines()[0].split(",")
    IP = arr[0]
    PORT = int(arr[1])
    USER = arr[2]
    PASSWORD= arr[3]
    DB = arr[4]
    
def connect():
    db = pymysql.connect(host=IP,
                     port=PORT,
                     user=USER,
                     password=PASSWORD,
                     db=DB
                    )
    return db

def count_image():
    try: 
        db = connect()
        with db.cursor() as cursor:
            sql = 'SELECT * from image_collector_engine_image;'
            cnt = int(cursor.execute(sql))
            print('# of image:', cnt)
    finally:
        db.close()
    
    return cnt
    
def count_triplet():
    try:
        db = connect()
        with db.cursor() as cursor:
            sql = 'SELECT * from image_collector_engine_tripletimage;'
            cnt = int(cursor.execute(sql))
            print('# of triplet:', cnt)
    finally:
        db.close()
    return cnt
    
def count_pospair():
    try:
        db = connect()
        with db.cursor() as cursor:
            sql = 'SELECT * from image_collector_engine_positivepairimage;'
            cnt = cursor.execute(sql)
            print('# of positive pair:', cnt)
    finally:
        db.close()
    return cnt
    
def count_negpair():
    try:
        db = connect()
        with db.cursor() as cursor:
            sql = 'SELECT * from image_collector_engine_negativepairimage;'
            cnt = cursor.execute(sql)
            print('# of negative pair:', cnt)
    finally:
        db.close()
    return cnt
