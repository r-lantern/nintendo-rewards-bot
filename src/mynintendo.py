from typing import List
import requests_html
import requests
import json

import src.consts as consts
from src import error


def get_store_request() -> requests.Response:
    session = requests_html.HTMLSession()
    req = session.get(consts.PAGE_REWARDS_STORE)
    try:
        req.html.render(retries=2, timeout=30)
    except requests_html.TimeoutError:
        session.close()
        raise error.SiteUnreachable
    session.close()
    return req


def get_rewards(req: requests.Response) -> List:
    html = req.html.html.split("\n")
    for line in html:
        if "embeddedResponses: JSON.parse" in line:
            break
    line = line.strip('embeddedResponses: JSON.parse("').rstrip('"),')
    line = line.encode("latin1", "ignore").decode("unicode-escape", "replace")
    response = json.loads(line)
    if "api_reward_list" in response:
        rewards = response["api_reward_list"]["data"]["items"]
        return rewards
    return None
