class Error(Exception):
    pass


class SiteUnreachable(Error):
    """Unable to reach My Nintendo website"""

    pass


class RewardsStringNotFound(Error):
    """Unable to find My Nintendo rewards string"""

    pass
