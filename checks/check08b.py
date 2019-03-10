# Note that I used the checkpoint solutions in
# many parts of this code. I got stuck quite a bit

class GPA:
    
    def __init__(self):
        self._value = 0.0
        
    def _get_gpa(self):
        return self._value
    
    def _set_gpa(self, value):
        if value > 4.0:
            self._valuea = 4
        elif value < 0.0:
            self._value = 0
        else:
            self._value = value
    

    def _get_letter(self):
        if self._value <= .99:
            return "F"
        elif self._value <= 1.99:
            return "D"
        elif self._value <= 2.99:
            return "C"
        elif self._value <= 3.99:
            return "B"
        else:
            return "A"
    
    def _set_letter(self, letter):
        if letter == "A":
            self._value = 4.0
        elif letter == "B":
            self._value = 3.0
        elif letter == "C":
            self._value = 2.0
        elif letter == "D":
            self._value = 1.0
        else:
            self._value = 0
    
    
    @property
    def letter(self):
        return self._get_letter()
    
    @letter.setter
    def letter(self, letter):
        return self._set_letter(letter)
    
    gpa = property(_get_gpa, _set_gpa)
    

def main():
    
    student = GPA()
    
    print("Initial values:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    value = float(input("Enter a new GPA: "))

    student.gpa = value

    print("After setting value:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

    letter = input("Enter a new letter: ")

    student.letter = letter

    print("After setting letter:")
    print("GPA: {:.2f}".format(student.gpa))
    print("Letter: {}".format(student.letter))

if __name__ == "__main__":
    main()