from priceCollector import PriceCollector
from connector.db_connector import DBConnector
from connector.redis_connector import RedisConnector
from processor.notification_sendor import EmailSendor
import asyncio
import aiocron
import functools, random
from apscheduler.schedulers.background import BackgroundScheduler


db_connector = DBConnector()
redis_connector = RedisConnector()
email_sendor = EmailSendor()

def start_collect(url) :
    price_collector = PriceCollector()
    
    soup = price_collector.get_product_url_response_html(url[1])
    price_info = price_collector.get_price_info_in_url_response_html(soup)
    
    return (
        # random.randint(0, 100), random.randint(10000, 100000), random.randint(10000, 100000), random.randint(1, 4)
        price_info["discount"],price_info["origin_price"],price_info["sale_price"], url[0]
        )

def send_url_to_user(updated_url) :
    for info in updated_url :
        for url_id, info in info.items() :
            data = db_connector.get_user_use_url(url_id)
            user_ids = [id["user_id"] for id in data]
            email_sendor.send(user_ids, *create_msg(info) )

def create_msg(data) :
    before = str(data["before"]["sale_price"])
    after = data["after"]["sale_price"]
    title = "가격 인하 알림"
    msg = f"장바구니에 담으신 상품의 가격이 내려갔습니다. \n {before}원 -> {after}원"
    
    return (title, msg)
    
    
        
async def main() :
    loop = asyncio.get_event_loop()
    futures = []
    result = []
    urls = db_connector.get_all_urls()
    
    pool = None
    for url in urls:
        # if i % 5 == 0 :
        #     pool = concurrent.futures.ThreadPoolExecutor()
        futures.append(loop.run_in_executor(None, functools.partial(start_collect, url)))

    for future in asyncio.as_completed(futures):
        result.append(await future)
    
    
    db_connector.save_price_data(result)
    updated_info = redis_connector.set_price_info(result)
    send_url_to_user(updated_info)
    
async def start() :
    await main()
    # cron_min = aiocron.crontab('*/1 * * * *', func=main, start=True)
    
    # while True :
    #     await asyncio.sleep(1)
        
if __name__ == "__main__" :    
    asyncio.run(start())