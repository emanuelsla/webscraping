# webscraping

This is the branch for Bamberg Winter School 2020 for the course "Python Programming for Social Sciences: Collecting, Analysing and Presenting Social Media Data (WC105)".

## Contents
1. The file "wikipedia_game.ipynb" derives a function to randomly follow Wikipedia links until the initial Wikipedia page is reached. The function is only dependent on a single input url, which needs to be provided as string.

2. The file "stock_price_monitor.ipynb" views stocks on boerse.de. The variables of interest are the current stock price, the 24h relative stock development and the 24h absolute stock development. The derived function takes three parameters as input:
    * url: a url of boerse.de that yields to a stock. It needs to be provided as string.
    * name: the name of the stock as string.
    * minutes: a integer, which stands for the number of minutes to watch the stock. It is equal to the number of requests.
    
3. The file "insta_image_reader.ipynb" derives a function to read images from Instagram that are related to a certain hashtag. The output are images as png. It has the following input parameters:
    * hashtag: a valid Instagram hashtag as string.
    * max_pictures: integer that stands for the maximum number of images to download.
    * directory: a string of the working directory in order to save the images.
