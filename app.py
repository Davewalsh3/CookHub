import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'cookbook'
app.config["MONGO_URI"] = os.getenv('MONGO_URI', 'mongodb://localhost')

mongo = PyMongo(app)


@app.route('/')
@app.route('/FILLERTEXT')
def FILLER_TEXT():
    return render_template("FILLERTEXT",
                           dbcollection=mongo.db.DBNAME.find())


@app.route('/filler_text')
def filler_text():
    return render_template('fillertext.html',
                           dbcollection=mongo.db.collection.find())


@app.route('/insert_FILLERTEXT', methods=['POST'])
def insert_FILLERTEXT():
    FILLERTEXT = mongo.db.collection
    FILLERTEXT.insert_one(request.form.to_dict())
    return redirect(url_for('get_FILLERTEXT'))


@app.route('/FILLERTEXT/<task_id>')
def filler_text(task_id):
    the_task = mongo.db.collection.find_one({"_id": ObjectId(task_id)})
    all_collection = mongo.db.collection.find()
    return render_template('FILLERTEXT.html', task=the_task,
                           collection=all_collection)


@app.route('/FILLERTEXT/<FILLERTEXT>', methods=["POST"])
def FILLERTEXT(task_id):
    collection = mongo.db.collection
    collection.update({'_id': ObjectId(task_id)},
                 {
        'task_name': request.form.get('task_name'),
        'category_name': request.form.get('category_name'),
        'task_description': request.form.get('task_description'),
        'due_date': request.form.get('due_date'),
        'is_urgent': request.form.get('is_urgent')
    })
    return redirect(url_for('get_collection'))


@app.route('/FILLERTEXT/<FILLERTEXT>')
def FILLERTEXT(task_id):
    mongo.db.collection.remove({'_id': ObjectId(task_id)})
    return redirect(url_for('FILLERTEXT'))


@app.route('/FILLERTEXT')
def FILLERTEXT():
    return render_template('collection.html',
                           collection=mongo.db.collection.find())


@app.route('/FILLERTEXT/<FILLERTEXT>')
def FILLERTEXT(category_id):
    mongo.db.collection.remove({'_id': ObjectId(category_id)})
    return redirect(url_for('collection'))


@app.route('/collection/<collection>')
def FILLERTEXT(category_id):
    return render_template('FILLERTEXT.html',
                           collection=mongo.db.collection.find_one
                           ({'_id': ObjectId(category_id)}))


@app.route('/FILLERTEXT/<FILLERTEXT', methods=['POST'])
def FILLERTEXT(category_id):
    mongo.db.collection.update(
        {'_id': ObjectId(category_id)},
        {'category_name': request.form.get('category_name')})
    return redirect(url_for('FILLERTEXT'))


@app.route('/FILLERTEXT', methods=['POST'])
def FILLERTEXT():
    category_doc = {'category_name': request.form.get('category_name')}
    mongo.db.cOLLECTIONinsert_one(category_doc)
    return redirect(url_for('FILLERTEXT'))


@app.route('/FILLERTEXT')
def FILLERTEXT():
    return render_template('FILLERTEXT.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)