from webapp2 import WSGIApplication
from webapp2 import Route

app = WSGIApplication(
	routes = [
	Route('/', handler='app.landing.HomePage'),
	Route('/ms_landing', handler='app.landing.MSHomePage'),
	Route('/signin', handler='app.landing.Signin'),
	Route('/register', handler='app.landing.Register'),
	Route('/subscribe', handler='app.landing.Subscribe'),
	Route('/details', handler='app.landing.Details'),
	Route('/lessons', handler='app.landing.Lessons')      

]
)

       