# This Python file uses the following encoding: utf-8

import os
from bottle import *
import numpy
from keras.preprocessing import image
from keras.models import load_model


@route('/')
def index():
    return "Getting started"

@route("/upload", method="POST")
def test():
    upload = request.files.get("upload")
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    print(type(upload))
    img = image.load_img('test.png', target_size=(28, 28), grayscale=True, )
    x = image.img_to_array(img)
    # Инвертируем и нормализуем изображение
    x = 255 - x
    x /= 255
    x = x.reshape(784)
    x = numpy.expand_dims(x, axis=0)
    myModel = load_model('model.h5')
    print(numpy.argmax(myModel.predict(x)))
    return str(numpy.argmax(myModel.predict(x)))



@route("/test")
def test():
    im_path = "test.png"
    img = image.load_img(im_path, target_size=(28, 28), grayscale=True, )
    x = image.img_to_array(img)
    # Инвертируем и нормализуем изображение
    x = 255 - x
    x /= 255
    x = x.reshape(784)
    x = numpy.expand_dims(x, axis=0)
    myModel = load_model('model.h5')
    # prediction = myModel.predict(x)
    print(numpy.argmax(myModel.predict(x)))
    return str(numpy.argmax(myModel.predict(x)))

    # final = numpy.argmax(prediction)
    # return final


# <======== CONNECTIONS =========>

@route("/form")
def index():
    return static_file('index.html', root='.')

@route("/app")
def app():
    return static_file("app.py", root=".")

run(host="0.0.0.0", port=os.environ.get('PORT', 5000))
