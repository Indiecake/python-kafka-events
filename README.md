# Project setup

## Start kafka & zookeeper
You can start kafka by running the command 
```
docker-compose up
```

## Install dependencies
```
Run pip install -r ./requirements.txt
```

## now you can start the python apps in the connectors directory
(make sure to run each app in different terminals)
```
python inference.py

python notification.py

python email.py
```

# Start the web server 
You can start the flask app by running 
```python app.py```

And now you can make a test call to the server to the 
`127.0.0.1:5000/kafka/pushToConsumers` endpoint

the flask api will send the data between the different applications using kafka messages

the application will look for ```notification_settings``` property in the data sent in the http request

### example data
```
{
    "notification_settings": {
        "phone": false,
        "email": true,
        "user": {
            "email": "test@test.com",
            "name": "Jhon doe",
            "phone": ""
        }
    }
}
```