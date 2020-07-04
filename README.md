# BBC news Crawler
this is an api that collects  articles from BBC.com using scrapy and stores it in Mongodb atlas
## Description
- this application crawls news Articles from BBC.com using [scrapy](https://www.scrapy.org)
- it cleans the articles to obtain only information relevant to the news story, e.g.title,summary,  headline,articles text, article url.
- it store the data in a hosted Mongo database, [MongoDB Atlas](https://www.mongodb.com/cloud/atlas), for subsequent search and retrieval. 
- Search REST APIs are provided  to be able to access the content in the mongo database.
    - using the Rest API ths user can search for :
        - all news in the database
        - news that contains a given keyword in tags
        - news that contains a given keyword in body
        - news that contains a given keyword in heading
## project Structure:
- Bbc_crawler/ holds the Scrapy Spider for the BBC News website.
- Rest_API/ holds an implementation of search REST API, for BBC News Crawler.
    - the search API  gets the data from the mongodb Database 
    - four  search APIs are implemanted :
        1 - to fetch all the article news in the database  : http://127.0.0.1:5000/news
        2 - to fetch all the articles related to given keyword in tags : http://127.0.0.1:5000/tags/<keyword>
        3 - to fetch all the articles related to given keyword in body : http://127.0.0.1:5000/body/<keyword>
        4 - to fetch all the articles related to given keyword in heading : http://127.0.0.1:5000/header/<keyword>
## Run 
- to run the crawler execute command 
```bash
cd BBc_crawler
scrapy crawl bbc
```
this application uses DeltaFetch librery to avoid re-storing already stored articles
If the user want to re-scrape pages, he can reset the DeltaFetch cache by passing the deltafetch_reset argument to the spider:
```bash
scrapy crawl bbc -a deltafetch_reset=1
```
- to start the rest API  oyu just need to execute the python script

```bash
cd Rest_API
python ArticleCrawlerAPi.py

```

 

