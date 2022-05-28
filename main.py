# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # the sorted strings are checked
    if (sorted(word) == sorted(anagram)):
        print("are they an anagram? ")
        print(True)
    else:
        print("are they an anagram? ")
        print(False)

        # driver code



word = input("Input First Word: ")
anagram = input("Input Second Word: ")
word= word.lower()
anagram = anagram.lower()
find_anagram(word, anagram)