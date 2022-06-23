import spacy
from data import text

# Creating a simple extractive summarizer based purely on the words in the text and how often they’re mentioned.

if __name__ == '__main__':
    # This is a language model of the library
    nlp = spacy.load("en_core_web_sm")

    # Dictionary to store words and their number of occurancy
    word_and_freq = {}

# tokenize text
doc = nlp(text)

# Iterate through doc tokens, count word frequencies and update the words dictionary

for word in doc:
    # turn word to lowercase
    word = word.text.lower()
    if word not in word_and_freq:
        word_and_freq[word] = 1
    else:
        word_and_freq[word] += 1

# Now the dictionary contains each word of the text and how many times each appears in it

# We then score the sentences - tuple containing the text of the sentence, its score, and its original index in the doc
sentences = []
sent_score = 0

# index of sentence in the doc and the doc sentences
for index, sent in enumerate(doc.sents):
    for word in sent:
        word = word.text.lower()
        # add the frequency of each word in the sentence
        sent_score += word_and_freq[word]
    # Final sentence score is the avg of the word frequencies in a word, divided by the number of words in the sentence
    sentences.append((sent.text.replace("\n", " "), sent_score / len(sent), index))

# Sort the sentences to get the most highly scored ones.

# Sorting based on the 2nd field, therefore the score, but negative, to be descending order
sentences = sorted(sentences, key=lambda x: -x[1])
# get the top 3 scored sentences and sort them, this time by their index order in the text, ascending
sentences = sorted(sentences[:3], key=lambda x: x[2])


# Create the summary by concatinating the top three sentences' text

summary_text = ""

for sent in sentences:
    summary_text += sent[0] + " "

print(summary_text)


