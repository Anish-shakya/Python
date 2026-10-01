import asyncio

async def api_call(url:str,delay:int):
    print(f"Getting Data from {url}")
    await asyncio.sleep(delay)
    print(f"Data Fetched from {url}")
    return f"{url} data"

async def main():
    ### Creating the task with Gather
    tasks = await asyncio.gather(
        api_call("https://api1.com",0),
        api_call("https://api2.com",10),
        api_call("https://api3.com",5),
        api_call("https://api4.com",10),
        api_call("https://api5.com",7),
    )
    
    # ## Dynamic approach using list comprehension
    # api_endpoints=[
    #     'https://api1.com',
    #     'https://api2.com',
    #     'https://api3.com',
    #     'https://api4.com',
    #     'https://api5.com',]
    
    # tasks = [api_call(url) for url in api_endpoints ]
    # result=await asyncio.gather(*tasks)
    
    print("All API Call Completed.")
    
asyncio.run(main())