from framework.request_handler import YumSearchRequestHandler
from models.customer_details import customer_details


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
    	self.redirect('/')
