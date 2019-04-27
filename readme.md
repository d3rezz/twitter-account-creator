# Twitter Account Creator - old (2014)
Script for creating Twitter accounts using an old mobile http only endpoint without need to enter captchas (2014). This endpoint has since been updated and no this script no longer works.

Wrote this for winning a voting competition between portuguese Universities organized by Red Bull. I quickly put this together in python with the mechanize scraping module for easily navigating the Twitter website.


## Competition 
The competition allowed voting through Facebook, Twitter or email.
Automatically creating accounts with Facebook proved though as they required inputing a phone number. For creating accounts with Twitter, no phone number was required, but a captcha had to be sovled, preventing multiple accounts to be created quickly.

I remembered from another write up I had read, that Twitter still had an old mobile http version of the website http://mobile.twitter.com/signup (think WAP era) with no JS or captchas which proved very easy to crawl. After writing the script to automatically create the Rwitter accounts createaccount.py, another script was created to log in the competition website and vote. The competition did not require the Twitter accounts to verify their email so this simplified the account creation a lot.
The mobile endpoint has since been updated.

Other alternatives would have included creating temporary email accounts as services such as yopmail, 10minutemail ... which were not blacklisted from voting in the competition. 


## Future improvements

Although this proved enough for us to win, possible improvements at the time would have been:

- Coming up with real First and Last names by randomly sampling from a list of names and then taking the first suggestion for the username from Twitter. In case the competition judges wanted to investigate the votes coming from this bot, this would make it much harder than having all bot usernames start with the same prefix;
- spawn multiple processes (ie. python's multiprocess module) instead of manually running the script many times;
