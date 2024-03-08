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





logging.info("App Started")
df = getData()
model, X = defineModel(df) 
v = VetiverModel(model, model_name='penguin_model', prototype_data=X)
app = VetiverAPI(v, check_prototype=True)

