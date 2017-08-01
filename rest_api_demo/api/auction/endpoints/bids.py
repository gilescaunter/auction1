from flask import request
from flask_restplus import Resource
from rest_api_demo.api.auction.business import create_bid_post, update_bid, delete_bid
from rest_api_demo.api.auction.serializers import auction_bid, page_of_vehicle_bids
from rest_api_demo.api.auction.parsers import pagination_arguments
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Post

ns = api.namespace('auction/bids', description='Operations related to auction bids')


@ns.route('/')
class BidsCollection(Resource):

    @api.expect(pagination_arguments)
    @api.marshal_with(page_of_vehicle_bids)
    def get(self):
        """
        Returns list of vehicle bids.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        bids_query = Bids.query
        bids_page = bids_query.paginate(page, per_page, error_out=False)

        return bids_page

    @api.expect(auction_bid)
    def post(self):
        """
        Creates a new vehicle bid.
        """
        create_vehicle_bid(request.json)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Post not found.')
class PostItem(Resource):

    @api.marshal_with(vehicle_bid)
    def get(self, id):
        """
        Returns a vehciel bid.
        """
        return Bid.query.filter(Bid.id == id).one()

    @api.expect(vehicle_bid)
    @api.response(204, 'Post successfully updated.')
    def put(self, id):
        """
        Updates a vehicle bid.
        """
        data = request.json
        update_bid(id, data)
        return None, 204

    @api.response(204, 'Bid successfully deleted.')
    def delete(self, id):
        """
        Deletes vehicle bid.
        """
        delete_post(id)
        return None, 204


@ns.route('/archive/<int:year>/')
@ns.route('/archive/<int:year>/<int:month>/')
@ns.route('/archive/<int:year>/<int:month>/<int:day>/')
class BidsArchiveCollection(Resource):

    @api.expect(pagination_arguments, validate=True)
    @api.marshal_with(page_of_vehicle_bids)
    def get(self, year, month=None, day=None):
        """
        Returns list of blog posts from a specified time period.
        """
        args = pagination_arguments.parse_args(request)
        page = args.get('page', 1)
        per_page = args.get('per_page', 10)

        start_month = month if month else 1
        end_month = month if month else 12
        start_day = day if day else 1
        end_day = day + 1 if day else 31
        start_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, start_month, start_day)
        end_date = '{0:04d}-{1:02d}-{2:02d}'.format(year, end_month, end_day)
        bids_query = Bids.query.filter(Bid.pub_date >= start_date).filter(Bid.pub_date <= end_date)

        bids_page = bids_query.paginate(page, per_page, error_out=False)

        return bids_page
