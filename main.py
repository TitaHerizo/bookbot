path_to_file = "./books/frankenstein.txt"

def main():
    with open(path_to_file) as f:
        file_contents = f.read()

    numWords = countNumberOfWords(file_contents)

    charRepetition = countRepetition(bookContent=file_contents)

    print(f"--- Begin report of {path_to_file} ---")
    
    print(f"{numWords} words found in the document")

    for char in charRepetition:
        print(f"The '{char}' character was found {charRepetition[char]} times")

    print("--- End report ---")

def countNumberOfWords(bookContent):
    return len(bookContent.split())

def countRepetition(bookContent):
    charList = list(bookContent.lower())

    uniqueChar = sorted(list("".join(filter(str.isalpha, list(set(charList))))))

    charRepetition = {} 
    for char in uniqueChar:
        charRepetition[char] = charList.count(char)

    return charRepetition

if __name__ =="__main__":
    main()
