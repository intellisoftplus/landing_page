from framework.request_handler import YumSearchRequestHandler
from models.customer_details import customer_details
import urllib2



class HomePage(YumSearchRequestHandler):
    def get(self):
        self.render('google_landing/landing.html')

    def post(self):
    	names = self.request.get('names')
    	email = self.request.get('email')
    	org = self.request.get('org')
    	number = self.request.get('number')
    	product = "Google Apps"

    	customer_details.add_new_details (

    		names = names,
    		email = email,
    		org = org,
    		number = number,
    		product = product,
    	)

    	#download file
    	#req = urllib2.Request('https://drive.google.com/open?id=0B2ItpO1CAjO9ckM0WTlmdFRaN0k')
    	#response = urllib2.urlopen(req)
    	#the_page = response.read()

    	#redirect the user the Document
    	self.redirect('https://drive.google.com/file/d/0B2ItpO1CAjO9aGw2TFVTd3hpcmc/view?usp=sharing')

class MSHomePage(YumSearchRequestHandler):
    def get(self):
        self.render('google_landing/landing-microsoft.html')

    def post(self):
        names = self.request.get('names')
        email = self.request.get('email')
        org = self.request.get('org')
        number = self.request.get('number')
        product = "Microsoft"

        customer_details.add_new_details (

            names = names,
            email = email,
            org = org,
            number = number,
            product = product,
        )

        #download file
        #req = urllib2.Request('https://drive.google.com/open?id=0B2ItpO1CAjO9ckM0WTlmdFRaN0k')
        #response = urllib2.urlopen(req)
        #the_page = response.read()

        #redirect the user the Document
        self.redirect('https://drive.google.com/file/d/0B2ItpO1CAjO9OXkwaEMxaWJTWnc/view?usp=sharing')



