from flask import request
from flask_restplus import Resource
from rest_api_demo.api.auction.business import create_vehicle, delete_vehicle, update_vehicle
from rest_api_demo.api.auction.serializers import vehicle, vehicle_with_posts
from rest_api_demo.api.restplus import api
from rest_api_demo.database.models import Vehicle

ns = api.namespace('auction/vehicles', description='Operations related to auction vehicles')
#category = vehicles
#posts = bids

@ns.route('/')
class VehicleCollection(Resource):

    @api.marshal_list_with(vehicle)
    def get(self):
        """
        Returns list of blog categories.
        """
        categories = Vehicles.query.all()
        return categories

    @api.response(201, 'Vehicle successfully created.')
    @api.expect(vehicle)
    def post(self):
        """
        Creates a new blog category.
        """
        data = request.json
        create_vehicle(data)
        return None, 201


@ns.route('/<int:id>')
@api.response(404, 'Vehicle not found.')
class VehicleItem(Resource):

    @api.marshal_with(vehicle_with_posts)
    def get(self, id):
        """
        Returns a vehicle with a list of posts.
        """
        return Vehicle.query.filter(Vehicle.id == id).one()

    @api.expect(vehicle)
    @api.response(204, 'Vehicle successfully updated.')
    def put(self, id):
        """
        Updates a vehicle.

        Use this method to change a vehicle.

        * Send a JSON object with the new name in the request body.

        ```
        {
          "name": "New Vehicle"
        }
        ```

        * Specify the ID of the vehicle to modify in the request URL path.
        """
        data = request.json
        update_vehicle(id, data)
        return None, 204

    @api.response(204, 'Vehicle successfully deleted.')
    def delete(self, id):
        """
        Deletes vehicle.
        """
        delete_vehicle(id)
        return None, 204
