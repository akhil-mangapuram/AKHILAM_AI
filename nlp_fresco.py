import nltk

f=open('cricket.txt','r',encoding='utf8')
raw=f.read()
#nltk.download('punkt')
tokens = nltk.word_tokenize(raw)
text = nltk.Text(tokens)
print(text)
for i in range(len(tokens)):
    tokens[i]= tokens[i].lower()
#removing digits
tokens= [x for x in tokens if not x.isdigit()]

#converting list into strings
tokens_str=' '.join(tokens)

#Removing the punctuations,tokenizer automatically convers string to list
from nltk.tokenize import RegexpTokenizer
tokenizer = RegexpTokenizer(r'\w+')
token_rem_punc= tokenizer.tokenize(tokens_str)

#Filtering the digits again
#tokens_NDP means NO DIGITS and PUNCTUATION
tokens_NDP= [x for x in token_rem_punc if not x.isdigit()]

#process to remove stopwords
nltk.download('stopwords')

from nltk.corpus import stopwords
#NO DIGITS PUNCTUATIONS AND STOPWORDS
tokens_NDPSW= [word for word in tokens_NDP if not word in set(stopwords.words('english'))]

#converting to string again to generate bigrams and trigrams
text_final = ' '.join(tokens_NDPSW)

#Generating Bi-grams
from nltk import ngrams
n1=2
bigrams=ngrams(text_final.split(),n1)
bigrams_list=[]
for x in bigrams:
    bigrams_list.append(x)

#Generating tri-grams
n2=3
tri_grams=ngrams(text_final.split(),n2)
trigrams_list=[]
for x in tri_grams:
    trigrams_list.append(x)
    
#Top 10 words in the tokens
count_list={} #creating the dictionary for word count
top10_list=[]

#Form the dictionary
for x in tokens_NDPSW:
    c=tokens_NDPSW.count(x)
    count_list[x]=c

#sorted_count_list is a list of tuples containing count of each word in the dictionary
import operator
sorted_count_list=sorted(count_list.items(),key=operator.itemgetter(1),reverse=True)

top10_list=sorted_count_list[0:10]
    

    
