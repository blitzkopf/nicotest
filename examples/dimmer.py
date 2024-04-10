import asyncio
import logging

from nicostick.controller import Controller

logging.basicConfig(level=logging.DEBUG)

scene = 7
async def main():

    ctrl = Controller('172.25.115.56',password='z')
    await ctrl.start()

    await ctrl.start_scene(scene, 0, 0, 0, 0)
    await asyncio.sleep(1)
    await ctrl.start_scene(scene, 0, 500, 0, 0, cmd=0x05)
    await asyncio.sleep(1)
    await ctrl.start_scene(scene, 0, 1000, 0, 0, cmd=0x05)
    await asyncio.sleep(1)
    await ctrl.start_scene(scene, 0, 1500, 0, 0, cmd=0x05)
    await asyncio.sleep(1)
    await ctrl.start_scene(scene, 0, 2000, 0, 0, cmd=0x05)
    await asyncio.sleep(1)


    await ctrl.stop()

if __name__ == "__main__":
    asyncio.run(main())
