import os
import falcon
import sqlalchemy

from sqlalchemy.orm import sessionmaker
from .middleware import SQLAlchemySessionManager
from .resources import TimeSeriesResource


engine = sqlalchemy.create_engine(os.environ['DATABASE_URL'])
session_factory = sessionmaker(bind=engine)

app = falcon.API(middleware=[
    SQLAlchemySessionManager(session_factory)
])
app.add_route('/timeseries', TimeSeriesResource())
