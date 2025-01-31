from django.test import TestCase, RequestFactory
from django.urls import reverse
from price.views import *
from django.urls import path
from unittest.mock import MagicMock, patch
# Create your tests here.

class TestUrlList(TestCase) :
        
        
    def setUp(self):
        self.request = RequestFactory().get(reverse('urllist'))
        self.view = UrlListView()
        self.view.setup(self.request)
        pass
    
    def tearDown(self):
        # Clean up run after every test method.
        pass
    
    @patch('requests.get')
    def test_get(self, mock_request):        
        mock_request.get.return_value = {"id" : "test"}
        response = (UrlListView.as_view())(mock_request)
        print(mock_request)
        print(response)
        self.assertEqual(response.status_code, 200)
        self.assertFalse(False)

    def test_something_that_will_fail(self):
        self.assertTrue(False)