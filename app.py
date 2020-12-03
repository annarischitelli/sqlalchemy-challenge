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
@app.route ("/")
def main ():
    "All paths available."
    return(
        f"Routes:<br>"
        f"/api/v1.0/precipitation<br>"
        f"/api/v1.0/stations<br>"
        f"/api/v1.0/tobs<br>"
        f"/api/v1.0/<start><br>"
        f"/api/v1.0/<start>/<end>"
    )

# #Route /api/v1.0/precipitation
# @app.route ("/api/v1.0/precipitation")
# def precipitation():
#     session = Session(engine)
#     precip = session.query(func.strftime("%Y-%m-%d", Measurement.date), Measurement.prcp).\
#     filter(func.strftime("%Y-%m-%d", Measurement.date)>= dt.date(2016, 8, 23)).all()
#     session.close()


#Route /api/v1.0/stations
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Stations.id).all()
    session.close()
    all_stations=list(np.ravel(results))
    print(all_stations)
    return jsonify(all_stations)

# #Route /api/v1.0/tobs
# @app.route("/api/v1.0/tobs")
# def tobs():
    


# # #Route /api/v1.0/<start> 
# # @app.route("/api/v1.0/<start> ")
# # def start(start):
    

# # #Route /api/v1.0/<start>/<end>
# # @app.route("/api/v1.0/<start>/<end>")
# # def st_end (start, end):

if __name__ == '__main__':
    app.run(debug=True)
