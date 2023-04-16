
Pre-Req:
1. Python
   - pip install virtualenv
   - virtualenv venv
   - source venv/bin/activate
2. Docker
3. REST api client

Steps:
- git clone repo
- pip install -r requirments.txt
- docker run -it -p 27017:27017 mongo
- Run below :

    POST:    http://0.0.0.0:5001/add
        {"name":"Deepak","age":30}
    GET:    http://0.0.0.0:5001/get
