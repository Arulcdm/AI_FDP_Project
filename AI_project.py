import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, SimpleRNN, Dense
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

# ------------------------------------------
# Streamlit App Title
# ------------------------------------------
st.title("📝 Basic Text Generator with RNN")
st.write("Enter a short starting phrase, and the model will generate the next few words using a simple RNN.")

# ------------------------------------------
# Sample Training Data (for demo purposes)
# ------------------------------------------
corpus = [
    "the quick brown fox jumps over the lazy dog",
    "the sun rises in the east",
    "the moon shines at night",
    "streamlit makes apps easy",
    "machine learning is fun",
    "deep learning powers AI",
    "data science is the future"
]

# ------------------------------------------
# Tokenization and Data Preparation
# ------------------------------------------
tokenizer = Tokenizer()
tokenizer.fit_on_texts(corpus)
total_words = len(tokenizer.word_index) + 1

input_sequences = []
for line in corpus:
    token_list = tokenizer.texts_to_sequences([line])[0]
    for i in range(1, len(token_list)):
        seq = token_list[:i+1]
        input_sequences.append(seq)

# Pad sequences
max_seq_len = max([len(x) for x in input_sequences])
input_sequences = pad_sequences(input_sequences, maxlen=max_seq_len, padding='pre')

# Split into inputs and labels
input_data = input_sequences[:, :-1]
labels = input_sequences[:, -1]
labels = tf.keras.utils.to_categorical(labels, num_classes=total_words)

# ------------------------------------------
# Build and Train the Model
# ------------------------------------------
model = Sequential()
model.add(Embedding(total_words, 10, input_length=max_seq_len-1))
model.add(SimpleRNN(50))
model.add(Dense(total_words, activation='softmax'))

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train model quickly (for demo)
model.fit(input_data, labels, epochs=300, verbose=0)

# ------------------------------------------
# Text Generation Function
# ------------------------------------------
def generate_text(seed_text, next_words=10):
    for _ in range(next_words):
        token_list = tokenizer.texts_to_sequences([seed_text])[0]
        token_list = pad_sequences([token_list], maxlen=max_seq_len-1, padding='pre')
        predicted = np.argmax(model.predict(token_list, verbose=0), axis=-1)[0]
        
        output_word = ""
        for word, index in tokenizer.word_index.items():
            if index == predicted:
                output_word = word
                break
        if output_word == "":
            break
        seed_text += " " + output_word
    return seed_text

# ------------------------------------------
# Streamlit Input and Output
# ------------------------------------------
user_input = st.text_input("Enter a starting phrase:", "")

if user_input:
    generated_text = generate_text(user_input)
    st.subheader("Generated Text:")
    st.write(generated_text)
