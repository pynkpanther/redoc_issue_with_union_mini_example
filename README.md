# redoc_issue_with_union_mini_example

example to demenstrate redoc bug.

# Let FastAPI generate openapi.json:

run:

```bash
poetry install
uvicorn --host=0.0.0.0 --port=8000 redoc_issue_with_union_mini_example.main:app --reload
```

go to http://localhost:8888/redoc and see example payload for circle.

redoc seems to generate examples for each class in Union and adds parameters of the example from main.example_shape on top.

for swaggerUI:
http://localhost:8888/docs

# Redoc manually:

Start via FastAPI and save http://localhost:8000/openapi.json to`redoc_issue_with_union_mini_example/redoc/openapi.json

```bash
cd redoc_issue_with_union_mini_example/redoc
python3 -m http.server 8001
```

# SwaggerUI manually:

Start via FastAPI and copy http://localhost:8000/openapi.json to live editor:

https://editor.swagger.io/