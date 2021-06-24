def print_upper_word(words):
    """For a list of words, print out each word on a separate line, but in all uppercase. 
    Ex:
      upper(self, /) 
      Return a copy of the string converted to uppercase."""
      
    for word in words:
          print(word.upper())
          
"""
   Ex:
    startswith(...) 
    S.startswith(prefix[, start[, end]])"""  
 
def print_upper_words(words):
 
    for word in words:
        if word.startswith('e') or word.startswith('E'):
           print(word.upper())
            
           
""" Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters."""


""" From solutions:   Print each word on sep line, uppercased, if starts with one of given

        >>> print_upper_words3(["eagle", "Edward", "Alfred", "zope"],
        ...                   must_start_with=["A", "E"])
        EDWARD
        ALFRED
    """

def print_upper_words(words, must_start_with):

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
        

# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"], must_start_with={"h", "y"})