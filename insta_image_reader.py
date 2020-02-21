#!/usr/bin/env python
# coding: utf-8

# # The Instagram Image Reader

#  

# ## The Objective 

# We want to build a function that is able to download all images from Instagram, which are related to a hashtag.

# ## Setup and requirements

# In[1]:


from bs4 import BeautifulSoup as bs
import selenium.webdriver as webdriver
from PIL import Image


#  

# ## Extract links from Instagram page

# At first, we need to extract all links from the hashtag page.

# In[4]:


url = 'https://www.instagram.com/explore/tags/picoftheday/'
driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get(url)


# In[5]:


soup = bs(driver.page_source)

all_links = []
for link in soup.find_all('a'):
    current_link = link.get('href')
    all_links.append(current_link)
    
print(all_links)
driver.close()


# Next we identify these links that follow to the single posts.

# In[6]:


substring = "/p/"

image_links = []
for i in range(0, len(all_links)):
    if all_links[i].startswith(substring):
        image_links.append(all_links[i])

print(image_links)


# ## Rebuild links 

# In[7]:


substring = "https://www.instagram.com"

image_urls = []

for i in range(0, len(image_links)):
    url = substring + image_links[i]
    image_urls.append(url)
    
print(image_urls)


# ## Save and crop image 

# Let us open the html of a single post as example.

# In[9]:


url = "https://www.instagram.com/p/B81HxWHqvHn/"
driver = webdriver.Chrome("/usr/bin/chromedriver")
driver.get(url)


# We make a screenshot and save it under a certain working directory.

# In[10]:


save_name = 'test' + '.png'  
save_path = "/home/emanuel/Desktop/saved_images/"
save_dir = str(save_path + save_name)
print(save_dir)
driver.save_screenshot(save_dir)
driver.close()


# We re-open the screenshot and extract the image by cropping the png-file.

# In[11]:


image = Image.open(save_dir)
box = (50, 200, 500, 730)
area = image.crop(box)
area.save(save_dir)


#  

# ## The Function

# In[13]:


def insta_pic_saver(hashtag, max_pictures, directory):
    
    url = "https://www.instagram.com/explore/tags/"
    url = url + hashtag + "/"
    
    driver = webdriver.Chrome("/usr/bin/chromedriver")
    driver.get(url)
    soup = bs(driver.page_source)

    all_links = []
    for link in soup.find_all('a'):
        current_link = link.get('href')
        all_links.append(current_link)
    driver.close()
    
    substring = "/p/"
    image_links = []
    for i in range(0, len(all_links)):
        if all_links[i].startswith(substring):
            image_links.append(all_links[i])

    substring = "https://www.instagram.com"
    image_urls = []
    for i in range(0, len(image_links)):
        url = substring + image_links[i]
        image_urls.append(url)
    
    if len(image_urls) < max_pictures:
        control_string = "ERROR: not enough images, max image number is"
        print(control_string, len(image_urls))
        return
    
    i = 0
    while i <= (max_pictures-1):
        
        driver = webdriver.Chrome("/usr/bin/chromedriver")
        url = image_urls[i]
        driver.get(url)
        soup = bs(driver.page_source)
        
        save_name = 'image' + str(i) + '.png'  
        save_path = directory
        save_dir = str(save_path + save_name)
        driver.save_screenshot(save_dir)
        driver.close()
        
        image = Image.open(save_dir)
        box = (50, 200, 500, 730)
        area = image.crop(box)
        area.save(save_dir)
        
        i += 1


#  

# ## Some examples 

# In[14]:


hashtag = "trump"
max_pictures = 5
directory = "/home/emanuel/Desktop/saved_images/"
insta_pic_saver(hashtag, max_pictures, directory)


# In[12]:


hashtag = "travelgram"
max_pictures = 5
directory = "/home/emanuel/Desktop/saved_images2/"
insta_pic_saver(hashtag, max_pictures, directory)


# In[ ]:


hashtag = "food"
max_pictures = 5
directory = "/home/emanuel/Desktop/saved_images3/"
insta_pic_saver(hashtag, max_pictures, directory)

