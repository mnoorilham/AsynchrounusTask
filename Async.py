import asyncio
import time

async def sleep():
    print(f'Waktu: {time.time() - start:.2f}')
    await asyncio.sleep(1)

async def sum(name, numbers):
    total = 0
    for number in numbers:
        print(f'Tugas {name}: Mengerjakan {total}+{number}')
        await sleep()
        total += number
    print(f'Tugas {name}: Total selesai = {total}\n')

start = time.time()

loop = asyncio.get_event_loop()
tasks = [
    loop.create_task(sum("A", [1, 2])),
    loop.create_task(sum("B", [1, 2, 3])),
]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()

end = time.time()
print(f'Waktu: {end-start:.2f} detik')