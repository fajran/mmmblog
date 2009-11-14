mmmblog
=======

A very simple blog engine built on Django. This blog engine is intended for
dynamic page haters that only eats server's resources. Static HTML pages will
be generated whenever blog entries are added or removed.

mmmblog is specially made for [KAMBING.ui.ac.id](http://kambing.ui.ac.id/)
because the admin is already tired to ssh the server just only to add updates.
mmmblog can be secretly placed somewhere and the resulted static pages can be
rsync-ed to the server.

This blog engine only have two kinds of content: Blog and Link. Blog has text
content while Link is used to put a new URL with a short description.


Installation
------------

I believe there are many tutorials out there showing you how to install a
Django application. So, just
[Google](http://lmgtfy.com/?q=deploying+django+application) it! If you are too
lazy, just open one of these two:

* [Deploying Django from The Django Book](http://www.djangobook.com/en/beta/chapter21/)
* [Deploying Django from the Django Documentation](http://docs.djangoproject.com/en/dev/howto/deployment/)

mmmblog uses [buildout](http://www.buildout.org/) to make life easier. Run
`bootstrap.py` and after that run `./bin/buildout`. Django installation and
environment will be taken care of by buildout. All other required modules are
too.

    $ python bootstrap.py
    $ ./bin/buildout

Test the app by running `syncdb` and `runserver` as usual.

    $ ./bin/django syncdb
    $ ./bin/django runserver


