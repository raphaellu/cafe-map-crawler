# cafe-map-crawler
## Description
A web crawler that collects the basic information of 82,463 restaurants in Shanghai, including title, rate, area, address and average price per person for every restaurant.

## Purpose
I implemented this project mainly to get familiar with web crawling, especially how to deal with __(1) HTML parsing/server requesting__ and __(2) bypassing scraping restrictions imposed by the website__.

I think it would be nice to know how to prevent malicious users from scraping valuable data on company's website. However, as that one cannot expect a coach not knowing about the game to be good, in order to learn anti-scraping techniques, one has to know how to scrape and avoid anti-scraping restrictions first. I found it very interesting to explore different ways to bypass the website's prevention of crawling while gracefully following the robot's agreement. (and crawling some websites can be very tough!)

## Dependencies
* [Scrapy 1.1](http://scrapy.org/)
* [Python 2.7](https://www.python.org/download/releases/2.7/)
* [MongoDB 3.0.6](https://www.mongodb.com/)
* [PyMongo](https://api.mongodb.com/python/current/)

## Comments
__[More details](http://raphaellu.com/blog/2016/07/cafe-map/)__

All data is collected from [dianping](http://www.dianping.com/) public pages and only for academic/non-profit use. Data has not been distributed anywhere.
