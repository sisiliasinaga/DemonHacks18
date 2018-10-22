import csv
import codecs, json
import pandas as pd
import matplotlib
import re
from wordcloud.wordcloud import WordCloud
from matplotlib import pyplot as plt
# Need to install
# sudo pip3 install wordcloud
# sudo pip3 install matplotlib

# might need
# sudo pip3 install numpy
# sudo pip3 install Pillow
# 
#
# DEPENDING ON WHAT WAS USED TO PULL ALL THE TWEETS, YOU CAN USE PANDAS. 
# THE WEB SCRAPER VERSION THAT USES NO API CAN BE PASSED AS A DF. 
# I might need to review how to install TkAgg stuff

matplotlib.use("TkAgg") # Set image creation engine to use. Necessary for non-Apple devices
input_data = "" # Stores all CSV entries as a single string

# Opens CSV and reads each entry, stores it into input_data
with open('tweets.csv', 'r', encoding='UTF-8', newline='') as csvarchive:
    entrada = csv.reader(csvarchive)
    for reg in entrada:
        input_data += ''.join(reg)

# Uses regex to filter the data. Mostly just removes URLs. 
input_data = re.sub(r'^https?:\/\/.*[\r\n]*', '', input_data, flags=re.MULTILINE) #Removes a few URLs
input_data = re.sub(r"http\S+", "", input_data) #removes some URLs
input_data = re.sub(r"pic\S+", "", input_data) #removes more URLs
input_data = re.sub(r"https\S+", "", input_data) #even more URLs!


#Wordcloud generator

# Generates wordcloud
wordcloud = WordCloud(max_font_size = 600, width=3200, height=1600).generate(input_data)

plt.figure( figsize=(40,20), facecolor='k') # Sets size for plt
plt.imshow(wordcloud) # Embed image into canvas
plt.axis("off")
plt.tight_layout(pad=0)
plt.show() # I don't even think you need this
plt.savefig('wordcloud.png', facecolor='k', bbox_inches='tight') # Saves to root directory









# ALL THIS CODE DOWN HERE WAS FOR TESTING AND MAY HAVE VALUE IF YOU NEED MORE FEATURES (I guess)


'''
with open('output.json', 'r') as f:
	for row in csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE):
		input_data += ''.join(row)
'''
#print(input_data)
# Generate a word cloud image
'''wordcloud = WordCloud(width=2000, height=1000).generate(input_data)
from matplotlib import pyplot as plt
# Display the generated image:
# the matplotlib way:
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
# lower max_font_size
wordcloud = WordCloud(max_font_size=40).generate(input_data)
plt.figure(figsize = (20, 10))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
plt.savefig('wordcloud.png', facecolor='k', bbox_inches='tight')
'''

#Image.open("WORDCLOUDIMAGEAAAAAAAA.png").save("WORDCLOUDIMAGEAAAAAAAA.png")

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()