import csv
import codecs, json
import pandas as pd
import matplotlib
import re
from wordcloud.wordcloud import WordCloud

# Need to install
# sudo pip3 install wordcloud
# sudo pip3 install matplotlib

# might need
# sudo pip3 install numpy
# sudo pip3 install Pillow

# I might need to review how to install TkAgg stuff
#read first column of csv file to string of words seperated
#by tab
matplotlib.use("TkAgg")
your_list = []
input_data = ""

with open('tweets.csv', 'r', encoding='UTF-8', newline='') as csvarchive:
    entrada = csv.reader(csvarchive)
    for reg in entrada:
        input_data += ''.join(reg)

input_data = re.sub(r'^https?:\/\/.*[\r\n]*', '', input_data, flags=re.MULTILINE) #Removes a few URLs
input_data = re.sub(r"http\S+", "", input_data) #removes some URLs
input_data = re.sub(r"pic\S+", "", input_data) #removes more URLs
input_data = re.sub(r"https\S+", "", input_data) #even more URLs!

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
from matplotlib import pyplot as plt
wordcloud = WordCloud(max_font_size = 600, width=3200, height=1600).generate(input_data)
# Open a plot of the generated image.

plt.figure( figsize=(40,20), facecolor='k')
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)
plt.show()
plt.savefig('wordcloud.png', facecolor='k', bbox_inches='tight')
#Image.open("WORDCLOUDIMAGEAAAAAAAA.png").save("WORDCLOUDIMAGEAAAAAAAA.png")

# The pil way (if you don't have matplotlib)
# image = wordcloud.to_image()
# image.show()