import unittest,requests
from unittest.mock import patch, MagicMock

from connector.db_connector import DBConnector

class TestPriceCollect(unittest.TestCase):    
    def setUp(self):        
        self.db = DBConnector()

    def test_get_user_info(self):        
        user_info = self.db.get_user_data("test")
        self.assertEqual(user_info[0]["user_id"], "test")
        self.assertEqual(user_info[0]["user_pw"], "test")
        
    def test_get_user_url(self) :
        user_url = self.db.get_user_url("test")
        self.assertEqual(len(user_url), 2)
        
        
    def test_save_price_data(self) :
        success = self.db.save_price_data([(78, 86000, 18500, 1)])        
        self.assertEqual(success, True)
    
    
    def test_get_all_urls(self) :
        db = MagicMock()
        cursor = MagicMock()
        db.cursor.return_value = cursor
        
        with patch('connector.db_connector.mariadb.connect', return_value=db):
            db = DBConnector()
        
        cursor.fetchall.return_value = [
            {"id" : 1, "url_link" : "xxxx"},
            {"id" : 2, "url_link" : "xxxx"},
            {"id" : 3, "url_link" : "xxxx"},
            {"id" : 4, "url_link" : "xxxx"},
        ]
        
        
        rs = db.get_all_urls()
        
        self.assertEqual(len(rs), 4)
        
        # cursor.execute.assert_called_once_with("SELECT * from url")
        # db.close.assert_called_once()