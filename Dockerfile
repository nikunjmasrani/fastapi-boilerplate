FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9

#USER nikunj

LABEL org.opencontainers.image.authors="nikunj.masrani@smartsensesolutions.com"
LABEL version="1.0"
LABEL description="Dokcer image for fastapi boilerplate"

# Set the Current Working Directory inside the container.
WORKDIR /app

# Upgrading pip.
RUN pip install --upgrade pip

# Download all dependencies.
COPY requirements.txt /app/

# Install all dependencies.
RUN pip install -r /app/requirements.txt

# Copy current directory into working directory.
COPY . /app

EXPOSE 8080
#CMD ["gunicorn", "app.application:get_app()", "--workers=2", "--worker-class=uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8080", "--timeout=120"]
CMD ["uvicorn", "app.application:get_app", "--workers=2", "--host=0.0.0.0", "--port=8080", "--timeout-keep-alive=120"]
