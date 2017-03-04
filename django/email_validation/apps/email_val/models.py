from __future__ import unicode_literals

from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9_+.-]+@[a-zA-Z0-9_+.-]+\.[a-zA-Z]+')

# Create your models here.
class EmailManager(models.Manager):
    # pass
    def register(self, data):
        print ("*"*100)
        print ("*"*100)
        print 'This is working so far'
        print data
        not_valid = 'Email address must be valid'

        if len(data) < 6:
            not_valid
            # errors.append('Email address must be valid')
            return (False, not_valid)
            
        if not EMAIL_REGEX.match(data):
            not_valid
            # errors.append('Email address must be valid')
            return (False, not_valid)

        else:
            new_email = Email.objects.create(email=data)
            print (new_email)
            print ("*"*50)
            print ("*"*50)
            return (True, new_email)

class Email(models.Model):
    email = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = EmailManager()
