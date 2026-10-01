import asyncio
import time

## Coroutine Function
async def main():
    print("Hello") # This will print imediately
    await asyncio.sleep(3) # This Thread is idle here # here addingn Await make sure it wait for 3 second 
                            ## But the thread is not locked and can be assigned to other task
    print("World") # This will be executed right after the thread is idle
  
# Run the main coroutine  
asyncio.run(main())