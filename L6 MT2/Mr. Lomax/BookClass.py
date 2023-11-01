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
        self._isbn = isbn

    def displayDetails(self):
        print(f"Title: {self._title}, author: {self._maker}, ISBN: {self._isbn}, On Loan?: {self._onLoan}, Date acquired: {self._dateAcquired}")

class CD(StockItem): 
    def __init__(self, title: str, maker: str, dateAcq: str, playingTime: int):
        super().__init__(title, maker, dateAcq)
        self._playingTime = playingTime

    def displayDetails(self):
        print(f"Title: {self._title}, artist: {self._maker}, playing time: {self._playingTime}, on Loan?: {self._onLoan}, Date acquired: {self._dateAcquired}")


b1 = Book("Meditations", "Marcus Aurelius", "10-10-21", 36123)
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
