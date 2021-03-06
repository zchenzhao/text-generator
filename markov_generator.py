import numpy as np

class MarkovGenerator(object):

    def __init__(self):
        self._mapping = {}

    def train(self, paths_to_texts):
        for path in paths_to_texts:
            text = self._read_file(path)
            text = self._processed_text(text)
            list_of_words = text.split()
            self._map(list_of_words)

    def generate_text(self, opening_word):
        opening_word = opening_word.lower()

        if opening_word not in self._mapping:
            raise WordNotFoundError

        list_of_generated_words = []
        current_word = opening_word

        for i in range(100):
            current_word_mapping = self._mapping[current_word]

            possible_following_words = list(current_word_mapping.keys())
            following_word_occurrences = [current_word_mapping[word] for word in possible_following_words]

            total_occurrences = sum(following_word_occurrences)
            following_word_probabilities = [occurrences / total_occurrences for occurrences in following_word_occurrences]

            next_word = np.random.choice(possible_following_words, 1, p=following_word_probabilities)[0]
            list_of_generated_words.append(current_word)
            current_word = next_word

        unprocessed_generated_text = ' '.join(list_of_generated_words)
        generated_text = self._processed_generated_text(unprocessed_generated_text)

        return generated_text

    def _read_file(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return f.read()
        except FileNotFoundError:
            print(f'`{file_path}` does not exist.')

    def _processed_text(self, text):
        unwanted_punctuation = '@#$%^&*()[]{}/\\`~<>=+_'

        text = text.lower()
        text = text.replace('.', ' .')
        text = text.replace(',', ' ,')
        text = text.replace('?', ' ?')
        text = text.replace('!', ' !')
        text = text.replace(':', ' :')
        text = text.replace(';', ' ;')
        text = text.replace('-', ' - ')
        text = text.replace('"', ' "')

        for punctuation in unwanted_punctuation:
            text = text.replace(punctuation, '')

        return text

    def _processed_generated_text(self, text):
        text = text.replace(' .', '.')
        text = text.replace(' ,', ',')
        text = text.replace(' ?', '?')
        text = text.replace(' !', '!')
        text = text.replace(' :', ':')
        text = text.replace(' ;', ';')
        text = text.replace(' - ', '-')
        text = text.replace(' "', '"')

        return text

    def _map(self, list_of_words):
        for i in range(len(list_of_words) - 1):
            current_word = list_of_words[i]
            next_word = list_of_words[i+1]

            if current_word not in self._mapping:
                self._mapping[current_word] = {}

            if next_word not in self._mapping[current_word]:
                self._mapping[current_word][next_word] = 0

            self._mapping[current_word][next_word] += 1


class WordNotFoundError(Exception):
    pass