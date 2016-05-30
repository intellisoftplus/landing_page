from google.appengine.ext import ndb
from google.appengine.api import search

from google.appengine.api import mail

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

    	#send an email to sales team
    	message = mail.EmailMessage(sender="ISP Marketting Campaign <noreply@isplandingpage2.appspotmail.com>",subject="NEW SIGN UP - REQUIRES YOUR ATTENTION")
    	message.to = "chantal@intellisoftplus.com,wakari@intellisoftplus.com,reshiwani@intellisoftplus.com"
    	message.body = """
				New sign up,

				The below contact has filled the report form.

				Name: %s
				Phone No.: %s
				E mail : %s
				Product : %s

				Please follow up immediately and Slack the team to keep them in the loop.
				""" % (names,number,email, product)
        message.send()

