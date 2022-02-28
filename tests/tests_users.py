from django.test import TestCase

class UsersViewsTests(TestCase):
    
    fixtures = ['users.json']

    def test_index_view(self):
        """
        Should return login page
        """
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Log In")

    def test_login_view(self):
        """
        Should login user
        """
        response = self.client.post("/users/login", {"username":'joe', "password":'bar'})
        self.assertEqual(response.status_code, 200)

    def test_login_view_wrong_credentials(self):
        """
        Should not login user
        """
        response = self.client.post("/users/login", {"username":'joey', "password":'bar'})
        self.assertEqual(response.status_code, 401)
        
    def test_logout_view(self):
        response = self.client.post("/users/login", {"username":'joe', "password":'bar'})
        self.assertEqual(response.status_code, 200)
        
        response = self.client.get("/users/logout")
        self.assertEqual(response.status_code, 200)
    
