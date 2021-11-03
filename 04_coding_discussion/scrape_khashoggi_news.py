'''
Download the news story about Erdogan talking about Khashoggi murder
'''

from newspaper import Article

def get_article(url,out_file):
    '''
    Scrape a new url and save the file.

    Arguments:

        - url: a url of a news story (with written content)
        - out_file: a file path and name of where the news story should be saved
    '''
    art = Article(url)
    art.download()
    art.parse()
    with open(out_file,'xt') as f:
        f.writelines(art.text.replace('\n\n'," "))


# BBC
get_article('https://www.bbc.com/news/world-europe-45949742','bbc-khashoggi.txt')

# Fox
get_article('https://www.foxnews.com/world/saudi-officials-planned-khashoggis-killing-days-before-his-death-erdogan-says','fox-khashoggi.txt')

# CNN
get_article('https://www.cnn.com/2018/10/23/middleeast/turkey-erdogan-khashoggi-intl/index.html','cnn-khashoggi.txt')

# Breitbart
get_article('https://www.breitbart.com/national-security/2018/10/23/trump-and-erdogan-demand-answers-from-saudis-for-khashoggi-killing/','breitbart-khashoggi.txt')

# Al-Jazeera
get_article('https://www.aljazeera.com/news/2018/10/khashoggi-killing-planned-turkish-president-erdogan-181023100141253.html','aljazeera-khashoggi.txt')
