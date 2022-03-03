# Nintendo Rewards Bot
[@my_rewards_bot](https://twitter.com/my_rewards_bot)

A Twitter bot that highlights catalogue and inventory changes for [My Nintendo](https://my.nintendo.com/) rewards.

## Before you start
The [My Nintendo](https://my.nintendo.com/) website redirects their users to different reward pages based on their IP address. The physical rewards catalogue in particular, might not work in your country of residence. 

### Validating applicability
#### Digital rewards
1. Go to [My Nintendo](https://my.nintendo.com/)
2. Navigate to _Redeem Points_ > _Smart device/PC rewards_
3. Access your browser's developer tools
4. Under _Elements_ (Chrome) or _Inspector_ (Firefox), search for `embeddedResponses: JSON.parse`. 

If the string is found and is followed by product information, digital products can be identified.

#### Physical rewards
1. Go to [My Nintendo](https://my.nintendo.com/)
2. Navigate to _Redeem Points_ > _My Nintendo Store rewards_
3. Ensure that the appropriate region was selected, displayed on the bottom-right of the page
4. Access your browser's developer tools
5. Under _Elements_ (Chrome) or _Inspector_ (Firefox), search for `__NEXT_DATA__`. 

If the string is found and is followed by product information, physical products can be identified.

## Installation 
### Prerequisites
* A Twitter Developer account with _elevated_ access
* Read and write premissions to a MongoDB server

### Setting up
1. Via the [Twitter Developer's portal](https://developer.twitter.com/en/portal/), create a project with _Read and write_ access
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
7. In MongoDB, create a `db` for this project 
8. Modify `src/config.py` with your:
   * Environment variable names (step 6)
   * Database's URI
   * `db` name (step 7)
9. Ensure that your MongoDB server is running 
10. Modify `src/consts.py` with the URLs for the:
   * Digital rewards page
      * [My Nintendo](https://my.nintendo.com/) > _Redeem Points_ > _Smart device/PC rewards_
   * Physical rewards page
      * [My Nintendo](https://my.nintendo.com/) > _Redeem Points_ > _My Nintendo Store rewards_
   * My Nintendo Rewards' product path 
      * In the My Nintendo Rewards store, click on a product and copy the link, excluding the product name
      * Ex: https://www.nintendo.com/en-ca/store/products/my-nintendo-game-card-case/, only copy https://www.nintendo.com/en-ca/store/products/

## Execution
1. Run `main.py`
2. (Optional) Set up a cron to automatically run `main.py`

### Additional notes
Upon your first execution:
* Chromium will be installed (if it is not already on your system)
* Every item in the catalogue will be tweeted as \[ NEW \]. 
  *  To by-pass this, prior to your first execution, comment out `twitter.post_tweet(msg)` to populate your database
  *  Afterwards, do not forget to comment it back in
