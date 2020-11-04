from fastapi import FastAPI, Body
from typing import Union
from pydantic import BaseModel, Field


class Circle(BaseModel):
    circle_center_x: int = Field(example=100)
    circle_center_y: int = Field(example=200)
    circle_radius: int = Field(example=500)


class Rectangle(BaseModel):
    rect_upper_left_x: int = Field(example=10)
    rect_upper_left_y: int = Field(example=20)
    rect_width: int = Field(example=30)
    rect_height: int = Field(example=40)


UnionInput = Union[
    Circle,
    Rectangle,
]

example_shape = Body(
    None,
    examples={
        "Rectangle": {
            "summary": "Rectangle",
            "value": {
                "rect_upper_left_x": 43,
                "rect_upper_left_y": 42,
                "rect_width": 42,
                "rect_height": 42,
            },
        },
        "Circle": {
            "summary": "Circle",
            "value": {
                "circle_center_x": 2,
                "circle_center_y": 2,
                "circle_cradius": 2,
            },
        },
    },
)


app = FastAPI()


@app.post("/shapes")
async def post_shapes(
    shape: UnionInput = example_shape,
):
    return 200