FROM nikolaik/python-nodejs:python3.11-nodejs20

USER pn

WORKDIR /home/pn/app

COPY requirements.txt ./

COPY package*.json ./

COPY tailwind.config.js ./

COPY src ./src

USER root

RUN pip install -r requirements.txt

RUN npm install

USER pn

EXPOSE 5000

CMD ["python", "./src/run.py"]

