import asyncio
import logging

from nicostick.controller import Controller

logging.basicConfig(level=logging.DEBUG)


async def main():

    ctrl = Controller('172.25.115.69')

    # await ctrl.start_scene(5, 0, 0, 0,0)
    await ctrl.start()
    await ctrl.send_poll()
    await asyncio.sleep(5)
    print(f'serial:{ctrl._state.serial}')
    await ctrl.stop()


if __name__ == "__main__":
    asyncio.run(main())
