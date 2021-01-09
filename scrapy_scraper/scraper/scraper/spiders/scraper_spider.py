


#  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$  /$$$$$$$  /$$$$$$ /$$   /$$  /$$$$$$                                        /$$     /$$                    
# /$$__  $$ /$$__  $$| $$__  $$ /$$__  $$| $$__  $$|_  $$_/| $$$ | $$ /$$__  $$                                      | $$    |__/                    
#| $$  \__/| $$  \__/| $$  \ $$| $$  \ $$| $$  \ $$  | $$  | $$$$| $$| $$  \__/        /$$$$$$$  /$$$$$$   /$$$$$$$ /$$$$$$   /$$  /$$$$$$  /$$$$$$$ 
#|  $$$$$$ | $$      | $$$$$$$/| $$$$$$$$| $$$$$$$/  | $$  | $$ $$ $$| $$ /$$$$       /$$_____/ /$$__  $$ /$$_____/|_  $$_/  | $$ /$$__  $$| $$__  $$
# \____  $$| $$      | $$__  $$| $$__  $$| $$____/   | $$  | $$  $$$$| $$|_  $$      |  $$$$$$ | $$$$$$$$| $$        | $$    | $$| $$  \ $$| $$  \ $$
# /$$  \ $$| $$    $$| $$  \ $$| $$  | $$| $$        | $$  | $$\  $$$| $$  \ $$       \____  $$| $$_____/| $$        | $$ /$$| $$| $$  | $$| $$  | $$
#|  $$$$$$/|  $$$$$$/| $$  | $$| $$  | $$| $$       /$$$$$$| $$ \  $$|  $$$$$$/       /$$$$$$$/|  $$$$$$$|  $$$$$$$  |  $$$$/| $$|  $$$$$$/| $$  | $$
# \______/  \______/ |__/  |__/|__/  |__/|__/      |______/|__/  \__/ \______/       |_______/  \_______/ \_______/   \___/  |__/ \______/ |__/  |__/

#   /$$                     /$$              
#  | $$                    | $$              
# /$$$$$$    /$$$$$$   /$$$$$$$  /$$$$$$  /$$
#|_  $$_/   /$$__  $$ /$$__  $$ /$$__  $$|__/
#  | $$    | $$  \ $$| $$  | $$| $$  \ $$    
#  | $$ /$$| $$  | $$| $$  | $$| $$  | $$ /$$
#  |  $$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$/|__/
#   \___/   \______/  \_______/ \______/     
#
#
#   per poter permettere allo scraper di analizzare diverse pagine automaticamente bisgona parsare il dominioe successivamente
#   chiamare una diversa callback in base al dominio richiesto.
#
#   ES. 
#
#       _rl = response.url
#       url = _rl.split("/")[2]
#
#       print (url)
#
#   fatto ciò posso chiamare una callback diversa 
#
#   yield scrapy.Request(link_richiesto, callback=callback.che.mi.serve)
#


import scrapy
from parser import *
#from .graphic_interface import gui
from .nltk.nltk_section import *
from scraper.items import ScraperItem
from datetime import date
from urllib.parse import urlparse

class scraper (scrapy.Spider):

    name = "scraper"
    count_link = 0
    count_rev = 0
    start_urls = []
    url = ''

    while True:
        if url == 'stop':
            break
        else:
            url = input("Inserire url: (digitare 'stop' per fermare l'inserimento) ")
            start_urls.append(url)
    #print(url.split("/")[2])
    data_list = []
    author_list = []
    urls = []
    today = date.today()
    date = today.strftime("%d/%m/%Y")

    #gui = gui()

    #def start_requests(self, domain):

    #    for elem in self.start_urls:

    #        if elem == 'stop':
    #            break
    #        else:
    #            domain = urlparse(elem).netloc
    #            if domain == 'www.tripadvisor.it':
    #                yield scrapy.Request(response.urljoin(elem), self.tripadvisor)
    #            elif elem.split('/')[2] == 'forum.tomshw.it':
    #                yield scrapy.Request(response.urljoin(elem), self.tomshw)

    def parse(self, response):
        print('ora parso      ', response.url)
        domain = urlparse(response.url).netloc
        if domain == 'www.tripadvisor.it':
            yield scrapy.Request(response.url, self.tripadvisor, dont_filter = True)
        elif domain == 'forum.tomshw.it':
            yield scrapy.Request(response.url, self.tomshw, dont_filter = True)

    def tomshw(self, response):

        print('sono in TOMSHW')

    def tripadvisor(self, response):

        for element in response.css('div.wQjYiB7z'):
            #yield {
            #    'text': review.css('span::text').get(),
            #    'author': review.css('a.ui_header_link _1r_My98y::text').get()
            #}
            #self.data_list.append(review.css('span::text').get())
            #self.author_list.append(review.css('a.ui_header_link _1r_My98y::text').get())
            print('pagina ristorante     ', element.css('a._15_ydu6b::attr(href)').get())
            self.urls.append(element.css('a._15_ydu6b::attr(href)').get())

        next_page = response.css('a.next::attr(href)').get()

        if next_page is not None and self.count_link < 3:
            next_page = response.urljoin(next_page)
            self.count_link += 1
            print('next page      ', next_page)
            yield scrapy.Request(next_page, self.parse)
        else:
            for link in range(len(self.urls)):
                yield scrapy.Request(response.urljoin(self.urls[link]), self.follow_link)

    def follow_link(self, response):
        print('sono in follow link')
        for review in response.css('div.rev_wrap'):
            #yield {
            #    'text': review.css('span::text').get(),
            #    'author': review.css('a.ui_header_link _1r_My98y::text').get()
            #}
            self.data_list.append(review.css('p.partial_entry::text').get())
            item = ScraperItem()
            item['review'] = review.css('p.partial_entry::text').get()
            item['user'] = review.css('div.info_text::text').get()
            item['timestamp'] = self.date
            #item['source'] = self.url.split("/")[2]
            yield item
            #self.author_list.append(review.css('a.ui_header_link _1r_My98y::text').get())

        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None and self.count_rev < 3:
            next_page = response.urljoin(next_page)
            self.count_rev += 1
            yield scrapy.Request(next_page, callback=self.follow_link)

    def closed(self, reason):
        prepare_text(self.data_list)




        
        
        
        
        
        
