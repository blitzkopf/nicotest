import asyncio
import logging

from nicostick.controller import Controller

logging.basicConfig(level=logging.DEBUG)

scene = 4
async def main():

    ctrl = Controller('172.25.115.56',password='z')
    await ctrl.start()

    await ctrl.start_scene(scene, 0, 0, 0, 0x12345600)
    await ctrl.start_scene(scene, 0, 0, 0, 0x12345601,cmd=0x07)
    await asyncio.sleep(1)
    await ctrl.start_scene(scene, 0, 0, 0, 0x0000003f,cmd=0x07)
    await asyncio.sleep(1)
    await ctrl.start_scene(scene, 0, 0, 0, 0x00003f00,cmd=0x07)
    await asyncio.sleep(1)
    await ctrl.start_scene(scene, 0, 0, 0, 0x003f0000,cmd=0x07)
    await asyncio.sleep(1)
    await ctrl.start_scene(scene, 0, 0, 0, 0x003f3f3f,cmd=0x07)
    await asyncio.sleep(1)
    await ctrl.stop()

if __name__ == "__main__":
    asyncio.run(main())
