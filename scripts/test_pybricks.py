import pybricksdev as pbd
from pybricksdev.connections.pybricks import PybricksHub
from pybricksdev.ble import find_device #, nus
import logging
import sys
import asyncio
from contextlib import redirect_stdout

async def main():
    address = await find_device('Pybricks Hub')
    #print(address)

    hub = PybricksHub()
    await hub.connect(address)
    print('hub connected:', hub.connected)
    
    
    await hub.run('../programs/mvp_test.py')
    
    await hub.disconnect()

if __name__ == "__main__":
    with open('mvp_data.log', 'w') as file:
        with redirect_stdout(file):
            logging.basicConfig(stream=sys.stderr, level=logging.ERROR)
            asyncio.run(main())
