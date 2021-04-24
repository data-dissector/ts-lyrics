# ts-lyrics
I am a longtime fan of Taylor Swift, and I admire her songwriting skills and ability to tell vivid stories with so few words. With a current discography of nine unique albums (not including rereleases or bonus editions) chronicling her life from ages 15 to 30, Swift has written an extensive amount of song lyrics that are ripe for analysis.


For my first foray into Python programming, I endeavored to take on this vast dataset of song lyrics. My first goal was to visually model the lyrics, sorted by album, in word clouds (also called tag clouds), which are an eye-catching and effective way to visualize language data. To view the word clouds I created, see the folder titled wordclouds.


My second goal was to perform statistical analysis and sentiment analysis on the dataset to determine prevalent lyrics, lyrical and thematic consistencies or changes throughout Swift's career, and implications of her as a songwriter and wordsmith.


I graphed plots for each album to statistically analyze and compare the most frequently-used lyric words per album. Each plot shows the 10 most-used words for the respective album, as well as the frequency of those words for every other album. To view these plots, see the folder titled lineplots.


I analyzed the sentiment or mood of each song and album using VADER (Valence Aware Dictionary and sEntiment Reasoner), a natural language sentiment analysis tool. VADER labels the sentiments of words as either negative, neutral, or positive, and calculates the proportion of the text that is negative vs neutral vs positive in sentiment. VADER also calculates a compound score of the sentiment of the text on a scale of -1 (most negative) to 1 (most positive). I determined the negative, neutral, positive, and compound scores for each song and album, and graphed plots to compare the scores and sentiments. To view these plots, see the files titled song_sentiments.png and album_sentiments.png.


Next, I will do further analysis to determine prevalent themes or topics in Swift’s lyrics.

Resources used:
https://docs.genius.com/#artists-h2


https://lyricsovh.docs.apiary.io/#reference


https://github.com/amueller/word_cloud


https://github.com/cristobalvch/Music-Lyrics-NLP


https://github.com/matplotlib/matplotlib


https://github.com/nltk/nltk


https://github.com/cjhutto/vaderSentiment


https://github.com/scikit-learn/scikit-learn


https://github.com/pandas-dev/pandas


https://github.com/numpy/numpy
