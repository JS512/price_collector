import unittest,requests

from priceCollector import PriceCollector, GOODWEARMALL
class TestPriceCollect(unittest.TestCase):    
    def setUp(self):
        self.url = "https://www.goodwearmall.com/product/1P241112762961/detail?trackNo=special&trackDtl=special_166400"
        self.price_collector = PriceCollector()

    def test_get_response(self):        
        response = self.price_collector.get_product_url_response(self.url)
        self.assertEqual(200, response.status_code)

    def test_get_response_text(self) :
        soup = self.price_collector.get_product_url_response_html(self.url)
        self.assertNotEqual(None, soup)
        
    def test_get_price_info(self) :
        soup = self.price_collector.get_product_url_response_html(self.url)
        price_info = self.price_collector.get_price_info_in_url_response_html(soup)
        self.assertEqual(34, self.price_collector.discount )
        self.assertEqual(37800, self.price_collector.sale_price )
        self.assertEqual(57800, self.price_collector.origin_price )