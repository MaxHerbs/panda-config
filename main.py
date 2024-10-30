import yaml
import os
from interface import updateBlock, caput, caget
import time

def parseConfig() -> dict:
    if not os.path.exists('config.yaml'):
        raise FileNotFoundError("config.yaml not found")
    
    with open('config.yaml') as file:
        config = yaml.safe_load(file)
    return config

def main():
    config = parseConfig()
    iocPrefix = config['iocPrefix']

    for block in config["blocks"]:
        updateBlock(iocPrefix, block)

    caput(f"{iocPrefix}:PCAP:ARM", "1")
    time.sleep(0.8)
    val = caget(f"{iocPrefix}:COUNTER2:OUT")
    print(val)

if __name__ == "__main__":
    main()