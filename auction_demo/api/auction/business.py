from auction_demo.database import db
from auction_demo.database.models import Bid, Vehicle


def create_auction_bid(data):
    title = data.get('title')
    body = data.get('body')
    vehicle_id = data.get('vehicle_id')
    vehicle = Vehicle.query.filter(Vehicle.id == vehicle_id).one()
    bid = Bid(title, body, vehicle_id)
    db.session.add(bid)
    db.session.commit()


def update_bid(post_id, data):
    bid = Bid.query.filter(Bid.id == bid_id).one()
    bid.title = data.get('title')
    bid.body = data.get('body')
    vehicle_id = data.get('vehicle_id')
    bid.category = Vehicle.query.filter(Vehicle.id == vehicle_id).one()
    db.session.add(vehicle)
    db.session.commit()


def delete_bid(bid_id):
    bid = Bid.query.filter(Bid.id == bid_id).one()
    db.session.delete(bid)
    db.session.commit()


def create_vehicle(data):
    name = data.get('name')
    vehicle_id = data.get('id')

    vehicle = Vehicle(name)
    if vehicle_id:
        vehicle.id = vehicle_id

    db.session.add(vehicle)
    db.session.commit()


def update_vehicle(vehicle_id, data):
    vehicle = Vehicle.query.filter(Vehicle.id == vehicle_id).one()
    vehicle.name = data.get('name')
    db.session.add(vehicle)
    db.session.commit()


def delete_vehicle(vehicle_id):
    vehicle = Vehicle.query.filter(Vehicle.id == vehicle_id).one()
    db.session.delete(vehicle)
    db.session.commit()
