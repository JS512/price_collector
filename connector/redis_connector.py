# redis 라이브러리 선언
import redis, json


class RedisConnector :
    def __init__(self, host='localhost', port=6379, db=0):        
        self.conn = redis.StrictRedis(host=host, port=port, db=db)
        pass
    
    def set_price_info(self, data) :
        temp = {}
        updated = []
        
        
        
        redis_price = self.get_minimum_price_info()
        
        
        for in_data in data :
            url_id = in_data[3]
            
            price_info = {"discount" : in_data[0],
                            "origin_price" : in_data[1],
                            "sale_price" : in_data[2]
                            }
            
            temp.update({
                url_id :json.dumps( price_info)
            })
            
            if self.set_minimum_price(redis_price, url_id, price_info) :
                updated_data = {
                    url_id : {"before" : redis_price[url_id],
                              "after" : price_info
                    }
                }
                updated.append(updated_data)
            
        self.conn.hset("price", mapping=temp)
        
        return updated
        
    def set_minimum_price(self, source, url_id, target_data) :
        
        if url_id not in source :
            self.conn.hset("price_minimum", url_id, json.dumps(target_data))
        elif source[url_id]["sale_price"] > target_data["sale_price"] :
            self.conn.hset("price_minimum", url_id, json.dumps(target_data))
            return True
            
        return False
        
                
        
    
    def get_price_info(self, url_id = None) :
        if url_id == None :
            redis_price = self.conn.hgetall("price")
            return {json.loads(key) : json.loads(val) for key,val in redis_price.items()}
        else :
            redis_price = self.conn.hget("price", url_id)
            return json.loads(redis_price)
            
    
    def get_minimum_price_info(self, url_id = None) :
        try :
            if url_id == None :
                redis_price = self.conn.hgetall("price_minimum")
                return {json.loads(key) : json.loads(val) for key,val in redis_price.items()}
            else :
                redis_price = self.conn.hget("price_minimum", url_id)
                return json.loads(redis_price)
        except Exception as e:
            print(e)
            return {}
        
            

        
    def check_has_minimum_price(self) -> bool :
        if self.conn.hgetall("price_minimum") :
            return True
        else :
            return False
        
        
if __name__ == "__main__" :
    a = RedisConnector()