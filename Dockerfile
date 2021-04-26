# Use the Debian 10(Buster) image
FROM python:3-buster
WORKDIR /code

# set env - PYTHONUNBUFFERED prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED=1

# install pip and project dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
<<<<<<< Updated upstream
COPY . /code/
=======
COPY . /code/
>>>>>>> Stashed changes
