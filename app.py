from flask import Flask, render_template, request, jsonify
from pymongo import MongoClient
import numpy as np
import json

MONGO_URI = "mongodb+srv://gagarinjoshua:Abcd1234@cluster0.m8sb0kf.mongodb.net/" # Update with your MongoDB URI
client = MongoClient(MONGO_URI)
db = client.chatbot
collection = db.chatdata
responses = db.response 
data = list(collection.find({}, {'_id': 0}))  
response = list(responses.find({}, {'_id': 0}))

chat_data = (data[0])
response_dict = (response[0])

chat_list = []
response_list = []

app = Flask(__name__)

# with open("chatdata.json", 'r') as f:
#     chat_data = json.load(f)
#     f.close()

# Reading Resposne 
# with open("response.json") as f:
#     response_dict = json.load(f)
#     f.close()

# Training Data
training_dict = {}

# creating formatted data for fitiing model
for intent, question_list in chat_data.items(): #chat_data.items()
    
   for question in question_list:
     training_dict[question] = intent
 

# Separating Features i.e questions and Labels i.e intents
feature =np.array(list(training_dict.keys()))
labels = np.array(list(training_dict.values()))
feature, labels
# WordVecotr with TF-IDF
from sklearn.feature_extraction.text import TfidfVectorizer
# Converting text to WordVector
tf_vec = TfidfVectorizer().fit(feature)
X = tf_vec.transform(feature).toarray()
# Reshaping labels to fit data
y = labels.reshape(-1)

# Classifier
from sklearn.ensemble import RandomForestClassifier
# Fitting model
rnn = RandomForestClassifier(n_estimators=200)
rnn.fit(X, y)

# Creating response

def botanswer(q):
    process_text = tf_vec.transform([q]).toarray()
    prob = rnn.predict_proba(process_text)[0]
    max_ = np.argmax(prob)

    if prob[max_] <= 0.2: #Only 60% and above accurate
        response_list.append("Sorry I am not getting you...!")
        return "Sorry I am not getting you...!"
    else:
        response_list.append(response_dict[rnn.classes_[max_]])
        return response_dict[rnn.classes_[max_]]

@app.route('/')
def home():
    return render_template('index.html',todos=chat_list, responses=response_list, zip=zip)

@app.route('/add', methods=['POST'])
def add_todo():
    task = request.form.get('task')
    if task:
        chat_list.append(task)
        botanswer(task)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
