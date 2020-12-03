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
@app.route ("/api/v1.0/precipitation")
def precipitation():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date > '2016-08-23').\
        order_by(Measurement.date.desc()).all()
    session.close()

    prcp_query = []
    for prcp in results:
        prcp_dict = {}
        prcp_dict["date"] = prcp.date
        prcp_dict["prcp"] = str(prcp)
        prcp_query.append(prcp_dict)
    return jsonify(prcp_query)

#Route /api/v1.0/stations
@app.route("/api/v1.0/stations")
def stations():
    session = Session(engine)
    results = session.query(Stations.station).all()
    session.close()
    all_stations=list(np.ravel(results))
    print(all_stations)
    return jsonify(all_stations)

# #Route /api/v1.0/tobs
@app.route("/api/v1.0/tobs")
def tobs():
    session = Session(engine)
    results = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date > '2016-08-23').\
        order_by(Measurement.date.desc()).all()
    session.close()
    all_dates = list(np.ravel(results))
    return jsonify(all_dates)

# # #Route /api/v1.0/<start> 
@app.route("/api/v1.0/<start>")
def start(start):
    session = Session(engine)
    def calc_temps(start_date):
        calc_temps('2017-03-01')
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start_date).all().\
            order_by(Measurement.date.desc()).all()
    session.close()
    start_date = list(np.ravel(results))
    return jsonify(start_date) 

# # #Route /api/v1.0/<start>/<end>
@app.route("/api/v1.0/<start>/<end>")
def st_end (start, end):
    session = Session(engine)
    def calc_temps(start_date, end_date):
        calc_temps('2017-03-01', '2017-03-15')
        results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start_date).filter(Measurement.date <= end_date).all()
    session.close()
    date_temp = list(np.ravel(results))
    return jsonify(date_temp)   

if __name__ == '__main__':
    app.run(debug=True)
