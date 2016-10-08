from keras.models import load_model
from sys import argv
from autocorrect import spell
import json, pickle, random, re, string
import numpy as np

diversity = 0.5
maxlen = 40

chars = pickle.load(open('chars.pkl', 'rb'))
char_indices = pickle.load(open('char_indices.pkl', 'rb'))
indices_char = pickle.load(open('indices_char.pkl', 'rb'))

model = load_model('brain.model')

def sample(preds, temperature=1.0):
    # helper function to sample an index from a probability array
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

def get_critique(data):
	phrases = data['description']['captions']
	# Only look at objects where P > 50%
	phrases = filter(lambda x: x['confidence'] > 0.5, phrases)
	# Sort from most likely to least likely
	phrases = sorted(phrases, key=lambda x: 1 - x['confidence'])
	seed = 'the artist has created ' + phrases[0]['text'] + '.'
	if len(seed) > maxlen:
		seed = seed[len(seed) - maxlen:]
	generated = ''
	sentence = seed
	generated += sentence
	for i in range(600):
	    x = np.zeros((1, maxlen, len(chars)))
	    for t, char in enumerate(sentence):\
	        x[0, t, char_indices[char]] = 1.

	    preds = model.predict(x, verbose=0)[0]
	    next_index = sample(preds, diversity)
	    next_char = indices_char[next_index]

	    generated += next_char
	    sentence = sentence[1:] + next_char
	return generated

def format_para(para):
	sentences = re.split('[.?]\\s*', para.replace('\n', ''))
	processed_sentences = []
	for sentence in sentences:
		processed_sentences.append(re.sub('^\s*', '', sentence).capitalize().replace(' i ', 'I'))
	formatted_para = string.join(processed_sentences, '. ')
	return formatted_para

def spell_para(para):
	sentences = re.split('[.?]\\s*', para)
	spelt_sentences = []
	for sentence in sentences[:-1]:
		words = sentence.replace('.', '').split(' ')
		spelt_words = []
		for word in words:
			spelt_words.append(spell(word))
		spelt_sentences.append(string.join(spelt_words, ' '))
	spelt_para = string.join(spelt_sentences, '. ') + '.'
	return spelt_para

data = json.loads(argv[1])
critique = get_critique(data)
# critique = 'a black and white photo of a large city.\ncould may be getted all trees that will of parallel: the artist responding and enous to predist, ons the mood, the artist\'s red abovedjen-xwest seems, the madonna and then want (and the setter actuan\'s faginators to suggest a foremur space. and the create even fisuing compositional conclusion of series. and the subjects, but a restrained and sunlike the background in impressical as we to emovelf.'

formatted_para = format_para(critique)
spelt_para = spell_para(formatted_para)

print spelt_para

