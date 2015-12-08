# GiP-radio-categories
Python script to download everything from a specific Radio Category with get_iplayer

When the BBC changed the way that programs could access feed information on what was available in iPlayer, this prevented get_iplayer (https://squarepenguin.co.uk/) from dowloading everything in a particular radio category. 

This script Web-scrapes the paginated feed for the particular category (first case is Sci-Fi and Fantasy - options to change category to be added later) and then calls get_iplayer with the PIDs from the URLs retrieved.

Prerequisites:
  Python 2.7,
  requests,
  BeautifulSoup,
  get_iplayer
