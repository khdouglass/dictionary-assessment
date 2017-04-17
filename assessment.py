"""Dictionaries Assessment

**IMPORTANT:** These problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    word_counts = {}
    for word in phrase.split():
        word_counts[word] = word_counts.get(word, 0) + 1

    return word_counts


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon.

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

    If melon name does not exist, return 'No price found'.

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    melon_counts = {'Watermelon': 2.95, 'Cantaloupe': 2.50, 
                    'Musk': 3.25, 'Christmas': 14.25}

    return melon_counts.get(melon_name, 'No price found')


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.
    """

    #For example::

        # >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        # [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

        # >>> word_length_sorted(["porcupine", "ok"])
  

   # new_list = {}

   # my first approach below, identifying the length of each word and creating
   # a tuple with the length and word. I attempted to use an if/else statement to 
   # add words to the list of words corresponding to the length

    # for word in words:
    #     if len(words) in new_list:
    #         new_list[1].append(words[i])
    #     else: 
    #         new_list.append((len(word), [word]))

    # my next attempt creating a dictionary of lengths and words with that length.
    # the next step would have been to create a list of tuples including the length 
    # number and corresponding words.

    # for i in range(len(words)):
    #     length = len(words[i])
    # if length not in new_list:
    #     new_list[length] = [words[i]]
    # else:
    #     new_list[length.append(words[i])]

    #return list(new_list.items)




def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """

    english_to_pirate = {'sir': 'matey', 
                         'hotel': 'fleabag inn',
                         'student': 'swabbie',
                         'man': 'matey',
                         'professor': 'foul blaggart',
                         'restaurant': 'galley',
                         'your': 'yer',
                         'excuse': 'arr',
                         'students': 'swabbies',
                         'are': 'be',
                         'restroom': 'head',
                         'my': 'me',
                         'is': 'be'}

    pirate_translation = []

    for word in phrase.split():
        pirate_translation.append(english_to_pirate.get(word, word))
 
    return " ".join(pirate_translation)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.
       """

    # For example::

    #     >>> kids_game(["bagon", "baltoy", "yamask", "starly",
    #     ...            "nosepass", "kalob", "nicky", "booger"])
    #     ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    # (After "baltoy", there are no more y-words, so we end, even
    # though "nicky" and "booger" weren't used.)

    # Two more examples:

    #     >>> kids_game(["apple", "berry", "cherry"])
    #     ['apple']

    #     >>> kids_game(["noon", "naan", "nun"])
    #     ['noon', 'naan', 'nun']

    """This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # I first cretaed a dictionary of first letter keys and values were a list of
    # words with the cooresponding first letter

    # names_dict = {}

    # for i in range(len(names)):
    #     first_letter = names[i][0]
    #     if first_letter not in names_dict:
    #         names_dict[first_letter] = [names[i]]
    #     else:
    #         names_dict[first_letter].append(names[i])

    # new_name_list = [names[0]]
    # #new_name_list.append(names[0])
    # key = names[0][len(names[0]) - 1]

    # value_list = names_dict[key]

    # Next I was trying identify the first value in the values list, if it 
    # was already in our new list, it would iterate over the next values to find
    # one that hand not yet been added to the list.

    # def add_name(name):
    #     key_index = 0
    #     if key in names_dict:
    #         names_list = names_dict[key]
    #         if names_list[key_index] in new_name_list:
    #             key_index += 1
    #         elif names_list[key_index] not in new_name_list:
    #             new_name_list.append(names_list[key_index])
    #             key = name[len(next_name) - 1]
    #             add_name(key)
    #         else:
    #             return


            # names_list = names_dict[key]
            # if names_list[key_index] in new_name_list:
            #     key_index += 1
            # elif names_list[key_index] not in new_name_list:
            #     new_name_list.append(names_list[key_index])
            #     key = name[len(next_name) - 1]
            #     add_name(key)
            # else:
            #     return



    

    # while key in names_dict:
    #     next_name_list = names_dict[key]
    #     for name in next_name_list:
    #         if name not in new_name_list:
    #             new_name_list.append(name)
    #             key = name[len(next_name) - 1]
    #         else:
    #             break

    return new_name_list
       


        # next_names = names_dict[key]
        # for value in names_dict[key]:
        #     if value not in new_name_list:
        #         next_name = names_dict[key][1]
        #     else:
        #         new_name_list.append(next_name)
        #         key = next_name[len(next_name) - 1]
    


#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
