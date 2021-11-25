from src import utils


def get_title(product: dict) -> str:
    return product["title"]


def get_start_time(product: dict) -> str:
    return utils.convert_time(product["beginsAt"])


def get_end_time(product: dict) -> str:
    end_time = "Undefined"
    if product["endsAt"]:
        end_time = utils.convert_time(product["endsAt"])
    return end_time


def get_category(product: dict) -> str:
    return product["category"].replace("_", " ").title()


def get_points_value(product: dict) -> str:
    return product["points"][0]["amount"]


def get_points_type(product: dict) -> str:
    # points type in one of two locations
    if "key" not in product["points"][0]:
        points_type = product["points"][0]["category"]
    else:
        points_type = product["points"][0]["key"]
    return points_type.replace("_", " ").title()


def get_url(product: dict) -> str:
    return product["links"]["myNintendo"]["href"]


def get_metadata(self, product: dict) -> dict:
    data = {
        "title": self.get_title(product),
        "start_time": self.get_start_time(product),
        "end_time": self.get_end_time(product),
        "category": self.get_category(product),
        "points_value": self.product(product),
        "points_type": self.product(product),
        "url": self.product(product),
    }
    return data


def get_stock(product: dict) -> bool:
    if "stock" in product:
        return product["stock"]["available"]
    return None
