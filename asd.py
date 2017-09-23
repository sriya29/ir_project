from flask import Flask,render_template,request
import porter
import re,requests,json,math

app = Flask(__name__,template_folder="./Templates")
@app.route("/", methods=["GET","POST"])
def hello():
	n_ten_items=[]
	if request.method=='POST':
		query=request.form['query']
		data_dict=proceed(query)
		n_items=(x[0] for x in data_dict)
		n_ty_items=list(n_items)
		print(type(n_ty_items))
		n_ty_items=n_ty_items[::-1]
		n_ten_items.extend(n_ty_items[:9])
		print(n_ten_items)
	return render_template("index.html",result=n_ten_items)


def normalize(word):
	regex=re.compile('[^a-zA-Z0-9]')
	word=regex.sub("",word)
	word=word.lower()
	word_obj=porter.PorterStemmer(word)
	word_obj.stem(word,0,len(word)-1)
	word=word_obj.word
	return word

def proceed(query):
	query_words=query.split(" ")
	for i in range(0,len(query_words)):
		query_words[i]=normalize(query_words[i])
	with open('final.json') as data_file:
		data=json.load(data_file)
	with open('final1.json') as len_file:
		len_d=json.load(len_file)	
	final_rank={}	
	for word in query_words:
		for file in data[word].keys():
			final_rank[file]=0

	for word in query_words:
		for file in data[word].keys():

			idf=math.log(600/len(data[word]))
			tf=1+math.log(data[word][file])
			tf_idf=(tf*idf)/(math.sqrt(len(query_words)*int(len_d[file])))
			final_rank[file]=final_rank[file]+tf_idf

	return sorted(final_rank.items(),key=lambda x:x[1])		



		
if __name__=='__main__':
	app.run(debug=True)	
