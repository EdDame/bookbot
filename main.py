from stats import count_words, count_characters, sort_dict
import sys

def get_book_text(book):
    with open(book) as f:
        return f.read()
# Function to read a book file and return its contents as a string
# input = book = filepath to book file
# output = main = contents of file as string
# I auto-commented the code to explain what it does, I am tired. __name__  has so many comments because it was my first time seeing it.


def main():
    book_text = get_book_text(sys.argv[1])
    # Call the function to read the book file and store its contents in a variable
    # The function get_book_text takes a file path as input and returns the contents of the file as a string
    # The file path is passed as an argument to the function
    character_counts = count_characters(book_text)
    
    character_list = []
    for char, num in character_counts.items():
        character_list.append({'char':char,'num': num})
    # Create a list of tuples containing the character and its count        
    character_list.sort(reverse=True, key=sort_dict)
    #sorts the tuble list by count (most > least)
    print(f"""" =========== BOOKBOT ============
    Analyzing book found at {sys.argv[1]}...
    ----------- Word Count ----------
    Found {len(count_words(book_text))} total words.
    --------- Character Count -------""")
    for entry in character_list:
        print(f"{entry['char']}: {entry['num']}")

    
    
    
   

if __name__ == "__main__":
    # Call the main function to execute the script
    # The __name__ variable is a special built-in variable in Python that evaluates to the name of the current module
    # If the module is being run directly, __name__ will be "__main__"
    # If the module is being imported, __name__ will be the name of the module
    # This allows you to run the script as a standalone program or import it without executing the main function
    main()

#main.py
# Function to read a book file and return its contents as a string




# input = book = filepath to book file
    # output = main = contents of file as string
