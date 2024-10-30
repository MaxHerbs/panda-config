from datetime import datetime
import atexit


thisLog = f"logs/log.{datetime.now().strftime('%d.%m.%Y.%H.%M.%S')}.txt"
f = open(thisLog, "w")

def closeLogFile():
    f.close()
atexit.register(closeLogFile)


def logging(func):
    def caput(pv: str, val: str, hasType=None) -> str:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] ")
        f.write(f"Ran caput `{pv}` `{val}`\n")
        return func(pv, val, hasType)


    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {func.__name__} called with args: {args} and kwargs: {kwargs}\n")
        return func(*args, **kwargs)

    localFuncs = list(locals())
    if func.__name__ in localFuncs:
        return locals()[func.__name__]
    else:
        return wrapper



if __name__ == "__main__":
    pass