#! python3
# -*- coding:utf-8 -*-

__author__ = 'nico'

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('base.html')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/test')
def test():
    fish = 'April fish'

    item = {
        'price': 10,
        'energy': '1000 cal',
    }

    fruit_list = [
        'apple',
        'pear',
        'banana',
        'watermelon',
        'melon'
    ]

    return render_template('test.html',
                           fish=fish,
                           item=item,
                           fruit_list=fruit_list
                           ), 200


if __name__ == '__main__':
    app.run()
