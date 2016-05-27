from framework.request_handler import YumSearchRequestHandler


class HomePage(YumSearchRequestHandler):
    def get(self):
        self.render('google_landing/landing.html')  