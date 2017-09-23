from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import os,re
import porter
import nltk.tokenize.api
import json
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
list_words_dict={}
for filename in os.listdir("."):
	file=open(filename,"rb")
	stri=file.read()
	list_words_dict[filename]=str(stri).split(" ")
	for i in range(0,len(list_words_dict[filename])):
		list_words_dict[filename][i]=normalize(list_words_dict[filename][i])
	list_set=set(list_words_dict[filename])
	final_set=final_set|list_set


len_lis={}
for key,values in list_words_dict.items():
	len_doc=len(set(list_words_dict[key]))
	len_lis[key]=len_doc
#	return len_lis		
	#final_set.remove("")
k=0	
for word in final_set:
	final_dict[word]={}
	#list_dict={}
	if(word!=""):
		for key,value in list_words_dict.items():
			if word in value:
				final_dict[word][key]=value.count(word)
os.chdir("/home/sriyamuppidi")
r=json.dumps(final_dict)
fp=open("final.json","w+")
fp.write(r)			
re=json.dumps(len_lis)
fr=open("final1.json","w+")
fr.write(re)
		


			

		



