### 使用 Python + Django 搭建 Web 服务网站

### install Python 3.4.3

[Python Home](https://www.python.org/)  [python-3.4.3-macosx10.6.pkg]{https://www.python.org/ftp/python/3.4.3/python-3.4.3-macosx10.6.pkg}

sudo ln -s /usr/local/bin/python3 /usr/bin/python

```
➜  ~  python
Python 3.4.3 (v3.4.3:9b73f1c3e601, Feb 23 2015, 02:52:03) 
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
```

### install Django 

[Django Home](https://www.djangoproject.com/)
[Django-1.8.3](https://www.djangoproject.com/m/releases/1.8/Django-1.8.3.tar.gz)

tar zxvf Django-1.8.3.tar.gz
cd Django-1.8.3 
sudo python setup.py install

sudo ln -s /Library/Frameworks/Python.framework/Versions/3.4/lib/python3.4/site-packages/Django-1.8.3-py3.4.egg/django/bin/django-admin.py /usr/local/bin/

### create Project

```
django-admin.py startproject rxfit
cd rxfit
tree
➜  rxfit  tree
.
├── rxfit
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

1 directory, 5 files
```

### start Server

```
➜  rxfit  python manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).

You have unapplied migrations; your app may not work properly until they are applied.
Run 'python manage.py migrate' to apply them.

August 12, 2015 - 03:55:19
Django version 1.8.3, using settings 'rxfit.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```







