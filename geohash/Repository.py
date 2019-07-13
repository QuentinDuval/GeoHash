import sqlalchemy as db

from geohash import Map
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
                    db.Column('id', db.Integer, primary_key=True),
                    db.Column('name', db.String, unique=True),
                    db.Column('x', db.Float, index=True),
                    db.Column('y', db.Float, index=True),
                    db.Column('hash', db.String, index=True)
                )
                metadata.create_all(self.engine)

    def add_character(self, name: str, x: float, y: float, map: Map):
        with self.engine.connect() as connection:
            metadata = db.MetaData()
            location = db.Table(self.LOCATION_TABLE, metadata, autoload=True, autoload_with=self.engine)
            statement = db.insert(location).values(name=name, x=x, y=y, hash=map.get_geohash(x, y))
            connection.execute(statement)

    def all_characters(self):
        with self.engine.connect() as connection:
            metadata = db.MetaData()
            location = db.Table(self.LOCATION_TABLE, metadata, autoload=True, autoload_with=self.engine)
            query = db.select([location.c.name])
            result_proxy = connection.execute(query)
            return [row[0] for row in result_proxy.fetchall()]

    def find_at(self, x: float, y: float):
        with self.engine.connect() as connection:
            metadata = db.MetaData()
            location = db.Table(self.LOCATION_TABLE, metadata, autoload=True, autoload_with=self.engine)
            query = db.select([location.c.name]).where(location.c.x == x and location.c.y == y)
            result_proxy = connection.execute(query)
            return [row[0] for row in result_proxy.fetchall()]

    def find_at_hash(self, x: float, y: float, map: Map):
        h = map.get_geohash(x, y)
        with self.engine.connect() as connection:
            metadata = db.MetaData()
            location = db.Table(self.LOCATION_TABLE, metadata, autoload=True, autoload_with=self.engine)
            query = db.select([location]).where(location.c.hash == h)
            result_proxy = connection.execute(query)
            return [row[1] for row in result_proxy.fetchall() if row[2] == x and row[3] == y]
