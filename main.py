from text_generator import TextGenerator

if __name__ == '__main__':
    pass

    texts = [
                '/Users/cindyzhao/Downloads/war-and-peace.txt',
                '/Users/cindyzhao/Downloads/the-mysterious-affair-at-styles.txt',
                '/Users/cindyzhao/Downloads/the-secret-adversary.txt'
            ]

    texts2 = ['data/spiderman.txt']

    generator = TextGenerator()
    generator.train(texts)
    generated_text = generator.generate_text('dear')

    print(generated_text)
    