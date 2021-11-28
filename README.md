# Nintendo Rewards Bot
[@my_rewards_bot](https://twitter.com/my_rewards_bot)

A Twitter bot that highlights catalogue and inventory changes for [My Nintendo](https://my.nintendo.com/reward_categories) rewards.

## Before you start
The [My Nintendo](https://my.nintendo.com/) website redirects their users to different reward pages based on their IP address. For their physical rewards catalogue in particular, this script may not work in your counrtry of residence. 

### How to check
1. Go to the [My Nintendo](https://my.nintendo.com/) website
2. Click on _Redeem Points_ (Name may vary)
3. Click on _Nintendo Store Rewards_ (Name may vary)
4. Access your browser's developer tools
5. Under _Elements_ (Chrome) or _Inspector_ (Firefox), search for `embeddedResponses: JSON.parse`
   * If the string is found, and what follows looks like product information, this project is applicable to you
   * If not, this script will not be able to scrape your country's My Nintendo physical rewards catalogue, but may still work for their digital rewards. To check, simply click on any other reward categories and repeat steps 4 and 5.

## Installation 
### Prerequisites
* A Twitter Developer account with _elevated_ access
* Read and write premissions to a MongoDB server

### Setting up
1. Via the [Twitter Developer's portal](https://developer.twitter.com/en/portal/), create a project with Read and write access
2. Clone this repository
3. Install `requirements.txt`
   ```
   pip3 install -r requirements.txt
   ```
4. Set `pyppeteer_fix.sh` as an executable
   ```
   chmod +x pyppeteer_fix.sh
   ```
5. Run `pyppeteer_fix.sh` -- Written for Ubuntu 20.04 (Modifications may be required)
   ```
   ./pyppeteer_fix.sh
   ```
6. Set environment variables for your Twitter project's:
   * Consumer key
   * Consumer secret
   * Access token
   * Access secret
7. In MongoDB, create a `db` and `collection` for this project 
8. Modify `src/config.py` with your:
   * Environment variable names (step 6)
   * database's URI
   * db and collection names (step 7)

## Executing the script
1. Run `main.py`
2. (Optional) Set up a cron to automatically run `main.py`

### Additional Notes
Upon your first execution:
* Chromium will be installed (if not already on your system)
* Every item in the catalogue will be tweeted as \[ NEW \]
