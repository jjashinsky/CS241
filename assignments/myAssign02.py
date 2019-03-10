def prompt_filename():
    fileName = input("Please enter the data file: ")
    return fileName

# this code worked but took longer to gather the information I needed so I went with a different design. 
#def parse_file(fileName):
#    with open(fileName, mode = "r", encoding = "UTF-8") as file_in:
#        com_rate_list = []
#        # skips the header
#        next(file_in)
#        for line in file_in:
#            line = line.split(',')
#            com_rate_list.append(float(line[6]))
#            mean = sum(com_rate_list) / len(com_rate_list)
#        return mean

def parse_file(fileName):
    with open(fileName, mode = "r", encoding = "UTF-8") as file_in:
        countLine = 0
        sum = 0
        low = 5
        high = 0
        lowLine = 0
        highLine = 0
        # skips the header
        next(file_in)
        for line in file_in:
            line = line.split(',')
            countLine += 1
            sum += float(line[6])
            if float(line[6]) < low:
                low = float(line[6])
                lowLine = line
            if float(line[6]) > high:
                high = float(line[6])
                highLine = line
        return (sum/countLine, highLine, lowLine)

def main():
    fileName = prompt_filename()
    # summary is composed of 3 items, [average, list, list]
    summary = parse_file(fileName)
    
    # putting the list into its own list
    highLine = summary[1]
    
    #putting the list into its own list
    lowLine = summary[2]
    
    print("\nThe average commercial rate is: {}" .format(summary[0]))
    
    print("\nThe highest rate is:")
    print("{} ({}, {}) - ${}" .format(highLine[2],highLine[0],highLine[3], highLine[6]))
        
    print("\nThe lowest rate is:")
    print("{} ({}, {}) - ${}" .format(lowLine[2], lowLine[0], lowLine[3], float(lowLine[6])))
    
if __name__ == "__main__":
    main()