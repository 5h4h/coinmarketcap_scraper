import scrapy
from scrapy import Request


class CoinmarketScraper(scrapy.Spider):
    name = 'coinmarket'
    allowed_domains = ['coinmarketcap.com']
    download_delay = 1.5
    start_urls = ['https://coinmarketcap.com/?page=%s' % page for page in range(1,62)]




    def parse(self, response):
        for coin in response.css('tbody > tr'):

            link = 'https://coinmarketcap.com'+ coin.css('td > a::attr(href)').get()
            
            yield Request(link, callback=self.second_page, dont_filter=True, meta={'Link': link})
            

    

    def second_page(self, response):
        
        link = response.meta.get('Link')
        rank = response.css('div.sc-16r8icm-0.bILTHz > div.namePill___3p_Ii.namePillPrimary___2-GWA::text').get()
        name = response.css('h2.sc-1q9q90x-0.iYFMbU.h1___3QSYG::text').get()
        symbol = response.css('h2.sc-1q9q90x-0.iYFMbU.h1___3QSYG > small.nameSymbol___1arQV::text').get()
        price = response.css('div.sc-16r8icm-0.kjciSH.priceTitle___1cXUG > div.priceValue___11gHJ::text').get()
        tags = response.css('div.tagModalTags___3dJxH > a.cmc-link > div::text').getall()
        reported_tags = response.css('div.tagModalTags___3dJxH > div.tagBadge___3p_Pk::text').getall()
        
        source_code = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][1]/a[@class='modalLink___MQefI']/@href[contains(.,'github') or contains(.,'gitlab')]").getall()
        discord = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][1]/a[@class='modalLink___MQefI']/@href[contains(.,'discord')]").getall()
        telegram = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][1]/a[@class='modalLink___MQefI']/@href[contains(.,'https://t.me') or contains(., 'telegram') or contains(., 'https://t.co')]").getall()
        slack = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][1]/a[@class='modalLink___MQefI']/@href[contains(.,'slack')]").getall()
        whitepaper = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][1]/a[@class='modalLink___MQefI']/@href[contains(.,'whitepaper') or contains(.,'white-paper') or contains(.,'WHITEPAPER') or contains(.,'docs') or contains(.,'drive.google') or contains(.,'.pdf') or contains(.,'docsend.com') or contains(.,'docdroid.net') or contains(.,'gitbook') or contains(.,'documentation')]").getall()
        facebook = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][1]/a[@class='modalLink___MQefI']/@href[contains(.,'facebook.com')]").getall()
        website = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][1]/a[@class='modalLink___MQefI']/@href[not(contains(.,'https://t.me') or contains(., 'telegram') or contains(., 'github') or contains(., 'gitlab') or contains(., 'discord') or contains(., 'slack') or contains(.,'whitepaper') or contains(.,'WHITEPAPER') or contains(.,'white-paper') or contains(.,'docs') or contains(.,'drive.google') or contains(.,'.pdf') or contains(.,'docsend.com') or contains(.,'docdroid.net') or contains(.,'gitbook') or contains(.,'documentation') or contains(., 'https://t.co') or contains(.,'facebook.com'))]").getall()
        
        etherscan = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][2]/a[@class='modalLink___MQefI']/@href[contains(.,'https://etherscan')]").getall()
        ethplorer = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][2]/a[@class='modalLink___MQefI']/@href[contains(.,'https://ethplorer')]").getall()
        bscscan = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][2]/a[@class='modalLink___MQefI']/@href[contains(.,'https://bscscan')]").getall()
        chain_cryptoid = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][2]/a[@class='modalLink___MQefI']/@href[contains(.,'chainz.cryptoid.info')]").getall()
        bloksio = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][2]/a[@class='modalLink___MQefI']/@href[contains(.,'https://bloks.io')]").getall()
        stellar_expert = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][2]/a[@class='modalLink___MQefI']/@href[contains(.,'stellar.expert')]").getall()
        medium = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][2]/a[@class='modalLink___MQefI']/@href[contains(.,'medium')]").getall()
        twitter = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][2]/a[@class='modalLink___MQefI']/@href[contains(.,'twitter')]").getall()
        reddit = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][2]/a[@class='modalLink___MQefI']/@href[contains(.,'reddit')]").getall()
        bitcointalk = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][2]/a[@class='modalLink___MQefI']/@href[contains(.,'bitcointalk')]").getall()
        other_explorers = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][2]/a[@class='modalLink___MQefI']/@href[not(contains(.,'https://etherscan') or contains(.,'https://ethplorer') or contains(.,'https://bscscan') or contains(.,'chainz.cryptoid.info') or contains(.,'https://bloks.io') or contains(.,'stellar.expert') or contains(.,'medium') or contains(.,'twitter') or contains(.,'reddit') or contains(.,'bitcointalk'))]").getall()

        medium2 = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'medium')]").getall()
        twitter2 = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'twitter')]").getall()
        reddit2 = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'reddit')]").getall()
        youtube = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'youtube') or contains(., 'youtu.be')]").getall()
        bitcointalk2 = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'bitcointalk')]").getall()
        telegram2 = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'https://t.me') or contains(., 'telegram') or contains(., 'https://t.co')]").getall()
        instagram = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'instagram')]").getall()
        discord2 = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'discord')]").getall()
        facebook2 = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'facebook')]").getall()
        linkedin = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'linkedin')]").getall()
        steemit = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'steemit.com')]").getall()
        blog = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'blog')]").getall()
        forum = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'forum')  or contains(.,'forums')]").getall()
        news = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[contains(.,'news')]").getall()
        community = response.xpath("//div[@class='sc-16r8icm-0 eMxKgr']/div[@class='sc-16r8icm-0 jKrmxw'][3]/a[@class='modalLink___MQefI']/@href[not(contains(.,'medium') or contains(.,'twitter') or contains(.,'reddit') or contains(.,'youtube') or contains(., 'youtu.be') or contains(.,'bitcointalk') or contains(.,'https://t.me') or contains(., 'telegram') or contains(., 'https://t.co') or contains(.,'instagram') or contains(.,'discord') or contains(.,'facebook') or contains(.,'linkedin') or contains(.,'steemit.com') or contains(.,'blog') or contains(.,'forum') or contains(.,'news') or contains(.,'forums'))]").getall()
        
        


        yield{
            'Rank' : rank,
            'Name' : name,
            'Symbol' : symbol,
            'Link' : link,
            'Price' : price,
            'Tags' : tags,
            'Self Reported Tags' : reported_tags,
            'Source Code' : source_code,
            'Telegram' : telegram,
            'Discord' : discord,
            'Facebook' : facebook,
            'Slack' : slack,
            'Whitepaper' : whitepaper,
            'Website(s)' : website,
            'Etherscan' : etherscan,
            'Ethplorer' : ethplorer,
            'BscScan' : bscscan,
            'Chain Cryptoid' : chain_cryptoid,
            'Bloks.io' : bloksio,
            'Stellar_Expert' : stellar_expert,
            'Medium' : medium,
            'Twitter' : twitter,
            'Reddit' : reddit,
            'Bitcointalk' : bitcointalk,
            'Other Explorers' : other_explorers,
            'Twitter2': twitter2,
            'Medium2' : medium2,
            'Reddit2' : reddit2,
            'Bitcointalk2' : bitcointalk2,
            'Youtube' : youtube,
            'Instagram' : instagram,
            'LinkedIn' : linkedin,
            'Steemit' : steemit,
            'Telegram2' : telegram2,
            'Discord2' : discord2,
            'Facebook2' : facebook2,
            'Blog' : blog,
            'Forum' : forum,
            'News' : news,
            'Community' : community,
            }