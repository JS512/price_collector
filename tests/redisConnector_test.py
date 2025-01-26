import unittest,requests
from unittest.mock import patch, MagicMock

from connector.redis_connector import RedisConnector

class TestPriceCollect(unittest.TestCase):    
    def setUp(self):        
        self.db = RedisConnector()
    
    def test_get_all_urls(self) :
        db = MagicMock()
        mock_data = {"discount" : 1, "origin_price" :2}
        
        with patch('connector.redis_connector.redis.StrictRedis', return_value=db):
            db_conn = RedisConnector()
        
        
        db.hget.return_value = mock_data#의미가 있나??
        a = db.hget("test", 1)
        self.assertEqual(a, mock_data)
        
        db_conn.set_price_info(1, mock_data)
        db.hset.assert_called_once_with(1, mock_data)
        
    def test_check_has_minimum_price(self) :
        rs = self.db.check_has_minimum_price()
        self.assertEqual(rs, False)
        
    def test_get_minimum_price_info(self) :
        rs = self.db.get_minimum_price_info()
        self.assertEqual(rs, {})
        
    def test_set_minimum_price(self) :
        rs = self.db.set_minimum_price({1 :{"discount" : 12,
                            "origin_price" : 15665,
                            "sale_price" : 2000
                            }}, 1, {"discount" : 12,
                            "origin_price" : 15665,
                            "sale_price" : 5000
                            })
        
        self.assertEqual(rs, False)
        
        