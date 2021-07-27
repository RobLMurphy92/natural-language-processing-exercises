from requests import get
from bs4 import BeautifulSoup
import os
import requests
import pandas as pd



######### Functions ###########

def create_article_text(url,user_agent, class_, name_article):
    headers = {"User-Agent": str(user_agent)}
    response = get(url, headers =headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    title = soup.select('.jupiterx-post-title')[0].text
    content = soup.select('.jupiterx-post-content')[0].text
    article = soup.find('div', class_ = str(class_))
    
    with open(str(name_article), 'w') as f:
        f = f.write(article.text)
    return f
#############

def get_article(article, category):
    # Attribute selector
    title = article.select("[itemprop='headline']")[0].text
    
    # article body
    content = article.select("[itemprop='articleBody']")[0].text
    
    output = {}
    output["title"] = title
    output["content"] = content
    output["category"] = category
    
    return output
        
  #####################

def get_articles(category, base ="https://inshorts.com/en/read/"):
    """
    This function takes in a category as a string. Category must be an available category in inshorts
    Returns a list of dictionaries where each dictionary represents a single inshort article
    """
    
    # We concatenate our base_url with the category
    url = base + category
    
    # Set the headers
    headers = {"User-Agent": "Mozilla/4.5 (compatible; HTTrack 3.0x; Windows 98)"}

    # Get the http response object from the server
    response = get(url, headers=headers)

    # Make soup out of the raw html
    soup = BeautifulSoup(response.text)
    
    # Ignore everything, focusing only on the news cards
    articles = soup.select(".news-card")
    
    output = []
    
    # Iterate through every article tag/soup 
    for article in articles:
        
        # Returns a dictionary of the article's title, body, and category
        article_data = get_article(article, category) 
        
        # Append the dictionary to the list
        output.append(article_data)
    
    # Return the list of dictionaries
    return output

#######



def get_all_news_articles(categories):
    """
    Takes in a list of categories where the category is part of the URL pattern on inshorts
    Returns a dataframe of every article from every category listed
    Each row in the dataframe is a single article
    """
    all_inshorts = []

    for category in categories:
        all_category_articles = get_articles(category)
        all_inshorts = all_inshorts + all_category_articles

    df = pd.DataFrame(all_inshorts)
    return df



def get_codeup_blog(url):
    '''
    creating a function which will extract title, images, content and dates from web blog.
    '''
    headers = {"User-Agent": "Mozilla/4.5 (compatible; HTTrack 3.0x; Windows 98)"}
    
    #requesting the content of the web page.
    response = get(url, headers = headers)
    #utilizing beautiful soup in which to get it in a condition to work with.Allow us to navigate the html data
    soup = BeautifulSoup(response.content, 'html.parser')
    #utilizing soup.find to get the title, in this case h1 is unique for each blog so we can use this to 
    #specify the title
    title = soup.find('h1').text
    #utilizing soup to select the content of the blog in this case taking in CSS select as a string 
    # and returning elements matching elements
    content = soup.select('.jupiterx-post-content')[0].text
    #utilize soup which has .time which can be utilized to get the publish date
    publish_date = soup.time.text
    #stating if the count of the images > 0 then 
    if len(soup.select('.jupitex-post-image')) > 0:
        blog_image = soup.select('.jupiterx-post-image')[0].picture.img['data-src']
    else:
        blog_image = none
        
    dictionary = {}
    dictionary['title'] = title
    dictionary['content'] = content
    dictionary['publish_date'] = publish_date
    dictionary['blog_image'] = blog_image
    
    return dictionary