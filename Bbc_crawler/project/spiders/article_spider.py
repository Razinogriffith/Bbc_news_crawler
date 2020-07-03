import scrapy
from ..items import ArtscrapItem
from scrapy.spiders import CrawlSpider
class ArticleSpider(CrawlSpider):
    '''
    DESCRIPTION:
    ------------
    * This class inherits the 'CrawlSpider' class of Scrapy.
    * It defines crawler for BBC News Website.
    '''
    name='bbc'
    start_urls=[
        'https://bbc.com/',
        
    ]
    def xpath_for_class(self,classname):
        '''
        DESCRIPTION:
        ------------
        * returns xpath for specific class
        PARAMETERS:
        ------------
        1 classname : the name of the wanted class 
        '''
        return "*[contains(concat(' ', @class, ' '), ' " + classname + " ')]"
    
    def get_first(self,in_list, if_empty):
        '''
        retruns first element in the list
        if list is empty  returns if_empty
         
        '''
        if len(in_list) > 0:
            return in_list[0]
        else:
            return if_empty

    def parse(self,response):
        '''
        DESCRIPTION:
        -----------
        * This function is called for parsing every URL encountered,
          starting from 'start_urls'.
        * In this function required information is fetched from
          the web page and stored in Item object.
        PARAMETERS:
        ----------
        1. response object of Web page.
        '''
        item=ArtscrapItem()
        articles=response.xpath("//"+self.xpath_for_class("media__content"))
        for article in articles:
            title = self.get_first(article.xpath(self.xpath_for_class('media__title') + "/a/text()").extract(), "").strip(' \n')
            if title is not "":
                item["title"] = title
                item["summary"] = self.get_first(article.xpath(self.xpath_for_class('media__summary') + "/text()").extract(), "").strip(' \n')
                item["tags"] = self.get_first(article.xpath(self.xpath_for_class('tag') + "/text()").extract(), "").strip(' \n')
                article_url = ''.join(article.xpath(self.xpath_for_class("media__title") + "/a/@href").extract())
                item["url"] = response.urljoin(article_url)
                yield scrapy.Request(item["url"], callback=self.parse_contents, meta=item)

    def parse_contents(self, response):
        '''
        DESCRIPTION:
        -----------
        * This function is called for crwling info from artcils URL,
          '.
        * In this function required information is fetched from
          the web page and stored in Item object.
        PARAMETERS:
        ----------
        1. response object of Web page.
        '''
        item = response.meta
        item["header"] = self.get_first(
            response.xpath("//" + self.xpath_for_class("story-body__h1") + "/text()").extract(), "").strip(' \n')
        body_list = response.xpath("//" + self.xpath_for_class("story-body__inner") + "//p/text()").extract()
        item["body"] = ' '.join(body_list).strip(' \n')
        yield item
        

              
            
        