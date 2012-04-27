class mixableString( object ):
    def __init__(self, text):
        self.text = list(text)

    def mixItUp(self):
        temp = self.text[3]
        self.text[3] = self.text[5]
        self.text[5] = temp
        temp = self.text[10]
        self.text[10] = self.text[6]
        self.text[6] = temp

    def get_text(self):
        return "".join(self.text)

original_string = 'this is a test'
test_string = mixableString(original_string)
test_string.mixItUp()
print original_string
print test_string.get_text()
