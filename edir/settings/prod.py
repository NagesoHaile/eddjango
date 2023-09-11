from .common import *
import os


SECRET_KEY = os.environ['SECRET_KEY']

DEBUG = False


ALLOWED_HOSTS = ['.vercel.app', 'edir-pi.vercel.app']
DATABASES = {}
