import sqlalchemy as db
from geohash.Configuration import *


class Repository:
    LOCATION_TABLE = 'location'

    def __init__(self, configuration: Configuration):
        self.engine = self._init_engine(configuration)

    def _init_engine(self, configuration: Configuration):
        with open(configuration.postgres_secrets) as secrets:
            secrets = secrets.read().strip()
            # db.create_engine('dialect+driver://user:pass@host:port/db')
            return db.create_engine("postgresql://{secrets}@{postgres_host}/geohash".format(
                secrets=secrets,
                postgres_host=configuration.postgres_host))

    def init_datamodel(self):
        with self.engine.connect():
            metadata = db.MetaData()
            if self.LOCATION_TABLE not in metadata:
                db.Table(
                    self.LOCATION_TABLE,
                    metadata,
                    db.Column('id', db.String, primary_key=True),
                    db.Column('name', db.String),
                    db.Column('x', db.Integer),
                    db.Column('y', db.Integer),
                    db.Column('hash', db.String)
                )
                metadata.create_all(self.engine)

