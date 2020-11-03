import pandas as pd
import uvicorn
import sklearn
import joblib
from fastapi import FastAPI

app = FastAPI()
model = joblib.load("modelIRIS.pkl")

@app.get("/")
async def root():
    return {"message": "Hello World"}

# Using Post
@app.get('/predict/{sepal_length}/{sepal_width}/{petal_length}/{petal_width}')
async def predict(sepal_length,sepal_width,petal_length,petal_width):
    irisX = pd.DataFrame({
    'sepal_length': [float(sepal_length)],
    'sepal_width': [float(sepal_width)],
    'petal_length': [float(petal_length)],
    'petal_width': [float(petal_width)]
    })
    Y_pred = model.predict_proba(irisX)[0]
    
    if Y_pred[0] > Y_pred[1] and Y_pred[0]> Y_pred[2]:
        return {"orig_name":'setosa',"prediction":Y_pred[0]}
    elif Y_pred[1] > Y_pred[0] and Y_pred[1]> Y_pred[2] :
        return {"orig_name":'versicolor',"prediction":Y_pred[1]}
    else :
        return {"orig_name":'virginica',"prediction":Y_pred[2]}
        
if __name__ == '__main__' :
    uvicorn.run(app,host="127.0.0.1",port="8000")