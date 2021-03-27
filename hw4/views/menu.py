#!/usr/bin/env python3

import random
from time import time
from datetime import datetime
from flask import Blueprint, render_template, request, redirect, url_for
from werkzeug.exceptions import NotFound

v_menu = Blueprint("v_menu", __name__)

MENU = {
    1: "Чай",
    2: "Кофе",
    3: "Борщ",
    4: "Окрошка",
    5: "Пюре",
    6: "Гречка",
    7: "Макароны",
    8: "Гуляш",
    9: "Котлеты куриные",
    10: "Свинная отбивная",
}

ORDERS = []

@v_menu.route("/", methods=["GET"])
def menu_list():
    return render_template("menu/index.html", menu=MENU)


@v_menu.route("/order/add", methods=["POST"])
def menu_order_add():
    my_order = {
        'id': f'{int(time())}/{int(random.random()*1000)}',
        'time': datetime.now(),
        'address': request.form.get('address'),
        'persons': request.form.get('persons') or 1,
        'food': [],
    }
    for food_id in request.form.getlist('food'):
        if MENU.get(food_id) is None:
            next
        my_order['food'].append(int(food_id))

    ORDERS.append(my_order)
    return render_template("menu/order_done.html", order=my_order)

@v_menu.route("/order/list", methods=["GET"])
def menu_order_list():
    return render_template("menu/order_list.html", orders=ORDERS, menu=MENU)