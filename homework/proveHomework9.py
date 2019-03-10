def read_count_file(fileName):
    ed_level = {}
    with open(fileName, "r") as file_in:
        for line in file_in:
            # .split by "," comma 
            words = line.split(",")
            if words[3] in ed_level:
                ed_level[words[3]] += 1
            else:
                ed_level[words[3]] = 1
    return ed_level

def main():
    fileName = "census.csv"
    ed_level = read_count_file(fileName)
    for type, count in ed_level.items():
        print("{} -- {}" .format(count, type))
    

if __name__ == "__main__":
    main()