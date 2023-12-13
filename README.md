### Create virtual env & activate it
1 python3 -m venv .venv 
1 . .venv/bin/activate
1 pip install --upgrade pip
1 pip install -r requirements.txt

## Run flake8 and black as below
1 flake8 .
1 black --exclude=.venv,tests .

###

1 pytest
1 swagger
