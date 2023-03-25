FROM python:3.8-slim-buster

WORKDIR /backend

#RUN py -3 -m venv venv
#RUN venv\Scripts\activate

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /backend/app
RUN pip install psycopg2-binary

COPY . ./

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "--app" , "app/main", "run", "--host=0.0.0.0"]

#CMD [ "flask", "--app" , "app/main", "run", "--host=0.0.0.0"]
