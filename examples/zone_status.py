import asyncio
import logging

from nicostick.controller import Controller

logging.basicConfig(level=logging.DEBUG)


async def main():

    ctrl = Controller('172.25.115.69')

    await ctrl.start()

    await ctrl.send_query_zone_status(0)
    await asyncio.sleep(3)
    await ctrl.start_scene(4, 0, 0, 0, 0)
    await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(main())
