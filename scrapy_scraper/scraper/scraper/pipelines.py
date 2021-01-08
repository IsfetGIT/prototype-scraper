# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.utils.project import get_project_settings
from scrapy.exceptions import DropItem
import logging
import pymongo

class MongoDBPipelines(object):

    def __init__(self):

        settings = get_project_settings()

        connection = pymongo.MongoClient(
            settings.get('MONGODB_SERVER'),
            settings.get('MONGODB_PORT')
        )
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):

        valid = True
        for data in item:
            if not data:
                valid = False
                raise DropItem("Missing {0}!".format(data))
        if valid:
            self.collection.insert(dict(item))
            #log.msg("Question added to MongoDB database!",
            #        level=log.DEBUG, spider=spider)

        return item

    def close_spider(self, spider):
    	print('######################## close chiamato #########################')
    	#self.collection.updateMany({'timestamp':today}, {'$set': {'topic': "topic di test"}})


class workEnded(object):

    def closed_scraper(self, spider):
        print("ho finito per dio")