from flask_sqlalchemy import SQLAlchemy
"""Models for pets."""


db = SQLAlchemy()

DEFAULT_IMAGE_URL = "data:image/png;base64,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"


def connect_db(app):
    db.app = app
    db.init_app(app)


# define models

class Pet(db.Model):
    """ Pet model """
    __tablename__ = "pets"

    def __repr__(self):
        p = self
        return f"< Pet id={p.id} name={p.name} image_url={p.image_url} age={p.age} available={p.available}>"
        
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    species = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.Text, nullable=False, default=DEFAULT_IMAGE_URL)
    age = db.Column(db.Integer, nullable=True)
    notes = db.Column(db.Text, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

