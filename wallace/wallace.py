from . import models
from .db import Base, engine, db


class Wallace(object):

    def __init__(self, drop_all=False):
        """Initialize Wallace."""
        # initialize the database
        if drop_all:
            Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

    def add_node(self, name, type):
        """Add a new node. The 'type' should be either "participant",
        "source", or "filter".

        """
        node = models.Node(name, type)
        db.add(node)
        db.commit()
        return node

    @property
    def nodes(self):
        """All nodes in the database."""
        return db.query(models.Node).all()

    def add_participant(self, name):
        """Add a new participant node."""
        return self.add_node(name, "participant")

    @property
    def participants(self):
        """All participants in the database."""
        return db.query(models.Node).filter_by(type="participant").all()

    def add_source(self, name):
        """Add a new source node."""
        return self.add_node(name, "source")

    @property
    def sources(self):
        """All source nodes in the database."""
        return db.query(models.Node).filter_by(type="source").all()

    def add_filter(self, name):
        """Add a new filter node."""
        return self.add_node(name, "filter")

    @property
    def filters(self):
        """All filter nodes in the database."""
        return db.query(models.Node).filter_by(type="filter").all()

    def add_vector(self, origin, destination):
        """Add a new vector from 'origin' to 'destination'."""
        vector = models.Vector(origin, destination)
        db.add(vector)
        db.commit()
        return vector

    @property
    def vectors(self):
        """All vectors in the database."""
        return db.query(models.Vector).all()

    def get_vectors(self, origin=None, destination=None):
        """Get the list of vectors, optionally filtered by their origin and/or
        destination.

        """
        if origin and destination:
            return db.query(models.Vector).filter_by(
                origin_id=origin.id, destination_id=destination.id).all()
        elif origin:
            return db.query(models.Vector).filter_by(
                origin_id=origin.id).all()
        elif destination:
            return db.query(models.Vector).filter_by(
                destination_id=destination.id).all()
        else:
            return db.query(models.Vector).all()

    def add_meme(self, origin, contents=None):
        """Add a new meme, created by 'origin'."""
        meme = models.Meme(origin, contents=contents)
        db.add(meme)
        db.commit()
        return meme

    @property
    def memes(self):
        """All memes in the database."""
        return db.query(models.Meme).all()

    @property
    def transmissions(self):
        """All transmissions in the database."""
        return db.query(models.Transmission).all()
