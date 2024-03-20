# Blog by Django
### Install
##### Create virtual environment  
python -m venv myenv
#### Activate virtual environment
myenv\Scripts\activate
#### Install requirements
pip install -r requirements.txt 
#### Perform migration
python manage.py makemigrations
python manage.py migrate

### Run
python manage.py runserver
### Credentials
Superuser  
Login: admin  
Password: admin  
### Endpoinst
/ post_lists  
/new_post/ create new post  
/new_comment/ create new comment  
