
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import pickle
import json


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class model_input(BaseModel):
    
    Edad : int
    Sexo : int
    DolorPecho : int
    PAreposo: int
    Colesterol : int
    GlucemiaAyunas : int
    Reposoecg : int
    FCmax : int
    AnginaEjercicio : int
    STdep : float
    STpend : int
    CA : int
    Thal : int 
    

# cargar el modelo hecho
heart_model = pickle.load(open('heart_model.sav', 'rb'))

@app.post('/Predictor_de_arritmias')
def heart_pred(input_parameters : model_input):
    
    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)
    
    age = input_dictionary['Edad']
    sex = input_dictionary['Sexo']
    cp  = input_dictionary['DolorPecho']
    trestbps = input_dictionary['PAreposo']
    chol = input_dictionary['Colesterol']
    fbs = input_dictionary['GlucemiaAyunas']
    restecg = input_dictionary['Reposoecg']
    thalach = input_dictionary['FCmax']
    exang = input_dictionary['AnginaEjercicio']
    oldpeak = input_dictionary['STdep']
    slope = input_dictionary['STpend']
    ca = input_dictionary['CA']
    thal = input_dictionary['Thal']
    
    
    input_list = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
    
    prediction = heart_model.predict([input_list])
    
    if (prediction[0] == 0):
        return 'Persona saludable'
    else:
        return 'Posible caso de arritmia'


