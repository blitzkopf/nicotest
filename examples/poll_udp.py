import asyncio
import logging
import socket
import struct

logging.basicConfig(level=logging.DEBUG)

addr = '172.25.115.69'


def poll_request_encode(self, ID=b'LSAG_ALL'):
    XHL_VERSION = 0x12
    return struct.pack('<8sHI2x', ID, 0x00, XHL_VERSION)


# I have not seen the Stick respond on UDP, so we will just fire and forget
async def send_udp(data):
    print(f'Sending UDP: {data.hex()}')
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        s.sendto(data, (addr, 2430))
        data = s.recvfrom(1024)
        print('Received UDP:', data.hex())


async def send_poll(ID=b'LSAG_ALL'):
    data = poll_request_encode(ID)
    await send_udp(data)


async def main():

    await send_poll()


if __name__ == "__main__":
    asyncio.run(main())
