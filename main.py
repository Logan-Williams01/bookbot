from stats import get_word_count
from stats import get_character_count
import sys

def get_book_text(filePath):
    with open(filePath) as f:
        return f.read()
    


    
def main():

    filePath = ""

    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        filePath = sys.argv[1]

    numWords = get_word_count(filePath)
    numChar = get_character_count(filePath)
    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filePath}...")
    print("----------- Word Count ----------")
    print(f"Found {numWords} total words")
    print("--------- Character Count -------")

    for i in numChar:
        if not i.isalpha():
            continue
        print(f"{i}: {numChar[i]}")

    print("============= END ===============")


main()