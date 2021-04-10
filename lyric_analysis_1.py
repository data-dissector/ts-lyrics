import json
from os import path
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import os
from wordcloud import WordCloud, STOPWORDS


## load in the data ##
with open('filtered_lyrics.json') as f:
    data = json.load(f)
print(data)


## function to convert list of lyrics to string of text ##
def listToString(lyrics):
    text = " "
    return (text.join(lyrics))


## function to create and generate a word cloud image for each album ##
def make_world_cloud(album, lyrics, mask, color):
    stopwords = set(STOPWORDS)
    stopwords.update(["n't", "oh", "ooh", "ai", "oooh", "wo", "mmmm", "mmmmmmm", "lyrics", "chorus", "written", "taylor", "repeat", "s", "ta", "la", "ve", "ll", "wan", "na", "ca", "re", "d", "m", "gon", "ah"])
    # wordclouds = []

    # for lyric in lyrics:

    text = listToString(lyrics)
    # records = ["selftitled", "fearless", "speaknow", "red", "1989", "reputation", "lover", "folklore", "evermore"]
    # for record in records:
        ## read the mask images ##
        # mask = np.array(Image.open("/Users/lindsaytubbs/Documents/python_projects/" + record + "_mask.png"))
    wordcloud = WordCloud(font_path="Arial", color_func=lambda *args, **kwargs: color, min_font_size=8, background_color="white", mask=mask, stopwords=stopwords, contour_width=3, contour_color=color)
    # color_func=lambda color, color:"blue"
    wordcloud.generate(text)
    # wordclouds.append(wordcloud)

    # for wordcloud in wordclouds:

    ## display the generated images ##
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    # plt.imshow(mask, cmap=plt.cm.gray, interpolation='bilinear')
    # plt.axis("off")
    # plt.show()

    ## Save the images in the python_projects folder ##
    filename = album + "_wordcloud.png"
    wordcloud.to_file("/Users/lindsaytubbs/Documents/python_projects/" + filename )


# print([k for k in data])
# records = ["selftitled", "fearless", "speaknow", "red", "1989", "reputation", "lover", "folklore", "evermore"]

matches = [{"mask": "selftitled", "album": "Taylor Swift", "color": "deepskyblue"},
            {"mask": "fearless", "album": "Fearless", "color": "darkgoldenrod"},
            {"mask": "speaknow", "album": "Speak Now", "color": "darkmagenta"},
            {"mask": "red", "album": "Red (Deluxe Edition)", "color": "darkred"},
            {"mask": "1989", "album": "1989", "color": "blueviolet"},
            {"mask": "reputation", "album": "reputation", "color": "black"},
            {"mask": "lover", "album": "Lover", "color": "hotpink"},
            {"mask": "folklore", "album": "folklore", "color": "dimgray"},
            {"mask": "evermore", "album": "evermore", "color": "forestgreen"}
            ]

for match in matches:
    print(match)
    mask = np.array(Image.open("/Users/lindsaytubbs/Documents/python_projects/" + match["mask"] + "_mask.png"))
    make_world_cloud(album=match["album"], lyrics=data[match["album"]], mask=mask, color=match["color"])
