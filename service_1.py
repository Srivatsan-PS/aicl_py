from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
from time import time
from urllib import request
from fastapi import FastAPI,Request
import pybase64


from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates



app = FastAPI()
@app.get("/hello/{my_query}")
async def home(my_query, q:Optional[str]=None):
    return{"sri":"vatsan","user_input":my_query,"query":q}

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

class EMPLOYEE(BaseModel):
    name:str
    exp:int
    yop:int
    age:int
    employeed:bool

app = FastAPI()
@app.put("/endpoint")
async def endpoint(person: RESUME):
    return{"personname": person.name,"personage":person.age,"personDOB":person.DOB,"personregion":person.region,"persontechnicalskills":person.technicalskills,"personcertifications":person.certifications,"personareasofinterest":person.areas_of_interest}

@app.post("/mypostendpoint")
async def mpep(emp:EMPLOYEE):
    return {"emp":emp.name}


@app.get("/token")
async def tokenGenerator():

    timenow = bytes(str(time.time()),"utf-8")
    token = pybase64.b64encode(timenow, altchars='_:')
    with open("token.txt","a+") as tokenfile: 
        tokenfile.write(str(token) + "|\n" )
        tokenfile.close()
    return {"token":token}


@app.get("/mySecureEndpoint")
async def msep(token:str,field1:str, field2:str,):
    
    file = eval(str(open("token.txt","r+").readlines()))
    for each in file:
        if token in each:
             authorisation = "Welcome Home!"
             break
        else:
             authorisation = "Get Out!"
             pass
    
    return {"server_pass":authorisation}
     

@app.get("/webpage", response_class=HTMLResponse)
async def webpage():
    html_code = """
            <html>
            <head>
            </head>
            <body>
            <h1>HI
            </body>
            </html>
    
     """
    return html_code


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")



@app.get("/htmlfile", response_class=HTMLResponse)
async def webpage(request:Request):
    return templates.TemplateResponse('index.html', context={'request': request})




