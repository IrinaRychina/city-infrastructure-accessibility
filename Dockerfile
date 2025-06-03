FROM python:3.11

WORKDIR /app

COPY requirements.txt requirements.txt
RUN python -m pip install --upgrade pip && pip install -r requirements.txt

COPY scripts/overpass_wheelchair_data_collection.py scripts/overpass_wheelchair_data_collection.py

ENTRYPOINT ["python", "scripts/overpass_wheelchair_data_collection.py"]