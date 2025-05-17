import random
import json
import pickle
import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer
import keras
print(keras.__version__)
from keras.models import load_model
lemmatizer = WordNetLemmatizer()
# Load the model
intents = json.loads(open('C:\\Users\\chhav\\OneDrive\\Desktop\\projects\\New folder\\sih-chatbot\\chatbot\\intents.json').read())
words = pickle.load(open('words.pkl', 'rb'))
classes = pickle.load(open('classes.pkl', 'rb'))
model = load_model('C:\\Users\\chhav\\OneDrive\\Desktop\\projects\\New folder\\sih-chatbot\\chatbot\\chatbot_model.keras')

ERROR_THRESHOLD = 0.25
# Load the model
def clean_up_sentence(sentence):
    # tokenize the pattern
    sentence_words = nltk.word_tokenize(sentence)
    # lemmatize each word and lower case it
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words

def bag_of_words(sentence):
    # initialize the bag of words
    bag = [0] * len(words)
    # tokenize the sentence
    sentence_words = clean_up_sentence(sentence)
    # create the bag of words
    for s in sentence_words:
        for i, w in enumerate(words):
            if w == s:
                bag[i] = 1
    return np.array(bag)
# Predict the class
def predict_class(sentence):
    # predict the class
    p = bag_of_words(sentence)
    res = model.predict(np.array([p]))[0]       
    ERROR_THRESHOLD = 0.25
    results = [[i, r] for i, r in enumerate(res) if r > ERROR_THRESHOLD]
    # sort by probability
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list
# Get the response
def get_response(intents_list, intents_json):
    tag = intents_list[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if i['tag'] == tag:
            response = random.choice(i['responses'])
            break
    return response
# Chat with the bot
print("Chatbot is running! Type 'exit' to stop.")
while True:
    message = input("")
    if message.lower() == "exit":
        break
    intents_list = predict_class(message)
    response = get_response(intents_list, intents)
    print(response)