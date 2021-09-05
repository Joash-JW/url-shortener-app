import unittest
from unittest import mock
from app import app, db, UrlMapping
app.testing = True

class Test(unittest.TestCase):
    def test_main(self):
        with app.test_client() as client:
            longUrl = 'https://github.com/Joash-JW'
            # send data as POST form to endpoint
            response = client.post('/shorten', data={'longUrl': longUrl})
            
            # check response status
            self.assertEqual(response.status_code, 200)
            
            shortUrl = response.data.decode('utf-8')
            queryResult = UrlMapping.query.filter(UrlMapping.shortUrl==shortUrl.split('/')[-1]).first()

            # check if endpoint in database
            self.assertTrue(queryResult)
            
            response = client.get(shortUrl)
            
            # check response status
            self.assertEqual(response.status_code, 302)

            # check redirected url
            self.assertEqual(response.location, longUrl)