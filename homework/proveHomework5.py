
def get_file_name():
    fileName = input("File: ")
    return fileName

def check_balance(fileName):
    stack = []
    with open(fileName, "r") as file_in:
        for line in file_in:
            for i in line:
                if i == "(" or i == "[" or i == "{":
                    stack.append(i)
                elif (i == ")" and len(stack) != 0) and stack[-1] == "(":
                    stack.pop()
                elif (i == "}" and len(stack) != 0) and stack[-1] == "{": 
                    stack.pop()
                elif (i == "]" and len(stack) != 0) and stack[-1] == "[":
                    stack.pop()
                elif i != "}" or i != ")" or i != "]":
                    pass
                else:
                    print("Not balanced")
                    return
            
        


def main():
    fileName = get_file_name()
    stack = check_balance(fileName)
    

if __name__ == "__main__":
    main()
