#### Client Report Details 
This flask application reads input.txt using JSON parsing data.
It generates CSV output per client and product with a net position.
Currently, it uses the root/home URL to kick-start the process and download the output file.


#### Improvements (TBD)
1. Input and output files can be parametrized
2. Adding more doc tests per function
3. Adding more unit tests & Flask app tests
4. Integration with SwaggerUI
5. Parametrized with user able to provide client id (say) to generate report specific to the client
6. Dockerize the solution & make it ready for K8S environment
7. Add Gunicorn and Nginx
8. Authentication
9. HTTPS

#### Create virtual env & activate it
1. python3 -m venv .venv 
1. . .venv/bin/activate
1. pip install --upgrade pip
1. pip install -r requirements.txt
1. export PYTHONPATH=.:$PYTHONPATH

#### Run flake8 and black as below
1. flake8 .
1. black --exclude=.venv,tests .

#### Run tests
1. python3 -m unittest
1. python -m doctest -v ReportGen/process_data.py 


#### run the application 
1. python3 -m flask --app ReportGen run --port 8000 --debug

#### Access the page and generate the report
http://127.0.0.1:8000/
