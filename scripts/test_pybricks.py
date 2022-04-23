import pybricksdev as pbd
from pybricksdev.connections.pybricks import PybricksHub
from pybricksdev.ble import find_device #, nus
import logging
import sys
import asyncio

async def main():
    address = await find_device('Pybricks Hub')
    print(address)

    hub = PybricksHub()
    await hub.connect(address)
    print('hub connected:', hub.connected)
    
    
    await hub.run('../programs/mvp_test.py')
    
    await hub.disconnect()

if __name__ == "__main__":
    logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    asyncio.run(main())
