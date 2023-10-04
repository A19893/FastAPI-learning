from fastapi import APIRouter,Request,FastAPI
from models.note import Note
from config.db import conn
from schemas.note import noteEntity,notesEntity
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

note=APIRouter()
templates= Jinja2Templates(directory="templates")

@note.get("/", response_class=HTMLResponse)
async def read_item(request: Request):
    docs=conn.notes.notes.find({});
    newDocs=[]
    for doc in docs:
        newDocs.append({
            "id": doc["_id"],
            "Title":doc["title"],
            "Description":doc["desc"],
        })
    return templates.TemplateResponse("index.html",{"request":request, "newDocs":newDocs})

@note.post("/")
async def add_note(request:Request):
  form= await request.form();
  note= conn.notes.notes.insert_one(dict(form))
  return{"Success": True}