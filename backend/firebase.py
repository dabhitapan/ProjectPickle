import pyrebase

config = {
  "apiKey": "AIzaSyBlMHINDnByxWSKEwzdGV4a7QVf3833W2Y",
  "authDomain": "projectpicle.firebaseio.com",
  "databaseURL": "https://projectpicle.firebaseio.com/",
  "storageBucket": "projectpicle.appspot.com"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()
#db.child("fridge_itmes").child("Tomato Ketchup")
#db.child("Tomatoes").push({"quantity": 1000})

#consumer part
db.child("consumers").child("userID").update({"name": "Yeet", "phone" : "123456789", "address" : "123, ABC"})
db.child("consumers").child("userID").child("previous_orders").child("order1").update({"item_name": "Yeet", "status" : "delivered", "firm_name" : "ABC"})
db.child("consumers").child("userID").child("previous_orders").child("order1").child("items").child("item1").update({"item_name": "Yeet", "price" : "10"})

#seller part
db.child("sellers").child("firmID").update({"name": "Yeet", "phone" : "123456789", "address" : "123, ABC"})
db.child("sellers").child("firmID").child("items").child("item1").update({"item_name": "Yeet", "price" : "10", "img_ur
l" : "..."})
db.child("sellers").child("firmID").child("orders").child("order1").update({"customer_name": "Yeet", "customer_address" : "123, ABC", "phone" : "123456", "status" : "active"})
