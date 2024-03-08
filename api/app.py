from vetiver import *
import vetiver
import pins
import duckdb
from pandas import get_dummies
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing
import logging


def getData():
    con = duckdb.connect('my-db.duckdb')
    df = con.execute("SELECT * FROM penguins").fetchdf().dropna()
    con.close()
    return df

def defineModel(df):
    X = get_dummies(df[['bill_length_mm', 'species', 'sex']], drop_first = True)
    y = df['body_mass_g']
    model = LinearRegression().fit(X, y)
    logging.info(f"R^2 {model.score(X,y)}")
    logging.info(f"Intercept {model.intercept_}")
    logging.info(f"Columns {X.columns}")
    logging.info(f"Coefficients {model.coef_}")
    return model, X

def getModel(folder, model_name):
    b = pins.board_folder(folder, allow_pickle_read=True)
    v = VetiverModel.from_pin(b, model_name, version = '20240308T141320Z-fdb5a')
    return v





logging.info("App Started")
model = getModel('data/model', 'penguin_model')
app = VetiverAPI(model, check_prototype=True)

app.run()
