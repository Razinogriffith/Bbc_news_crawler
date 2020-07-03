# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from pymongo import MongoClient
from itemadapter import ItemAdapter




class ProjectPipeline:

    def __init__(self):
        self.client = MongoClient("mongodb+srv://user1:kasdefghajklem@razinogriffith.r8vjd.mongodb.net/Articles?retryWrites=true&w=majority")
        db=self.client['Articles']
        self.collection=db["Articles_db"]
        
    
    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item