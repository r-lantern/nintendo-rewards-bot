from typing import List
import requests_html
import requests
import json

import src.consts as consts


def get_request(page: str) -> requests.Response:
    session = requests_html.HTMLSession()
    req = session.get(page)
    req.html.render(retries=2, timeout=30)
    session.close()
    return req


def get_digital_rewards_req() -> requests.Response:
    return get_request(consts.PAGE_DIGITAL_REWARDS)


def get_physical_rewards_req() -> requests.Response:
    return get_request(consts.PAGE_PHYSICAL_REWARDS)


def get_digital_rewards() -> List:
    req = get_digital_rewards_req()
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


def get_physical_rewards() -> List:
    req = get_physical_rewards_req()
    html = req.html.find("#__NEXT_DATA__", first=True).text
    response = json.loads(html)
    items = response["props"]["pageProps"]["page"]["content"]["merchandisedGrid"][0]
    return items
