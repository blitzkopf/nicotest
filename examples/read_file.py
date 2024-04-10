import asyncio
import xml.etree.ElementTree as ET

from nicostick.controller import Controller


async def main():

    ctrl = Controller('172.25.115.56', password='z')

    await ctrl.start()
    file_data = await ctrl.read_file('Show1/show_map.xml')
    print(file_data)
    root = ET.fromstring(file_data)
    print(root.tag)
    for item in root.findall('Scenes/item'):
        print(item.attrib)
        print(item.find('Scene').attrib['name'])
    await ctrl.stop()


if __name__ == "__main__":
    asyncio.run(main())
