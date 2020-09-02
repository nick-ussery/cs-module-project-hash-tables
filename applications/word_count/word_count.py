import re
import string


def word_count(s):
    # Your code here
    ignore_characters = [
        '\"',
        ':',
        ';',
        ',',
        '.',
        '-',
        '+',
        '=',
        '/',
        '\\',
        '|',
        '[',
        ']',
        '{',
        '}',
        '(',
        ')',
        '*',
        '^',
        '&'
    ]
    upper_s = s.lower()
    count = {}

    all_words = upper_s.split()

    for i in all_words:
        i = re.sub(r'[^\w\']', '', i)
        if i in count:
            count[i] += 1
        elif i != '':
            count[i] = 1
    print(count)
    return count


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count(
        'This is a test of the emergency broadcast network. This is only a test.'))
