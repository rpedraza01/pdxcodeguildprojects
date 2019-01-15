# count_words_lab_21.py
import string
# line 4 is a list of words we don't want to count as they come up so often
stop_words = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't", 'gutenberg', 'ebooks', 'project', 'gutenbergtm']
# lines 6 - 9 open and read the file -- prints out the body of the text
with open("ThePrince.txt") as the_prince_file:
    contents = the_prince_file.read()
    print(contents)
# line 10 converts contents into lower case words
contents = contents.lower()
# lines 12 - 15 removes the punctuations from all of the words in contents
translator = str.maketrans("", "", string.punctuation)
string_without_punct = contents.translate(translator)
words = string_without_punct.split()
print(words)
# lines 17 - 25 create a dictionary with a for loop that keeps track of how many times each word comes up except for words in the stop_words list.
word_dict = {}
for i in range(len(words)):
    word = words[i]
    if word in stop_words:
        continue
    elif word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
# lines 27 - 37 create a dictionary with a for loop that keeps track of how many times each word pair comes up except for word pairs in the stop_words list.
pairs = {}
for i in range(len(words) - 1):
    first = words[i]
    second = words[i + 1]
    pair = (first, second)
    if first in stop_words or second in stop_words:
        continue
    elif pair in pairs:
        pairs[pair] += 1
    else:
        pairs[pair] = 1
# line 39 creates the variable words which is a list of the dictionary word_dict
words = list(word_dict.items())
# line 41 sorts the variable words
words.sort(key = lambda tup: tup[1], reverse = True)
# lines 42 - 43 creates and prints a list of the top 10 most used words (excluding the stop_words list)
for i in range(min(10, len(words))):
    print(words[i])
# lines 46 - 49 creates and prints a list of the top 10 most used word pairs (again, excluding word pairs in the stop_words list)
pairs_10 = list(pairs.items())
pairs_10.sort(key = lambda tup: tup[1], reverse = True)
for i in range(min(10, len(pairs_10))):
    print(pairs_10[i])