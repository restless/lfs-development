What is it?
===========

This is the development environment for LFS. 

It will create a complete developement evironment for [LFS](https://github.com/diefenbach/django-lfs).

LFS is an online shop based on Python, Django and jQuery.

Why should (not) I use it?
============================

I strongly recommend checking the [LFS cookiecutter template](https://github.com/restless/cookiecutter-django-lfs) as it will generate the project like this one for you. I will also focus on the cookiecutter-django-lfs and not on this project so it will be probably more up to date than this project is.

But if you want then go with this project - it's based on standard pip and its requirements file - not on buildout as lfs-buildout-development does.

How to use it?
==============

1. Check it out from GitHub
    
    $ git clone git@github.com:restless/lfs-development.git

2. Change to the directory

    $ cd lfs-development

3. Create virtualenv (use virtualenv and virtualenv_wrapper)

    $ mkvirtualenv lfs

4. Install required libraries

    $ pip install -r requirements/local.txt
    
5. Enter your database settings into lfs_project/settings.py

6. Change to the directory

    $ cd lfs_project

7. Migrate your database

    $ python manage.py migrate
    
8. Initialize LFS

    $ python manage.py lfs_init

9. Start server

    $ python manage.py runserver
    
10. Browse to LFS

    http://localhost:8000
 
    
More Information
================

* Official page http://www.getlfs.com/
* Documentation on PyPI http://packages.python.org/django-lfs/index.html
* Releases on PyPI http://pypi.python.org/pypi/django-lfs
* Source code on GitHub https://github.com/diefenbach/django-lfs
* Google Group http://groups.google.com/group/django-lfs
* lfsproject on Twitter http://twitter.com/lfsproject
* IRC irc://irc.freenode.net/django-lfs