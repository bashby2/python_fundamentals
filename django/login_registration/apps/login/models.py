from __future__ import unicode_literals

from django.db import models
import re, bcrypt
from bcrypt import hashpw, checkpw, gensalt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_+.-]+@[a-zA-Z0-9_+.-]+\.[a-zA-Z]+$')
NUMBER_REGEX = re.compile(r'.*[0-9]+')
LETTER_REGEX = re.compile(r'.*[a-zA-Z\-]+$')
UPPER_REGEX = re.compile(r'.*[A-Z]+')

class UserManager(models.Manager):
    def login_user(self, data):
        errors=[]
        db_user = User.objects.filter(email=data['email'])
        print ('-'*60)
        print 'looking for email in db'
        print db_user
        if not db_user:
            errors.append('Email/Password Combination Not Valid')
            return (False, errors)
        else:
            if not bcrypt.hashpw(postData['password'].encode(), bd_user[0].password.encode()) ==         db_user[0].password.encode():
                errors.append('Email/Password Combination Not Valid')
                return (False, errors)
            else:
                user = {
                'first_name': db_user[0].first_name,
                'last_name': db_user[0].last_name,
                'email': db_user[0].email
            }

            return (True)




    def create_new_user(self, data):
        errors = []
        print ('8'*50)
        print ('8'*50)
        print 'so far so good', data['first_name']

        if User.objects.filter(email=data['register_email'].strip().lower()):
            errors.append('A user with that Email Address already exists.  Please Log In.')

        if len(data['first_name']) < 2:
            errors.append('First name must be more than one charater')
        if not LETTER_REGEX.match(data['first_name']):
            errors.append('First name must be letters only ')

        if len(data['last_name']) < 2:
            errors.append('Last name must be more than one charater ')
        if not LETTER_REGEX.match(data['last_name']):
            errors.append('Last name must be letters only ')

        if not EMAIL_REGEX.match(data['register_email']):
            errors.append('Email must be valid ')
        if len(data['register_email']) < 6:
            errors.append('Email must be valid')

        if len(data['register_password']) < 9:
            errors.append("Please enter your password. Your password must be at least 8 charaters")
        if not LETTER_REGEX.match(data['register_password']):
            errors.append("Your password must contain at least one letter")
        if not UPPER_REGEX.match(data['register_password']):
            errors.append("Your password must contain at least one upper case letter.")
        if not NUMBER_REGEX.match(data['register_password']):
            errors.append("Your password must contain at least one number")
            print errors
        if data['confirm_password'] != data['register_password']:
            errors.append("Your passwords do not match. Please enter your password.")
            print errors

        if errors:
            return(False, errors)

            print ('50'*50)
            print errors

        else:
            print ('8'*50)
            print 'where are all the errors?'
            hashed = hashpw(data['register_password'].encode('utf-8'), gensalt())

            # first_name=data['first_name']
            # last_name=data['last_name']
            # email=data['register_email']
            # password=hashed
            # user = self.create(first_name=first_name, last_name=last_name, email=email)

            return(True, user)





class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    password=models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    objects=UserManager()
