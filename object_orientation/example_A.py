class mixableString( object ):
    def __init__(self, text):
        self.__text = list(text)

    def mixItUp(self):
        temp = self.__text[3]
        self.__text[3] = self.__text[5]
        self.__text[5] = temp
        temp = self.text[10]
        self.__text[10] = self.__text[6]
        self.__text[6] = temp

    def get_text(self):
        return "".join(self.__text)

original_string = 'this is a test'
test_string = mixableString(original_string)
test_string.mixItUp()
print original_string
print test_string.get_text()
