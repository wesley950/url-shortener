# URL Shortener

This project is a very simple URL Shortener made using Django and Python. To deploy it just folow [the instructions on their documentation](https://docs.djangoproject.com/en/4.1/howto/deployment) (with a few minor details).

## SECRET_KEY

The environment variable `SECRET_KEY` should be present the moment the app is started, meaning you should either load an environment file before starting the app (you can do this where you import your application, if you are using WSGI), specifying in the command line if you are using `manage.py`'s runserver command, or manually add the variable to `os.environment`. Here's an example:

```
export DJANGO_SECRET_KEY=`openssl rand -hex 64`
python3 manage.py runserver
```
This will use the `openssl` command to create a strong key.
