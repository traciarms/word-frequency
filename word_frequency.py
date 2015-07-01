# Your program should open sample.txt and read in the entirety of its
# text. You'll need to normalize the text so that words in different cases
# are still the same word and so it's scrubbed of punctuation. Once you've
# done that, go through the text and find the number of times each word is used.
#
# After that, find the top 20 words used and output them to the console in reverse
# order, along with their frequency, like this:
#
# peanut 33
# racket 31
# and 29
# common 21
# religion 15
# fate 14
# algorithm 10
# the 9

import re
import sys


def remove_ignore_list(book_list):

    my_ignore_list = ['a','able','about','across','after','all','almost','also',
                    'am','an','and','any','are','as','at','be','because',
                    'been','but','by','can','cannot','could','did','do','does',
                    'for','from','get','got','had','has','have','he','her','hers',
                    'him','his','how','however','i','if','in','into','is']

    book_list = filter(lambda book_list: book_list not in my_ignore_list, book_list)

    return book_list


def find_the_frequency(the_list):
    #my_string = "hello world"

    freq = {}

    for word in the_list:
        if word not in freq:
            freq[word] = 1
        else:
            freq[word] += 1

    freq_list = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    return freq_list


def find_count_divisor(this_list):
    max_found = this_list[0][1]
    count = 0

    while max_found/50 > 0:
        max_found -= 50
        count += 1

    return count


def scale_back_counts(the_list, scale):
    new_list = []

    for item in the_list:
        new_list.append([item[0], int(item[1]/scale)])

    return new_list


def print_word_frequency_list(my_word_frequency_list):

    for word in my_word_frequency_list:
        print("{}  {}".format(word[0], word[1]))


def print_hash_frequency_list(hash_list):
    prntstr = ''
    for item in hash_list:
        prntstr = prntstr+item[0]+'   '
        this_cnt = item[1]

        while this_cnt > 0:
            prntstr = prntstr+'#'
            this_cnt -=1

        prntstr = prntstr+'\n'

    print(prntstr)


def open_filter_book(book_name):
    with open(book_name) as my_book:

        # read the string from the book and replace new lines and lower case it
        book_string = my_book.read().replace('\n', ' ').lower()

        # now scrub all the punctuation
        book_string = re.sub(r'[^a-z ]', "", book_string)

        # now make the string into a list separated by spaces - ' '
        book_list = book_string.split(' ')

        # I am removing all elements in the list that are ''
        book_list = filter(lambda x: x != '', book_list)

        return book_list


if __name__ == "__main__":

    book_name = sys.argv[-1]
    #book_name = "sample2.txt"

    #open the book into a list and filter out unwanted characters
    book_list = open_filter_book(book_name)

    # take out the ignore list words before finding the frequency of words
    # in the list
    book_list = remove_ignore_list(book_list)

    # now find the frequency for every word in the list
    # this will be a list of tuples (word, freq)
    my_word_frequency_list = find_the_frequency(book_list)

    # ok now truncate the list to 20
    my_word_frequency_list = my_word_frequency_list[:20]

    # and print the list
    print_word_frequency_list(my_word_frequency_list)

    #find the divisor for the normalizer
    divisor = find_count_divisor(my_word_frequency_list)
    hash_list = scale_back_counts(my_word_frequency_list, divisor)

    print_hash_frequency_list(hash_list)
