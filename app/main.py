import base64
from logging import critical
from typing import List, Tuple
from showplaces import get_showplaces
from draw_graph import draw_graph

from fastapi import FastAPI, Response
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Graph(BaseModel):
    nodes_number: int
    max_time: int
    leave_nodes: List[int]
    arrive_nodes: List[int]
    nodes_width: List[int]



@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/get-graph")
def plot_graph(graph: Graph):
    
    visitable_showplaces = get_showplaces(graph.leave_nodes, graph.arrive_nodes, graph.nodes_width, graph.max_time, graph.nodes_number)

    img_bytes = draw_graph(graph.leave_nodes, graph.arrive_nodes, graph.nodes_width, graph.nodes_number, visitable_showplaces)

    encoded_image_string = base64.b64encode(img_bytes.read())

    return {"image_string": encoded_image_string}