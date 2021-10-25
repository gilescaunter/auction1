from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from auction_demo.database.models import Bid, Vehicle  # noqa
    db.drop_all()
    db.create_all()
