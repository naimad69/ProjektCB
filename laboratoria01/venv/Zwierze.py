class zwierze:
    def __init__(self, ilosc_nog, drapieznik, szybki):
        self.ilosc_nog = 4
        self.drapieznik = True
        self.szybki = True

    def wyswietl(self):
        print(self.ilosc_nog, self.drapieznik, self.szybki)
        return 0

tygrys = zwierze(4, True, False)

tygrys.wyswietl()
tygrys.ilosc_nog = 9
tygrys.drapieznik = False
tygrys.wyswietl()