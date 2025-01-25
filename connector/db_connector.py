import mariadb
import sys, math

class DBConnector() :
    def __init__(self, host="localhost", port=3306 ,user="host" , pw="ss147147!@", db="price"):
        
        self.conn = mariadb.connect(
            host="localhost",
            port=3306,
            user="host",
            password="ss147147!@",
            database = db
        )
        self.cursor = self.conn.cursor(dictionary=True)
        
    def get_user_data(self, id) :
        self.cursor.execute(
            "SELECT user_id, user_pw FROM user WHERE user_id = ?", 
            (id,))
        
        return self.cursor.fetchall()
    
    
    def get_all_urls(self) :
        self.cursor.execute("SELECT * from url")
        rs = []
        for url_info in self.cursor.fetchall() :
            rs.append((url_info["id"], url_info["url_link"]))
        return rs
    
    def get_user_url(self, id) :
        self.cursor.execute(
            """SELECT url.url_link FROM user
            JOIN user_url ON (user.user_id = user_url.user_id)
            JOIN url ON (user_url.url_id = url.id)
            WHERE user.user_id=?""", 
            (id,))
        
        return self.cursor.fetchall()
    
    def save_price_data(self, data:list[tuple]) :
        
        try :
            for i in range(math.ceil(len(data)/2500)) :
                self.cursor.executemany("INSERT INTO  price_data (discount, origin_price, discount_price, url_id)  values (%s, %s, %s, %s)",
                data[:2500])
                data = data[2500:]
                
                self.conn.commit()
                
            return True
        except Exception as e :
            print(e)
            return False
        
    def close(self):
        """클래스의 리소스를 정리하는 메서드"""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()
            
        