Installation Instructions:

1) Clone the project

1) Setup a PostgreSQL database and do following changes in "demo/settings.py" in 'DATABASES' variable-
  1. Replace the 'demo_data' with your database's name
  2. Provide the 'USER' and 'PASSWORD' of the user having access to this database.
  
2) Install Python==3.6(if not) and all the requirements given in file "requirement.txt"

3) To upload the data to database open terminal and activate the virtual environment(if there is)-
  1. run 'export DJANGO_SETTINGS_MODULE=demo.settings'
  2. open python shell by typeing 'python3'
  3. type and enter 'from home.task import save_data', do it again if there is any error
  4. type and enter 'save_data()', wait this function to finish cause it may take some time.
  5. Exit the python shell

4) Go to directory 'demo' (where 'manage.py' file exists)
5) Start the server 'python3 manage.py runserver'
6) Visit 'http://localhost:8000/' to see the results

