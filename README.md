# bank_transac
Bank_trasaction application

# To test this setup a postgresql database with these credentials:

'NAME': 'tran_db',
'USER': 'tran_user',
'PASSWORD': 'Work@100',
'HOST': 'localhost',
'PORT': 5432

# Install the necessary dependecies:
run the command: pip install -r requirements.txt

# Run migrations:
run the commands:
python manage.py makemigrations
python manage.py migrate

# Run the server:
run this command: python manage.py runserver,

After this, the web-app would be running on port 8000, an you can access it on your web brouser by this url: localhost:8000 
