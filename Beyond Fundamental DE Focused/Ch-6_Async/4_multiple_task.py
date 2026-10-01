import asyncio
import time
# First Task
async def api_call(url:str,delay:int=3):
    print(f"Getting Data from {url}")
    await asyncio.sleep(delay)
    print(f"Data Fetched from {url}")
    

# Second Task
async def execution():
    time.sleep(10)
    print("Exetution Completed")

# Third Task
async def transformation():
    asyncio.sleep(5)
    print("Transformation Completed")
    
async def main():
    
    tasks=await asyncio.gather(
        api_call('https://api1.com'),
        execution(),
        transformation()
    )

asyncio.run(main())