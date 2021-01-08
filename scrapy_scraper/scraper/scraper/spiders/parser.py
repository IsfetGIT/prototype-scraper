import json

class parser():
    
    def parseJson():
        dataList = []
        
        with open('/home/isfet/prototype.scraper/scrapy_scraper/scraper/scraper/spiders/data.json') as f:
            data = json.load(f)
            for line in data['data']:
                #print(line['review']['text'])
                dataList.append(line['review']['text'])
        return dataList
        
    def printList(list):
        
        for elem in list:
            print(elem)

