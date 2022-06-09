import asyncio
import time

# task = promise


async def outrafuncao():
    await asyncio.sleep(10)
    print(f"momento outrafuncao: {time.strftime('%X')}")

    print("Minha mensagem 1")


async def outrafuncao2():
    await asyncio.sleep(2)
    print(f"momento outrafuncao2: {time.strftime('%X')}")

    print("Minha mensagem 2")


async def funcao():
    print(f"iniciou: {time.strftime('%X')}")
    task = asyncio.create_task(outrafuncao())
    task1 = asyncio.create_task(outrafuncao2())
    print(f"terminou: {time.strftime('%X')}")

    await task
    await task1


asyncio.run(funcao())
