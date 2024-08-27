# NOTES FOR WEB SCRAPING

## BASICS

A webpage is made up of HTML for structure and CSS for styling. In web scraping, the class or ID of the title, paragraph, etc., are targeting to extract/scrape data from the web page. 

## `robots.txt` file and web scraping rules

Rules and laws regarding web scraping are specified in a file named `robots.txt`

This file tells us the directories the website does not want a scraper to crawl. 

Scrapy automatically follows the rules of `robots.txt` and does not crawl the URL links given in the `robots.txt`

If you don't want to follow the rules of `robots.txt` file, then change the value of `ROBOTSTXT? OBEY` to `False` in `settings.py` in the code directory.

## Virtual Environment

Virtual environment creates a virtual isolated environment where whatever we install in this does not affect the rest of the computer.

## Steps to follow

1. Create virtual env

```
$ python -m venv venv

$ source myvenv/bin/activate
```

- pip install `pipenv`
- create virtual environment: `virtualenv .`
- activate virtual environment in 
    - linux & mac: `source ./bin/activate`
    - windows: `.\Scripts\activate`

2. Install Scrapy using `pip install Scrapy`

3. `scrapy startproject projectname`

## SCRAPY FILE STRUCTURE

Spider is a python program that scrapes other websites. 

### components of `settings.py` - 

- BOT is anything that automates the writing of code 
- USER_AGENT authenticates our identity to the browser 
- CONCURRENT_REQUESTS - a bunch of requests made at the same time is concurrent requests. A large number of concurrent requests can overload the server of the website, hence there is a default value of 16 concurrent requests. 

### components of `items.py`
    
a function is already created where fields that are needed to be scraped can be defined. 

### components of `pipeline.py`

after scraping the data, we should store it somewhere like JSON file, SQL database or MongoDB database. This is done by pipeline stored in pipeline file. 

### components of `middleware.py`

When you are sending a request to a website you can add some stuff to that request, like user agent, adding proxies to a request proxy (using different IP addresses to bypass restrictions). Adding proxies is done using middleware. 

### Running the spider

to run the spider created in Spider folder, in terminal change directory to `quotetutorial` and then run `scrapy crawl spidername`

#### extracting ata with CSS selectors

`response.css('title::text').extract()`

here the response is parsed for it's CSS selectors, hence this method is extracting the data with CSS selectors

`$ scrapy shell "website URL"`

running this is in terminal is going to open a Scrapy shell that opens terminal inside the scrapy

#### extracting data with XPATH

used to get value od Anchor tags and href in an easy way. it can be done using css seelctors also. 

`response.xpath("//title/text()").extract()`

`response.xpath("//span[@class='text']/text()").extract()`

`response.css("li.next a").xpath("@href").extract()` - extracts the href values of the anchor tags in list with "next" as its class

`response.css("a").xpath("@href").extract()` - extracts all the values of href in the anchor tags

### ITEM CONTAINERS

Scrapy stores the extracted data in the "yield" python dictionary. Dictionaries can be inconsistent when the amount of data is huge. So, extracted can be stored in temporary containers (item containers) and then store these in a database. Item.py file is used to create the item containers. 

`items.py` file is used to create item containers. 

### STORING IN JSON FILE

```
cd projectfolder

scrapy crawl spidername -o items.json
e.g. scrapy crawl quotes -o items.json

scrapy crawl spidername -o items.csv
e.g. scrapy crawl quotes -o items.csv

scrapy crawl spidername -o items.xml
e.g. scrapy crawl quotes -o items.xml
```

this command creates a new json file and stores the data in it. 

scraped data --> item containers --> json/csv/xml files

### USING PIPELINES TO STORE DATA

scraped data --> item containers --> pipleine --> SQL/Mongo database

pipleines need to be activated in the `settings.py` file. 

```
ITEM_PIPELINES = {
    "quotetutorial.pipelines.QuotetutorialPipeline": 300,
}
```

lower the number, higher the priority of the pipeline. 

these aboves lines need to be uncommented in the settings.py file. "300" assigns the priority of the pipeline. If multiple pipelines are used in the project, new pipelines must be added in the ITEM_PIPELINES in settings.py and priority has to be assigned to it. Lower value implies higher priority. Pipeline with higher priority will be executed first. 

### STORING DATA FROM PIPELINE TO SQLite DATABASE

a SQLite connection is created in the `database.py file` which consists of making a connection to the database, creating the structure of the database using cursor and then committing it. 

whenever the instance of QuotetutorialPipeline() class is called, the objects looks for an initialization method. 

in SQLite, only one tag is stored in the 'tags' column. for storing all the tags, we need to create a foreign key and connect that to the table. 

### STORING DATA FROM PIPELINE TO MONGODB DATABASE

steps:

1. install mongoDB - install with mongodb compass
https://docs.mongodb.com/manual/administration/install-community/

https://www.mongodb.com/products/compass

2. create a folder /data/db
3. run the mongod.exe once
4. install pymongo in IDE
5. make sure your pipeline is activated
6. write the code in mongodb
6. see the saved data in mongodb compass

link to the video: https://www.youtube.com/watch?v=djfnjtYB2co&list=PLhTjy8cBISEqkN-5Ku_kXG4QW33sxQo0t&index=18

### WEB CRAWLING AND FOLLOWING LINKS

this works for websites where `next` button is there for the different pages or crawling other links present in the website

Scrapy should start crawling on the first page, then find the `next` button and then start crawling that link. 

one more condition should be added for when there are no more pages to follow. 






