FROM python
WORKDIR /usr/app/
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
#RUN apt-get update
#RUN apt-get install ffmpeg libsm6 libxext6  -y
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]
#CMD python app.py