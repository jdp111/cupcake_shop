from unittest import result
from flask import Flask, render_template, redirect, request, flash
from models import Cupcake, db, connect_db
from flask.json import jsonify



app = Flask(__name__)
app.config['SECRET_KEY'] = "cupcakesarejustlittlecakeslikewhatsthepoint"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route('/api/cupcakes')
def getCupcakes():
    allcakes = db.session.query(Cupcake)
    result = jsonify({"cupcakes":[ cake.parse()for cake in allcakes]} )
    return (result, 200)

@app.route('/api/cupcakes/<int:cupcakeId>')
def getOneCake(cupcakeId):
    singleCake = Cupcake.query.get_or_404(cupcakeId)
    result = jsonify({"cupcake": singleCake.parse()})
    return (result,200)

@app.route('/api/cupcakes', methods = ['POST'])
def createCake():   
    data = request.json
    newFlavor = data['flavor']
    newSize = data['size']
    newRating = data['rating']
    newImage = data.get('image',"https://tinyurl.com/demo-cupcake")

    newCake = Cupcake(flavor=newFlavor, size=newSize, rating=newRating, image=newImage)
    db.session.add(newCake)
    db.session.commit()
    
    return (jsonify({"cupcake": newCake.parse()}), 201)

@app.route('/api/cupcakes/<int:cupcakeId>',methods = ['PATCH'])
def patchCake(cupcakeId):
    newData = request.json
    oldCake = Cupcake.query.get_or_404(cupcakeId)
    
    oldCake.flavor = newData.get('flavor', oldCake.flavor)
    oldCake.size = newData.get('size', oldCake.size)
    oldCake.rating = newData.get('rating', oldCake.rating)
    oldCake.image = newData.get('image', oldCake.image)
    db.session.commit()
    result = jsonify({"cupcake" : oldCake.parse()})

    return (result,200)

@app.route('/api/cupcakes/<int:cupcakeId>', methods = ['DELETE'])
def deleteCake(cupcakeId):
    oldCake = Cupcake.query.get_or_404(cupcakeId)
    db.session.delete(oldCake)
    db.session.commit()
    result = jsonify({"cupcake":oldCake.parse()})
    return (result,200)


@app.route('/')
def home():
    return render_template('home.html')