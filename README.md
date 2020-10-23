# redoc_issue_with_union_mini_example

example to demenstrate redoc bug.

run:

```bash
uvicorn --host=0.0.0.0 --port=8000 redoc_issue_with_union_mini_example.main:app --reload
```

go to http://localhost:8888/redoc and see example payload for circle.

redoc seems to generate examples for each class in Union and adds parameters of the example from main.example_shape on top.
