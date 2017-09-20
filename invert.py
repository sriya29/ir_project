from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os,re
import porter
import nltk.tokenize.api
def normalize(word):
	regex=re.compile('[^a-zA-Z0-9]')
	word=regex.sub("",word)
	word=word.lower()
	word_obj=porter.PorterStemmer(word)
	word_obj.stem(word,0,len(word)-1)
	word=word_obj.word
	return word

os.chdir("ir_project")
list=""
list_t=[]
final_set=set(list)
final_dict={}
for filename in os.listdir("."):
	file=open(filename,"rb")
	stri=file.read()
	list_words=(str(stri).split(" "))
	for i in range(0,len(list_words)):
		list_words[i]=normalize(list_words[i])
	list_set=set(list_words)
	final_set=final_set|list_set
	#final_set.remove("")
for word in final_set:
	final_dict[word]={}
	list_dict={}
	if(word):
		for filename in os.listdir("."):
			file=open(filename,"rb")
			stri=file.read()
			list_words=(str(stri).split(" "))
			for i in range(0,len(list_words)):
				list_words[i]=normalize(list_words[i])								
			if word in list_words:			#			#print(list_tuple)
				#list_dict[filename]=list_words.count(word)
				#final_dict[word].append(list_dict)
				final_dict[word][filename]=list_words.count(word)
#			#print(final_dict[word][filename])
		#break
#print(list_t)
#	break		
strin=str(final_dict)
fp=open("fg.txt","w+")
fp.write(strin)			

		


