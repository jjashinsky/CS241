def get_file_name():
    fileName = input("Enter file: ")
    return fileName

def read_count_file(fileName):
    lineCount = 0
    wordCount = 0
    with open(fileName, "r") as file_in:
        for line in file_in:
            lineCount +=1
            # .split by space 
            words = line.split()
            wordCount += len(words)
    return (lineCount, wordCount)

def main():
    fileName = get_file_name()
    (lineCount, wordCount) = read_count_file(fileName)
    print("The file contains {} lines and {} words." .format(lineCount, wordCount))

if __name__ == "__main__":
    main()