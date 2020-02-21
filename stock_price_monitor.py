#!/usr/bin/env python
# coding: utf-8

# #  Stock Price Monitor

#  

# ## The Objective 

# The aim is to monitor stock prices on https://www.boerse.de/.
# 
# We look for the current price, the absolute 24h development and the relative 24h development.

#  

# ## Setup and requirements

# In[1]:


from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
import datetime
import time


#  

# ## Extract relevant information 

# We choose the MSCI World Index as an example. The MSCI World is the index for the 23 countries with the strongest economy. The index measures the development of 1650 stocks. 
# 
# First, we save the respective URL as string. We inspect the website for a better understanding of the contents.

# In[2]:


url = "https://www.boerse.de/indizes/MSCI-World/XC0009692739"


# We read he contents and search for those parameters, where the target variables are stored.

# In[3]:


html = urlopen(url)   
soup = bs(html.read())
soup = soup.find_all('span',{'class':'BW_PUSH'})


# The stored items are converted to a list.

# In[4]:


temp = []
for i in range(0, len(soup)):
    temp.append(str(soup[i]))
soup = temp
print(soup)


# We find the following substrings indicating our target information. We search for the position of the strings in our list that contain these substrings.

# In[5]:


# "last", "perfInstAbs", "perfInstRel"

substrings = ["last", "perfInstAbs", "perfInstRel"]

for j in range(0, len(substrings)):
    temp_ind = []
    for i in range(0, len(soup)):
        if substrings[j] in soup[i]:
            temp_ind.append(i)
    print(temp_ind)
        


# For further processing, it is recommended to choose a convenient string. 

# In[8]:


price_string = soup[29]
print(price_string)


# In[9]:


da_string = soup[30]
print(da_string)


# In[10]:


dr_string = soup[31]
print(dr_string)


# In order to extract the target information from the strings as floats, string manipulation is applied. 

# In[11]:


price = re.findall("\d*\.*\d*\,\d*", price_string)
price = price[0]
print(price)

price = re.findall("\d*", price)
print(price)

price = float(str(price[0] + price[2] + "." + price[4]))
print(price)


# In[12]:


da = re.findall("\-*\d*\,\d*", da_string)
da = da[0]
print(da)

da =re.findall("\-*\d*", da)
print(da)

da = float(str(da[0] + "." + da[2]))
print(da)


# In[13]:


dr = re.findall("\-*\d*\,\d*", dr_string)
dr = dr[0]
print(dr)

dr =re.findall("\-*\d*", dr)
print(dr)

dr = float(str(dr[0] + "." + dr[2]))
print(dr)


# Lastly, we use the generated information to print the result.

# In[14]:


print("MSCI World Index stock is at ", price, "$ at ", datetime.datetime.now(), ".")
print("The absolute 24h development is ", da, ".")
print("The relative 24h development is ", dr, "% .")


#  

# ## The Function 

# Now, we compute a function that takes following input arguments:
# 
# * **url**: any url from https://www.boerse.de/
# * **name**: name of stock market item (only used for result)
# * **minutes**: minutes to watch the stock.
# 
# The aim is a general function that watches any stock from https://www.boerse.de/ as long as we intend.

# In[17]:


def stock_monitor(url, name, minutes):
    
    minute = 1
    while minute <= minutes: 
        
        html = urlopen(url)   
        soup = bs(html.read())
        soup = soup.find_all('span',{'class':'BW_PUSH'}) 
    
        temp = []
        for i in range(0, len(soup)):
            temp.append(str(soup[i]))
        soup = temp
    
        price_string = soup[29]
        da_string = soup[30]
        dr_string = soup[31]
    
        price = re.findall("\d*\.*\d*\,\d*", price_string)
        price = price[0]
        price = re.findall("\d*", price)
        price = float(str(price[0] + price[2] + "." + price[4]))
    
        da = re.findall("\-*\d*\,\d*", da_string)
        da = da[0]
        da = re.findall("\-*\d*", da)
        da = float(str(da[0] + "." + da[2]))
    
        dr = re.findall("\-*\d*\,\d*", dr_string)
        dr = dr[0]
        dr =re.findall("\-*\d*", dr)
        dr = float(str(dr[0] + "." + dr[2]))
    
        print(name ,"stock is at ", price, "$ at ", datetime.datetime.now(), ".")
        print("The absolute 24h development is ", da, ".")
        print("The relative 24h development is ", dr, "% .")
        print(" ")
        
        time.sleep(30)
        minute += 1
        
        
      


#  

# ## Some examples 

# In[16]:


url = "https://www.boerse.de/indizes/MSCI-World/XC0009692739"
name = "MSCI WORLD INDEX"

stock_monitor(url, name, minutes=5)


# In[18]:


url = "https://www.boerse.de/indizes/Dax/DE0008469008"
name = "DAX"

stock_monitor(url, name, minutes=5)


# In[16]:


url = "https://www.boerse.de/rohstoffe/Goldpreis/XC0009655157"
name = "GOLD"

stock_monitor(url, name, minutes=5)


# In[18]:


url = "https://www.boerse.de/indizes/Dow-Jones/US2605661048"
name = "DOW JONES"

stock_monitor(url, name, minutes=5)

