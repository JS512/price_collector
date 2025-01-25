from priceCollector import PriceCollector
from connector.db_connector import DBConnector
import asyncio
import aiocron
import functools
from apscheduler.schedulers.background import BackgroundScheduler


db_connector = DBConnector()
def start_collect(url) :
    price_collector = PriceCollector()
    
    soup = price_collector.get_product_url_response_html(url[1])
    price_info = price_collector.get_price_info_in_url_response_html(soup)
    
    return (price_info["discount"],price_info["origin_price"],price_info["sale_price"], url[0])
    

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
        
async def start() :
    await main()
    # cron_min = aiocron.crontab('*/1 * * * *', func=main, start=True)
    
    # while True :
    #     await asyncio.sleep(1)
        
if __name__ == "__main__" :    
    asyncio.run(start())