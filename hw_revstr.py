class StringReverse:
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return " ".join(self.text.split()[::-1])


x = StringReverse("Hello World")

print(x)