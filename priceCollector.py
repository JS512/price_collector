import requests, re
from bs4 import BeautifulSoup
from enum import Enum

class GOODWEARMALL(Enum) :
    DICOUNT = "dcRt"
    ORIGIN_PRICE = "cvrPrc"
    SALE_PRICE = "salePrc"
    
    
class PriceCollector() :
    def __init__(self):
        self._origin_price = 0
        self._sale_price = 0
        self._discount = 0

    @property
    def origin_price(self):
        return self._origin_price
    
    @property
    def sale_price(self):
        return self._sale_price
    
    @property
    def discount(self):
        return self._discount
    
    def get_product_url_response(self, url) :
        return requests.get(url)
    
    def get_product_url_response_html(self, url) :
        res = self.get_product_url_response(url)
        soup = BeautifulSoup(res.text, "lxml")
        return soup
    
    def get_price_info_in_url_response_html(self, soup) :
        scripts = soup.find_all("script")
        
        for script in scripts :
            origin_price = self.find_key_value_pairs(script.string, GOODWEARMALL.ORIGIN_PRICE.value)
            sale_price = self.find_key_value_pairs(script.string, GOODWEARMALL.SALE_PRICE.value)
            discount = self.find_key_value_pairs(script.string, GOODWEARMALL.DICOUNT.value)
            
            if len(origin_price) > 0 and len(sale_price) > 0 and len(discount) > 0 :                
                self._origin_price = int(float(origin_price[0]["value"])) if self.check_string_is_float(origin_price[0]["value"]) else int(origin_price[0]["value"])
                self._sale_price = int(float(sale_price[0]["value"])) if self.check_string_is_float(sale_price[0]["value"]) else int(sale_price[0]["value"])
                self._discount = int(float(discount[0]["value"])) if self.check_string_is_float(discount[0]["value"]) else int(discount[0]["value"])
                
        return {
            "discount" : self.discount,
            "sale_price" : self.sale_price,
            "origin_price" : self.origin_price
        }
    
    def find_key_value_pairs(self, input_string, target_key):
        if input_string :
            # 정규식을 정의하여 'var key = ...; var value = ...;' 패턴을 찾습니다.
            pattern = rf"var\s+key\s*=\s*['\"]{target_key}['\"];\s*var\s+value\s*=\s*['\"](.*?)['\"];"
            matches = re.finditer(pattern, input_string)
            
            # 결과를 리스트로 반환합니다.
            results = [{"key": target_key, "value": match.group(1)} for match in matches]
            
        else :
            results = []
        return results
    
    def check_string_is_float(self, element) -> bool :
        if re.match(r'^-?\d+(?:\.\d+)$', element) is None:
            return False
        else :
            return True
    
    