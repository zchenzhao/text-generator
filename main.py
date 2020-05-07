from markov_generator import MarkovGenerator

if __name__ == '__main__':
    pass

    texts = [
                '/Users/cindyzhao/Downloads/war-and-peace.txt',
                '/Users/cindyzhao/Downloads/the-mysterious-affair-at-styles.txt',
                '/Users/cindyzhao/Downloads/the-secret-adversary.txt'
            ]

    texts2 = ['data/spiderman.txt']

    generator = MarkovGenerator()
    generator.train(texts)
    generated_text = generator.generate_text('dear')

    print(generated_text)
    