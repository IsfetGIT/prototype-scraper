


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
    start_urls = []
    url = ''
    count_link_trip = 0
    count_rev_trip = 0

    count_link_th = 0
    count_rev_th = 0


    #while True:
    #    if url == 'stop':
    #        break
    #    else:
    #        url = input("Inserire url: (digitare 'stop' per fermare l'inserimento) ")
    #        start_urls.append(url)
    #print(url.split("/")[2])

    f = open("urls.txt", "r")
    lines = f.readlines()
    for line in lines:
        start_urls.append(line)
    trip_urls = []
    tomhw_urls = []
    data_list = []
    today = date.today()
    date = today.strftime("%d/%m/%Y")

    #gui = gui()

    def parse(self, response):
        print('ora parso      ', response.url)
        domain = urlparse(response.url).netloc
        if domain == 'www.tripadvisor.it':
            yield scrapy.Request(response.url, self.tripadvisor, dont_filter = True)
        elif domain == 'forum.tomshw.it':
            yield scrapy.Request(response.url, self.tomshw, dont_filter = True)

    def tomshw(self, response):

        for element in response.css('div.structItem'):
            self.tomhw_urls.append(element.css('div.structItem-title::attr(uix-data-href)').get())

            next_page = response.css('a.pageNav-jump--next::attr(href)').get()

            if next_page is not None and self.count_link_th <= 3:
                next_page = response.urljoin(next_page)
                print('next page      ', next_page)
                self.count_link_th += 1
                yield scrapy.Request(next_page, self.parse)
            else:
                for link in range(len(self.tomhw_urls)):
                    yield scrapy.Request(response.urljoin(self.tomhw_urls[link]), self.follow_link_THW)

    def tripadvisor(self, response):
        count_link = 0

        for element in response.css('div.wQjYiB7z'):
            #yield {
            #    'text': review.css('span::text').get(),
            #    'author': review.css('a.ui_header_link _1r_My98y::text').get()
            #}
            #self.data_list.append(review.css('span::text').get())
            #self.author_list.append(review.css('a.ui_header_link _1r_My98y::text').get())
            print('pagina ristorante     ', element.css('a._15_ydu6b::attr(href)').get())
            self.trip_urls.append(element.css('a._15_ydu6b::attr(href)').get())

        next_page = response.css('a.next::attr(href)').get()

        if next_page is not None and self.count_link_trip <= 3:
            next_page = response.urljoin(next_page)
            self.count_link_trip += 1
            yield scrapy.Request(next_page, self.parse)
        else:
            for link in range(len(self.trip_urls)):
                yield scrapy.Request(response.urljoin(self.trip_urls[link]), self.follow_link_TA)

    def follow_link_TA(self, response):

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
            item['source'] = urlparse(response.url).netloc
            yield item
            #self.author_list.append(review.css('a.ui_header_link _1r_My98y::text').get())

        next_page = response.css('a.next::attr(href)').get()
        if next_page is not None and self.count_rev_trip <= 3:
            next_page = response.urljoin(next_page)
            self.count_rev_trip += 1
            yield scrapy.Request(next_page, callback=self.follow_link_TA)

    def follow_link_THW(self, response):
        print('response seconda', response.url)
        for elem in response.css('div.message-userContent'):

            self.data_list.append(elem.css('div.bbWrapper::text').get())
            item = ScraperItem()
            item['review'] = elem.css('div.bbWrapper::text').get()
            item['user'] = ''
            item['timestamp'] = self.date
            item['source'] = urlparse(response.url).netloc
            yield item
            #self.author_list.append(review.css('a.ui_header_link _1r_My98y::text').get())

        next_page = response.css('a.pageNav-jump--next::attr(href)').get()
        if next_page is not None and self.count_rev_th <= 3:
            next_page = response.urljoin(next_page)
            self.count_rev_th += 1
            yield scrapy.Request(next_page, callback=self.follow_link_THW)

    def closed(self, reason):

        for elem in self.data_list:
            if elem is None:
                self.data_list.remove(elem)

        prepare_text(self.data_list)




        
        
        
        
        
        
