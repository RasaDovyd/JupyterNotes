A = 55
def printA():
    print("As esu nauja PrintA() funkcija")
    print('Dar vienas paskutinis pakeitimas')


class Vehicles():
    def __init__(self, Pavadinimas, Rida):
        self. Pavadinimas = Pavadinimas
        self.Rida = Rida

class Car(Vehicles): # isirasom () tevines klases pavadinima
    def __init__(self, Pavadinimas, Rida, Seats):  # kintamuosius isirasome, tai ka paveldejom + naujas sios klases
        super().__init__(Pavadinimas, Rida)# kintamuosius isirasome, tai ka paveldejom
        self.Seats = Seats # isirasome trukstama kintamaji

    def GetSeats(self):
        Txt = self.Pavadinimas + "turi "+ str(self.Seats) + " sedimu vietu."
        return Txt
    
class Bus(Vehicles): 
    def __init__(self, Pavadinimas, Rida, Seats):  
        super().__init__(Pavadinimas, Rida)
        self.Seats = Seats 

    def GetSeats(self):
        Txt = self.Pavadinimas + "turi "+ str(self.Seats) + " sedimu vietu."
        return Txt
    
class Train(Vehicles): 
    def __init__(self, Pavadinimas, Rida, Seats):  
        super().__init__(Pavadinimas, Rida)
        self.Seats = Seats 

    def GetSeats(self):
        Txt = self.Pavadinimas + "turi "+ str(self.Seats) + " sedimu vietu."
        return Txt
    

class keturiolika_failu():
    '''
    Klase skirta paskaiciuoti kazkam.
    '''
    def __init__(self, Pavadinimas, Skirtukas):
        self.Pavadinimas = Pavadinimas
        self.Skirtukas = Skirtukas
        self.I = []
        self.U = []
        self.j = []
        self.p = []

    def dataReader(self):
        fname = self.Pavadinimas
        file = open(fname, mode='r', encoding= 'utf-8')
        sarasas = file.readlines()
        file.close()

        for eilute in sarasas[1::]:
            self.I.append(float(eilute.split(self.Skirtukas)[0]))
            self.U.append(float(eilute.split(self.Skirtukas)[1]))           
            self.j.append(float(eilute.split(self.Skirtukas)[2]))
            self.p.append(float(eilute.split(self.Skirtukas)[3].replace('\n', '')))

    def getPmax(self):
        Pmax = (max(self.p))
        return Pmax
    
    def getPCE(self):
        Pmax= self.getPmax()
        PCE = round((Pmax / 1000 * 100),2)
        return PCE
    

class Mokinys():
    '''
    Klase, kurioje skaiciavome Mokinys, Abiturientas, Mokykla.
    '''
    def __init__(self, Vardas, Pavarde, pazymiu_sarasas):
        self.Vardas = Vardas
        self.Pavarde = Pavarde
        self.pazymiu_sarasas= pazymiu_sarasas
        self.vid_max_min()

    def vid_max_min(self):
        vidurkis = sum(self.pazymiu_sarasas)/len(self.pazymiu_sarasas)
        maximumas = max(self.pazymiu_sarasas)
        mininimumas = min(self.pazymiu_sarasas)
        return (vidurkis, maximumas, mininimumas)
    
class Abiturientas(Mokinys):
    def __init__ (self, Vardas, Pavarde, pazymiu_sarasas, egzminai):
        super().__init__(Vardas, Pavarde, pazymiu_sarasas)
        self.egzaminai = egzminai
        self.prideti_egz_rez()

    def prideti_egz_rez(self):
        bendras_sarasas = self.pazymiu_sarasas + self.egzaminai
        bendras_vidurkits = sum(bendras_sarasas)/len(bendras_sarasas)
        return bendras_vidurkits   

class Mokykla():
    def __init__(self):
        self.Mokiniai = []
    def addMokinys(self, mokinys):
        self.Mokiniai.append(mokinys)
    def removeMokinys(self, mokinys):
        self.Mokiniai.remove(mokinys)
    def VisuMokiniuVidurkis(self):
        VisuMokiniuPazymiai = []
        for mokinys in self.Mokiniai:
            VisuMokiniuPazymiai.extend(mokinys.pazymiai) # extend leidzia sujungti skirtingus sarasus, prisplecia sarasas, esantis pries extend metoda
        VisuMokiniuVidurkis = sum(VisuMokiniuPazymiai)/len(VisuMokiniuPazymiai)
        return VisuMokiniuVidurkis