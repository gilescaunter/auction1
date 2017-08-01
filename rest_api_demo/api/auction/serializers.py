from flask_restplus import fields
from rest_api_demo.api.restplus import api

auction_bid = api.model('Auction bid', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of an auction bid'),
    'title': fields.String(required=True, description='Article title'),
    'body': fields.String(required=True, description='Article content'),
    'pub_date': fields.DateTime,
    'vehicle_id': fields.Integer(attribute='vehicle.id'),
    'vehicle': fields.String(attribute='vehicle.id'),
})

pagination = api.model('A page of results', {
    'page': fields.Integer(description='Number of this page of results'),
    'pages': fields.Integer(description='Total number of pages of results'),
    'per_page': fields.Integer(description='Number of items per page of results'),
    'total': fields.Integer(description='Total number of results'),
})

page_of_vehicle_bids = api.inherit('Page of vehicle bids', pagination, {
    'items': fields.List(fields.Nested(auction_bid))
})

vehicle = api.model('Vehicle', {
    'id': fields.Integer(readOnly=True, description='The unique identifier of a Vehicle'),
    'name': fields.String(required=True, description='Vehicle name'),
})

vehicle_with_posts = api.inherit('Auction vehicle with bids', vehicle, {
    'posts': fields.List(fields.Nested(auction_bid))
})
