import time


def convert_time(epoch_time: int) -> str:
    return time.strftime("%b %d, %Y %H:%M %Z", time.localtime(epoch_time))
