import time


def convert_time(epoch_time: int) -> time.struct_time:
    return time.localtime(epoch_time)


def get_date() -> time.struct_time:
    today = time.time()
    today = today - (today % (24 * 60 * 60))
    timezone = time.strftime("%Z", convert_time(today))

    if timezone == "EST":
        today += 5 * 60 * 60
    elif timezone == "EDT":
        today += 4 * 60 * 60
    return convert_time(today)


def format_time(struct_time: time.struct_time) -> str:
    return time.strftime("%b %d, %Y %H:%M %Z", struct_time)
