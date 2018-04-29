class zwierze:
    ilosc = ""
    drapieznik = ""
    szybki = ""
    def __init__(self, ilosc, drapieznik, szybki):
        self.ilosc_nog = ilosc
        self.drapieznik = drapieznik
        self.szybki = szybki

    def wyswietl(self):
        print(self.ilosc_nog, self.drapieznik, self.szybki)
        return 0

tygrys = zwierze(10, "Jest drapieznikiem", False)

tygrys.wyswietl()

class ssak(zwierze):
    def costam(self):
        zwierze.wyswietl(self)


X = ssak(10, "Działa!!!11", False)
X.wyswietl()



