import time


def convert_time(epoch_time: int) -> time.struct_time:
    return time.localtime(epoch_time)


def get_current_time() -> time.struct_time:
    today = time.time()
    return convert_time(today)


def format_time(struct_time: time.struct_time) -> str:
    return time.strftime("%b %d, %Y %H:%M %Z", struct_time)
