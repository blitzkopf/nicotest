import asyncio
import logging
from sys import argv

from nicostick.controller import Controller

logging.basicConfig(level=logging.DEBUG)


async def main(address):

    ctrl = Controller(address)
    await ctrl.start()
    # await ctrl.send_get_salt()
    # salt = await ctrl.get_salt()
    # print(f"Salt: {salt.hex()}")
    auth_code = await ctrl.authenticate(b'Stick_3A', b'remote', 'z')
    print(f"Auth result: {auth_code:x}")
    await asyncio.sleep(10)
    await ctrl.stop()


if __name__ == "__main__":
    asyncio.run(main(argv[1]))
