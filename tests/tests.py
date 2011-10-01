import os
import unittest

from google.appengine.ext import testbed
import models
import main

class PortalTestCase(unittest.TestCase):
    def setUp(self):
        # Flask apps testing. See: http://flask.pocoo.org/docs/testing/
        main.app.config['TESTING'] = True
        main.app.config['CSRF_ENABLED'] = False
        self.app = main.app.test_client()
       
 		self.testbed = testbed.Testbed()
        self.testbed.activate()
        self.testbed.init_datastore_v3_stub()
        self.testbed.init_user_stub()
        self.testbed.init_memcache_stub()

    def tearDown(self):
        self.testbed.deactivate()

    def setCurrentUser(self, email, user_id, is_admin=False):
        os.environ['USER_EMAIL'] = email or ''
        os.environ['USER_ID'] = user_id or ''
        os.environ['USER_IS_ADMIN'] = '1' if is_admin else '0'

    def logoutCurrentUser():
        setCurrentUser(None, None)

    def test_home_redirects(self):
        rv = self.app.get('/')
        assert rv.status == '200 OK'
    
if __name__ == '__main__':
    unittest.main()