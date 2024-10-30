from cothread import catools
from cothread.catools import ca_nothing
from logging import logging

def updateBlock(iocPrefix: str, blockSchema: dict) -> list:
    blockName = blockSchema["name"]
    for key, value in blockSchema["puts"].items():
        putCommand = f"{iocPrefix}:{blockName}:{key}".upper()
        value = str(value)

        try:
            if ";;" in value:
                value = value.split(";;")
                response = caput(putCommand, value[0], hasType=value[1])
            else:
                response = caput(putCommand, value)
        except ca_nothing as e:
            print("Does this PV exist?")
            print(f"Error: {e}")
            exit()


        print("Response:")
        print(response)
        print("\n")


def caget(pv: str) -> str:
    return catools.caget(pv)

@logging
def caput(pv: str, val: str, hasType=None) -> str:
    print(f"Running caput '{pv}' '{val}' {f'with type {hasType}' if hasType else ''}")
    if hasType:
        match hasType:
            case "DBR_STRING":
                return catools.caput(pv, val, datatype=catools.DBR_STRING)
            case _:
                print("Type not supported. Continuing with string")
        

    return catools.caput(pv, val)