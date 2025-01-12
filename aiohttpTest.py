# import aiohttp
# import asyncio
# import time
# import requests


# count = 500

# def main3() :
#     url_list = [
#         'https://www.baidu.com/' for i in range(count)
        
#     ]
#     result = [requests.get(url) for url in url_list]
#     return result
# async def get(url) :
#     return requests.get(url)
    
# async def main2() :
#     url_list = [
#         'https://www.baidu.com/' for i in range(count)
        
#     ]
#     tasks = [asyncio.create_task(get(url)) for url in url_list]
#     tasks_results = await asyncio.gather(*tasks)
#     return tasks_results


# async def main():

#     async with aiohttp.ClientSession() as session:
#         for i in range(count) :
#             async with session.get('https://www.baidu.com/') as response:
#                 # f = open('./t1.txt', 'a') # 파일에 텍스트 쓰기
                
#                 # print("Status:", response.status)
#                 # print("Content-type:", response.headers['content-type'])

#                 html = await response.text()
            
#             #     f.write(html)
#             #     f.write("\n\n\n\n=================================================================")
#             # f.close()

            
            
            
# s = time.time()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(main())
# print(time.time()-s)
# loop.close()    
            
# # s = time.time()
# # loop = asyncio.get_event_loop()
# # loop.run_until_complete(main2())
# # print(time.time()-s)
# # loop.close()


# # s = time.time()
# # main3()
# # print(time.time()-s)


import asyncio
import functools
import requests
import time
import concurrent.futures

ts = time.time()
loop = asyncio.get_event_loop()

# @asyncio.coroutine
async def do_checks():
    futures = []
    pool = None
    for i in range(10000):
        # if i % 5 == 0 :
        #     pool = concurrent.futures.ThreadPoolExecutor()
        futures.append(loop.run_in_executor(pool, functools.partial(requests.get, "http://127.0.0.1:5000")))

    for req in asyncio.as_completed(futures):
        resp = await req
        # done = req.done()
        # print(resp.status_code)

loop.run_until_complete(do_checks())
te = time.time()
print("Version A: " + str(te - ts))


# import asyncio
# from aiohttp import ClientSession

# async def fetch(url, session):
#     async with session.get(url) as response:
#         delay = response.headers.get("DELAY")
#         date = response.headers.get("DATE")
#         # print("{}:{} with delay {}".format(date, response.url, delay))
#         return await response.text()


# async def bound_fetch(sem, url, session):
#     # Getter function with semaphore.
#     # async with sem:
#     await fetch(url, session)


# async def run(r):
#     url = "http://127.0.0.1:5000"
#     tasks = []
#     # create instance of Semaphore
#     # sem = asyncio.Semaphore(1000)

#     # Create client session that will ensure we dont open new connection
#     # per each request.
#     async with ClientSession() as session:
#         for i in range(r):
#             # pass Semaphore and session to every GET request
#             task = asyncio.ensure_future(bound_fetch(1, url, session))
#             tasks.append(task)

#         responses = asyncio.gather(*tasks)
#         await responses

# import time
# number = 10000
# s = time.time()
# loop = asyncio.get_event_loop()
# loop.run_until_complete(run(number))
# print(time.time()-s)
# # loop.close()    