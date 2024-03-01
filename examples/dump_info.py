import asyncio
import logging
from sys import argv

from nicostick.controller import Controller

logging.basicConfig(level=logging.DEBUG)


async def main(address):

    ctrl = Controller(address)
    await ctrl.start()
    await ctrl.initialize()
    await asyncio.sleep(2)
    print(ctrl._state)
    print("Controller Info:")
    print(ctrl.zones)
    print(ctrl.scenes)
    await asyncio.sleep(40)
    await ctrl.send_query_zone_status(0)
    await asyncio.sleep(5)
    await ctrl.stop()
    await asyncio.sleep(5)


if __name__ == "__main__":
    asyncio.run(main(argv[1]))
