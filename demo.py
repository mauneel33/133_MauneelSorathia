import nltk
from nltk.corpus import twitter_samples as ts
import matplotlib.pyplot as plt
import re
import string
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import TweetTokenizer
import random

all_positive_tweets = ts.strings('positive_tweets.json')
# all_negative_tweets = ts.strings('negative_tweets.json')

# fig = plt.figure(figsize=(5,5))
# labels = 'Positive', 'Negative'
# sizes = [len(all_positive_tweets), len(all_negative_tweets)]
# plt.pie(sizes, labels=labels, autopct='%1.1f%%', shadow=True, startangle=90)
# plt.axis('equal')
# plt.show()

# print('\033[92m'+ all_positive_tweets[random.randint(0, 5000)])
# print('\033[91m'+ all_negative_tweets[random.randint(0, 5000)])

tweet = all_positive_tweets[2277]
# print('\033[92m' + tweet)
# print('\033[94m')

# Regular Expression
tweet2 = re.sub(r'https?:\/\/.*[\r\n]*', '', tweet)
tweet2 = re.sub(r'#', '', tweet2)

# Tokenizer
tokenizer = TweetTokenizer(preserve_case=False)
tweet_tokens = tokenizer.tokenize(tweet2)
# print('Tokenized string:')
# print(tweet_tokens)

stopwords_english = stopwords.words('english')
# print('stop words\n')
# print(stopwords_english)
# print(string.punctuation)

tweets_clean = []
for word in tweet_tokens:
    if (word not in stopwords_english and word not in string.punctuation):
        tweets_clean.append(word)

print('\033[92m')
print(tweets_clean)
print('\033[94m')


# Stemming
stemmer = PorterStemmer()
tweets_stem = []
for word in tweets_clean:
    stem_word = stemmer.stem(word)
    tweets_stem.append(stem_word)
print(tweets_stem)
