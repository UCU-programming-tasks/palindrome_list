'''Palindrome class realization.'''

from arraystack import ArrayStack


class Palindrome:
    '''
    Class for reading and writing data to files and finding palindromes.
    '''

    @staticmethod
    def read_file(filename: str) -> list:
        '''
        Read words from file.
        '''
        with open(filename, 'r') as input_file:
            words = [line.strip().split(' ')[0]
                     for line in input_file.readlines()]

        return words

    @staticmethod
    def write_to_file(filename: str, words: list):
        '''
        Read words to file.
        '''
        with open(filename, 'w') as output_file:
            output_file.write('\n'.join(words))

    @staticmethod
    def find_palindromes(input_filename: str, output_filename: str) -> list:
        '''
        Find palindrome words in the input file
        and write them to the output file.
        '''
        words = Palindrome.read_file(input_filename)
        palindromes = []

        for word in words:
            pre_middle_idx = len(word) // 2
            post_middle_idx = pre_middle_idx + (1 if len(word) % 2 else 0)
            first_half = ArrayStack()

            for idx in range(pre_middle_idx):
                first_half.add(word[idx])

            for idx in range(post_middle_idx, len(word)):
                if first_half.peek() != word[idx]:
                    break

                first_half.pop()

            if first_half.isEmpty():
                palindromes.append(word)

        Palindrome.write_to_file(output_filename, palindromes)

        return palindromes
