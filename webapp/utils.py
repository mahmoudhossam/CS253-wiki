#Misc. utility functions
from models import User, Article
import bcrypt
import re

def get_user(userid=None, username=None):
    try:
        if username:
            user = User.objects.get(username=username)
        else:
            user = User.objects.get(id=userid)
        return user
    except User.DoesNotExist:
        return None

def get_page(page_name):
    try:
        article = Article.objects.get(title=page_name)
    except Article.DoesNotExist:
        return None
    return article

def hash_password(password, salt=None):
    if not salt:
        salt = bcrypt.gensalt()
    hashed_pw = bcrypt.hashpw(password, salt)
    return [hashed_pw, salt]

def valid_username(usr):
    usr_re = re.compile(r"^[a-zA-Z0-9_-]{3,20}$")
    return usr_re.match(usr)

def valid_password(pw):
    pw_re = re.compile("^.{3,20}$")
    return pw_re.match(pw)

def valid_email(email):
    email_re = re.compile("^[\S]+@[\S]+\.[\S]+$")
    return email_re.match(email)
