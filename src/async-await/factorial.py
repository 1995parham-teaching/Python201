import asyncio
import time


async def async_sleep():
    print('sleep')
    await asyncio.sleep(1)


async def normal_sleep():
    print('sleep')
    time.sleep(1)


async def factorial(name, number):
    f = 1
    for i in range(2, number+1):
        print('Task {}: Compute factorial({})'.format(name, i))
        await async_sleep()
        f *= i
    print('Task {}: factorial({}) is {}\n'.format(name, number, f))


start = time.time()
loop = asyncio.get_event_loop()

tasks = [
    asyncio.ensure_future(factorial("A", 3)),
    asyncio.ensure_future(factorial("B", 4)),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print("Total time: {}".format(end - start))
