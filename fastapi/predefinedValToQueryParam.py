from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class CountryEnum(str, Enum):
    India = "India"
    China = "China"
    Russia = "Russia"

# employees information
emps = {
    1 : {
        "name" : "Krishna",
        "age": 32,
        "country": "India"
    },
    2 : {
        "name" : "Ram",
        "age": 33,
        "country": "China"
    },
    3 : {
        "name" : "Bomma",
        "age": 38,
        "country": "China"
    }
}

@app.get("/emps/by-country")
def empByCountryName(countryName: CountryEnum):
    empsTemp = []

    for empId in emps:
        if (emps[empId]["country"] == countryName.value):
            empsTemp.append(emps[empId])
    return empsTemp