import time
import sys
from types import TracebackType

def animates():
    animation = "|/-\\"

    for i in range(20):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
    return True        