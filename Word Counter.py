"""
Level 1:
Task 3:
Create a python program that reads a text file and counts the number of words in it.
"""

def count_words(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
            words = content.split()
            print(f'Total Number of words: {len(words)}')
    except FileNotFoundError:
        print('Error: File not found.')
    except Exception as e:
        print('An Error occurred:', e)

file_name = input('Enter the file name: ')
count_words(file_name)
