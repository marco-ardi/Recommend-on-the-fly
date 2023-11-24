FROM tiangolo/uvicorn-gunicorn-starlette:python3.7

COPY * .
RUN pip install numpy pandas scikit-surprise starlette