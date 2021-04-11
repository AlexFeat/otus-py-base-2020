from flask import Blueprint, render_template, request
from models import db, Menu, Order


v_menu = Blueprint("v_menu", __name__)

ORDERS = []


@v_menu.route("/", methods=["GET"])
def menu_list():
    menu = Menu.query.all()
    return render_template("menu/index.html", menu_all=menu)


@v_menu.route("/order/add", methods=["POST"])
def menu_order_add():
    order_food = []
    total_cost = 0
    for food_id in request.form.getlist('food'):
        food = Menu.query.filter_by(id=food_id).one_or_none()
        if food is None:
            next
        order_food.append(food.name)
        total_cost = total_cost + food.cost

    new_order = Order(
        count_person=request.form.get('persons') or 1,
        address=request.form.get('address') or '',
        total_cost=total_cost,
        item_list=', '.join(order_food),
    )
    db.session.add(new_order)
    db.session.commit()
    return render_template("menu/order_done.html", order=new_order)


@v_menu.route("/order/list", methods=["GET"])
def menu_order_list():
    orders = Order.query.all()
    menu = Menu.query.all()
    return render_template("menu/order_list.html", orders=orders, menu=menu)
