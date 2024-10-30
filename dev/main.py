import yaml


def parseConfig() -> dict:
    with open('config.yaml') as file:
        config = yaml.safe_load(file)
    return config


def main():
    config = parseConfig()
     
    for block in config["blocks"]:
        basePv = f"{config['iocPrefix']}:{block['name']}"
        puts = block["puts"]
        for put in puts:
           print(put)
           pv = basePv + buildPv(put)
           print("PV is: ", pv)

def buildPv(element) -> str:
    if type(element) == dict:
        print("Its layered!")
        for key, value in element.items():
            return f":{key}:" + buildPv(value)
    return f":{element}"


if __name__ == "__main__":
    main()