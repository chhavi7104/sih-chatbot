import random 
import json 
import pickle
import numpy as np
import tensorflow as tf
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt_tab')
from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()
intents = json.loads(open('C:\\Users\\chhav\\OneDrive\\Desktop\\projects\\New folder\\sih-chatbot\\chatbot\\intents.json').read())
words = []
classes = []
documents = []
ignore_words = ['?', '!', '.', ',', "'s", "'m", "'re", "'ll", "'ve", "'d", "'t", "n't", "(", ")", "[", "]", "{", "}", ";", ":", "\""]
# Preprocess the data
for intent in intents['intents']:
    for pattern in intent['patterns']:
        # tokenize each word
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        # add to documents
        documents.append((word_list, intent['tag']))
        # add to classes if not already there
        if intent['tag'] not in classes:
            classes.append(intent['tag'])
# lemmatize and lower each word and remove duplicates
words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
words = sorted(set(words))
# sort classes
classes = sorted(set(classes))
# save words and classes to pickle files
pickle.dump(words, open('words.pkl', 'wb'))
pickle.dump(classes, open('classes.pkl', 'wb'))
# create training data
training = []
output_empty = [0] * len(classes)
# create the training set
for doc in documents:
    # initialize the bag of words
    bag = []
    # list of tokenized words for the pattern
    pattern_words = doc[0]
    # lemmatize each word and lower case it
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    # create the bag of words
    for w in words:
        bag.append(1) if w in pattern_words else bag.append(0)
    # output is a 1 for the current tag and 0 for the rest
    output_row = list(output_empty)
    output_row[classes.index(doc[1])] = 1
    training.append([bag, output_row])
# shuffle the training data

random.shuffle(training)
training = np.array(training, dtype=object)

train_x = np.array([item[0] for item in training])
train_y = np.array([item[1] for item in training])
# create train and test sets

# save the training data to pickle files
model =tf.keras.Sequential()
model.add(tf.keras.layers.Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(64, activation='relu'))
model.add(tf.keras.layers.Dense(len(train_y[0]), activation='softmax'))
sgd = tf.keras.optimizers.SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])
# fit the model
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
# save the model
model.save('chatbot_model.keras')
# save the model to a pickle file
print("Model created")