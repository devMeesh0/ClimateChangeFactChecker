import json
import tensorflow as tf
from flask import Flask, render_template, request
import numpy
from database import Database as DB

app = Flask(__name__)
model = ""
tokenizer = ""
db = ""


def init():
    global model, tokenizer, db
    model = tf.keras.models.load_model('model/my_model.h5')
    file = json.load(open('Resources/tokenizer.json'))
    tokenizer = tf.keras.preprocessing.text.tokenizer_from_json(file)
    db = DB()


@app.route("/")
def index():
    conspiracyArr = db.get_category('conspiracy')
    adhomArr = db.get_category('adhominem')
    unsubArr = db.get_category('unsubstant')

    return render_template("index.html", adhominem_0 = adhomArr[0], adhominem_1=adhomArr[1],
                           adhominem_2=adhomArr[2], adhominem_3=adhomArr[3],
                           adhominem_4=adhomArr[4], adhominem_5=adhomArr[5],
                           unsubstant_0=unsubArr[0], unsubstant_1=unsubArr[1],
                           unsubstant_2=unsubArr[2], unsubstant_3=unsubArr[3],
                           unsubstant_4=unsubArr[4], unsubstant_5=unsubArr[5],
                           conspiracy_0=conspiracyArr[0], conspiracy_1=conspiracyArr[1],
                           conspiracy_2=conspiracyArr[2], conspiracy_3=conspiracyArr[3],
                           conspiracy_4=conspiracyArr[4], conspiracy_5=conspiracyArr[5])


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    data = request.args.get('data')

    if data is None:
        return "Got None"
    else:
        data = preprocess([data])
        prediction = str(numpy.round(model.predict(data)[0][0]))

    return prediction


def preprocess(data):
    global tokenizer
    newData = tokenizer.texts_to_sequences(data)
    newData = tf.keras.preprocessing.sequence.pad_sequences(newData, 70)
    return newData


if __name__ == "__main__":
    init()
    app.run()
