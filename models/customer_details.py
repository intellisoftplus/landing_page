from google.appengine.ext import ndb
from google.appengine.api import search

class customer_details(ndb.Model):
    names = ndb.StringProperty()
    email = ndb.StringProperty()
    org = ndb.StringProperty()
    number = ndb.StringProperty()
    product = ndb.StringProperty()
    posted = ndb.DateTimeProperty(auto_now_add=True)

    @classmethod
    def add_new_details(cls, names, email, org, number, product):

    	user_details_key = cls(
    		names = names,
    		email = email,
    		org = org,
    		number = number,
    		product = product
    		
    		).put()
