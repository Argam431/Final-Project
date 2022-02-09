import logging
#from multiprocessing import Process, Pool
from bs4 import BeautifulSoup
import requests


logger = logging.getLogger(__name__)

def parse(doc):
    '''
    returned like this...
    [{'quote':quote,'author':author,'tags':[tag_1,tag_2,...]},..x10]
    '''
    soup = BeautifulSoup(doc, 'lxml')
    
    #row = soup.select('div.col-md-8 div.quote')
    
    row = soup.find_all("div", class_="quote")
    

    if row:
        data = []
        for div_quote in row:
            quote = div_quote.select_one('span.text').text
            author = div_quote.find('small').text 
            tags = [tag.text for tag in div_quote.find('div', class_='tags').find_all('a')]   
            data.append({'quote':quote,'author':author,'tags':tags})
        return data
    else:
        logger.error('Not data')
    


def my_scrap(pages=1):
    '''
    returned like this...
    [{'quote':quote,'author':author,'tags':[tag_1,tag_2,...]},..x10 x <page:int>]
    '''
    parsed_data:list=[]
    for page in range(1,pages+1):
        url = f'https://quotes.toscrape.com/page/{page}/'
        parsing_data = scrap(url)
        if parsing_data:            
            parsed_data.extend(parsing_data)
        else:
            logger.error(f'Page not found {url}')
           
    return parsed_data



def scrap(url):
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        logger.debug('received 200 status, now will do parsing')
        return parse(response.text)
    else:
        logger.error(f'unable to get response {response.status_code} {response.content}')


if __name__ == '__main__':
    print(len(my_scrap(10)))

