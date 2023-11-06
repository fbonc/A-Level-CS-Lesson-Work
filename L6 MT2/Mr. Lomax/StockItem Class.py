class StockItem:
    def __init__(self, title: str, maker: str, dateAcq: str):
        self._title = title
        self._maker = maker
        self._onLoan = False
        self._dateAcquired = dateAcq

    def setLoan(self):
        self._onLoan = True

    def ReturnLoan(self):
        self._onLoan = False


class Book(StockItem): 
    def __init__(self, title: str, maker: str, dateAcq: str, isbn: int):
        super().__init__(title, maker, dateAcq)
        self._isbn = self.ISBNCheck(isbn)


    def displayDetails(self):
        print(f"Title: {self._title}, author: {self._maker}, ISBN: {self._isbn}, On loan?: {self._onLoan}, Date acquired: {self._dateAcquired}")

    def ISBNCheck(self, isbn):
        ISBN = [int(i) for i in str(isbn)]

        calculatedDigit = 0
        Count = 1

        while Count < 13:
            calculatedDigit += ISBN[Count - 1]
            Count += 1
            calculatedDigit += ISBN[Count - 1] * 3
            Count += 1

        while calculatedDigit >= 10:
            calculatedDigit -= 10

        calculatedDigit = 10 - calculatedDigit

        if calculatedDigit == 10:
            calculatedDigit = 0

        if calculatedDigit == ISBN[12]:
            print("Valid ISBN")
            temp = int(''.join(str(digit) for digit in ISBN))
            return temp
        else:
            retry = input("Invalid ISBN, please try again: ")
            self.ISBNCheck(retry)


class CD(StockItem): 
    def __init__(self, title: str, maker: str, dateAcq: str, playTime: int):
        super().__init__(title, maker, dateAcq)
        self._playTime = playTime

    def displayDetails(self):
        print(f"Title: {self._title}, artist: {self._maker}, playing time: {self._playTime}, on loan?: {self._onLoan}, Date acquired: {self._dateAcquired}")


b1 = Book("Meditations", "Marcus Aurelius", "10-10-21", 9780099410676)
CD1 = CD("From Time", "Drake", "21-03-18", 189)
b1.displayDetails()
b1.setLoan()
b1.displayDetails()
b1.ReturnLoan()
b1.displayDetails()
print('')
CD1.displayDetails()
CD1.setLoan()   
CD1.displayDetails()
CD1.ReturnLoan()
CD1.displayDetails()
print()
