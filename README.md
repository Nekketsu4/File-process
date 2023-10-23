# File process

## Quick start

### Short Description

DRF + Celery + Flower + Docker 

After starting the project server according to the instructions, you can go to the following pages.

- A page with a list of files http://127.0.0.1:8000/files/
- Upload any files. Only .txt .png .pdf .jpg file formats will be processed http://127.0.0.1:8000/upload/
- Еhe page with the flower interface is here http://127.0.0.1:5555

### Requires

- [Python => 3.10](https://www.python.org/downloads/)


### Install

Clone this git repository to your local machine https://github.com/ekketsu4/pikasso.git

```bash
#Go to the project directory
cd files

#Create a virtual environment
python3 -m venv venv

#Run the virtual environment
source venv/bin/activate (on Windows: venv/Scripts/activate)

#Install requierements
pip install -r req.txt

#migrate data
python3 manage.py makemigrations
python3 manage.py migrate

#build docker-compose and run it
docker-compose build
docker-compose run

```


