import numpy as np
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
import datetime as dt

#Create engine
engine = engine = create_engine("sqlite:///Resources/hawaii.sqlite")

#Reflect database
Base = automap_base()
Base.prepare(engine, reflect = True)

#Classes
Measurement = Base.classes.measurement
Stations = Base.classes.station

#Session
session = Session(engine)
app = Flask(__name__)

#Route /

#Route /api/v1.0/precipitation
#Route /api/v1.0/stations
#Route /api/v1.0/tobs
#Route /api/v1.0/<start> and /api/v1.0/<start>/<end>
