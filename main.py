from priceCollector import PriceCollector
import asyncio
import aiocron
import functools
from apscheduler.schedulers.background import BackgroundScheduler

def start_collect(url) :
    price_collector = PriceCollector()
    
    soup = price_collector.get_product_url_response_html(url)
    price_info = price_collector.get_price_info_in_url_response_html(soup)
    return price_info

async def main() :
    loop = asyncio.get_event_loop()
    futures = []
    urls = [
        "https://www.goodwearmall.com/product/1P241029722581/detail?trackNo=special&trackDtl=special_140180"
    ]
    pool = None
    for url in urls:
        # if i % 5 == 0 :
        #     pool = concurrent.futures.ThreadPoolExecutor()
        futures.append(loop.run_in_executor(None, functools.partial(start_collect, url)))

    for future in asyncio.as_completed(futures):
        future = await future
        print(future)
        
async def start() :
    cron_min = aiocron.crontab('*/1 * * * *', func=main, start=True)
    
    while True :
        await asyncio.sleep(1)
        
if __name__ == "__main__" :    
    asyncio.run(start())