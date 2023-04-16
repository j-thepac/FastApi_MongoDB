from MongoDB import DB

def test_getData():
    db=DB("test")
    data=db.get_table("test").find()
    res=[]
    for i in data:res.append(i)
    print (res)


test_getData()
