def prompt_filename():
    fileName = input("Enter file: ")
    print("\nOpening file '{}' ".format(fileName))
    return fileName

    
def prompt_word_choice():
    users_choice = input("\nSearch the file for the word: ")
    return users_choice

def parse_file(fileName, users_choice):
    with open(fileName, mode = "r", encoding = "UTF-8") as file_in:
        wordCount = 0
        for line in file_in:
            # .split splits by space 
            words = line.split()
            for i in range(len(words)):
                if (words[i].lower() == users_choice.lower() or words[i].lower().find(users_choice.lower()) != -1):
                    wordCount += 1
        return wordCount
    
def main():
    fileName = prompt_filename()
    users_choice = prompt_word_choice()
    wordCount = parse_file(fileName, users_choice)
    print("\n'{}' appears {} times in the file '{}'" .format(users_choice, wordCount, fileName)) 
    
if __name__ == "__main__":
    main()