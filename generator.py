import numpy as np


def processed_text(text):
    unwanted_punctuation = '@#$%^&*()[]{}/\\`~<>\"\''

    text = text.lower()
    text = text.replace('.', ' .')
    text = text.replace(',', ' ,')
    text = text.replace('?', ' ?')
    text = text.replace('!', ' !')
    text = text.replace(':', ' :')
    text = text.replace(';', ' ;')
    text = text.replace('-', ' - ')

    for punctuation in unwanted_punctuation:
        text = text.replace(punctuation, '')

    return text


def generate_mapping(list_of_words, mapping=None):
    if not mapping:
        mapping = {}

    for i in range(len(list_of_words) - 1):
        current_word = list_of_words[i]
        next_word = list_of_words[i+1]

        if current_word not in mapping:
            mapping[current_word] = {}

        if next_word not in mapping[current_word]:
            mapping[current_word][next_word] = 0

        mapping[current_word][next_word] += 1

    return mapping


def generate_sentences(mapping, opening_word):
    list_of_generated_words = []
    current_word = opening_word

    for i in range(100):
        current_word_mapping = mapping[current_word]

        possible_following_words = list(current_word_mapping.keys())
        following_word_occurrences = [current_word_mapping[word] for word in possible_following_words]

        total_occurrences = sum(following_word_occurrences)
        following_word_probabilities = [occurrences / total_occurrences for occurrences in following_word_occurrences]

        next_word = np.random.choice(possible_following_words, 1, p=following_word_probabilities)[0]
        list_of_generated_words.append(current_word)
        current_word = next_word

    return ' '.join(list_of_generated_words)


def generate(list_of_texts):
    mapping = None

    for path in list_of_texts:
        text = training_text(path)
        text = processed_text(text)
        list_of_words = text.split()
        mapping = generate_mapping(list_of_words, mapping)

    opening_word = input('First word: ')
    generated_writing = generate_sentences(mapping, opening_word.lower())

    return generated_writing


def training_text(path):
    with open(path, 'r') as f:
        return f.read()


if __name__ == '__main__':
    generated_text = generate(
        [
            '/Users/cindyzhao/Downloads/war-and-peace.txt',
            '/Users/cindyzhao/Downloads/the-mysterious-affair-at-styles.txt',
            '/Users/cindyzhao/Downloads/the-secret-adversary.txt'
        ])

    print(generated_text)
    