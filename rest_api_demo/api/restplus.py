import traceback

from flask_restplus import Api
from sqlalchemy.orm.exc import NoResultFound

from rest_api_demo import settings

api = Api(version='0.1', title='My Auction Test Mock API',
          description='Simple Auction Mock using ideas from web')


@api.errorhandler
def default_error_handler(e):
    message = 'An unhandled exception occurred.'
    log.exception(message)

    if not settings.FLASK_DEBUG:
        return {'message': message}, 500


@api.errorhandler(NoResultFound)
def database_not_found_error_handler(e):
    log.warning(traceback.format_exc())
    return {'message': 'A database result was required but none was found.'}, 404
