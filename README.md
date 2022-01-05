# gudlift-registration


## 1. Installation

   - First you need to clone the repository to your local machine :
```
$ git clone https://github.com/Ldm3110/Python_Testing.git
```

   - Come to the folder creating after the cloning :
```
$ cd Python_Testing
```

   - You must install a virtual environment on this folder to execute the app, for them type :
```
$ python3 -m venv env
```
   - After than, activate it :
```
$ source env/bin/activate
```
   - You must install all the packages necessary to the good functioning of the app
```
$ pip install -r requirements.txt
```

CONGRATULATIONS you're ready to use the application !!


## 2. Test application

- All the tests are in the 'tests' folder, there are different types of test on this application :

   - Unit tests
   - Performance tests
   - Coverage test

- To perform all these test, we used the following packages :

   - Pytest
   - Coverage
   - Locust
   
### Realize tests

#### For unit tests :

From the project root, type <code> $ pytest -v </code>. You will see the report on your terminal or command prompt

#### For coverage tests :

From the project root, type <code> $ pytest --cov=. --cov-report=html </code>. You will see a new folder on your 
project named "htmlcov", go to that folder with <code> $ cd htmlcov </code> and type <code> $ open index.html </code>.
You will be redirected to the coverage report on your browser 

#### For performance tests :

Go to he performance folder with <code> $ cd tests/performance_test/ </code> an just type <code> $ locust </code>.
Open your browser and go to <code> http://0.0.0.0:8089 </code>. Indicate how many users you want to create during the
test, the intervall enter each creation and the adress of your project. Here, it will be the following adress 
<code> http://127.0.0.1:5000 </code>. Click on "Start swarming". The test begin.
If you want to stop the test, clic on the "STOP' button at the top right of your browser window.
    

