from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


class RESUME(BaseModel):
    name: str
    age: int
    DOB: int
    region:str
    hobbies:Optional[list]
    technicalskills:Optional[list]
    areas_of_interest:Optional[list]
    certifications:Optional[list]
    internships:Optional[list]
    
    
@app.get("/hello/{my_query}")
async def home(my_query, q:Optional[str]=None):
    return{"sri":"vatsan","user_input":my_query,"query":q}


@app.put("/endpoint")
async def endpoint(person: RESUME):
    return{"personname": person.name,"personage":person.age,"personDOB":person.DOB,"personregion":person.region,"persontechnicalskills":person.technicalskills,"personcertifications":person.certifications,"personareasofinterest":person.areas_of_interest}