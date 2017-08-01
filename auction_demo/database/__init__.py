from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def reset_database():
    from auction_demo.database.models import Post, Vehicles  # noqa
    db.drop_all()
    db.create_all()
