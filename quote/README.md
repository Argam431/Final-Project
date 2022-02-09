# Quote project

## Initial actions
create virtual environments<br>
> py -m venv venv - windows

install requirements.txt<br>
> pip install -r requirements.txt

Go the project settings and add your database settings

I use django-debug-toolbar<br>
<a href="https://django-debug-toolbar.readthedocs.io/en/latest/">how to use this tool</a>

## Second actions

Create database tables with the project models<br>
> py manage.py makemigrations<br>
> py manage.py migrate<br>


https://quotes.toscrape.com/
> py manage.py load_quotes [position parameter page count {int} ]
