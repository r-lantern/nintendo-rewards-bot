from src import consts


class Reward:
    def __init__(self, data: dict, status=consts.STATUS_NEW):
        self.status = status
        self.data = data
