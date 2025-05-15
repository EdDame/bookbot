def count_words(book_text):
    words = book_text.split()
    return words
# Function to count the number of words in the book text

def count_characters(book_text):
    character_counts = {}
    a = 'a'
    z = 'z'

    for char in book_text:
        lower_char = char.lower()
        # Convert the book text to lowercase for counting
        if a <= lower_char <= z:
            # Check if the character is an alphabetic character
            if lower_char in character_counts:
                character_counts[lower_char] += 1
            else:
                character_counts[lower_char] = 1
    
    return character_counts
    
       
def sort_dict(d):
    return d['num']
   

## for lower_char in character_counts), reverse=True)
    # Function to print the report of character counts
    
   
# input = entire book text as string
# output = dictionary with character counts"""