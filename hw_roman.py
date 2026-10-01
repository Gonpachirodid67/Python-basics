class Roman:
    def __init__(self, number):
        self.number = number

    def convert(self):
        values = [
            (1000, "M"),
            (900, "CM"),
            (500, "D"),
            (400, "CD"),
            (100, "C"),
            (90, "XC"),
            (50, "L"),
            (40, "XL"),
            (10, "X"),
            (9, "IX"),
            (5, "V"),
            (4, "IV"),
            (1, "I")
        ]

        result = ""

        for value, symbol in values:
            while self.number >= value:
                result += symbol
                self.number -= value

        return result


number = int(input("Enter an integer: "))

roman = Roman(number)
print("Roman numeral:", roman.convert())