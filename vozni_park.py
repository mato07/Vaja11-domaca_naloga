# -*- coding: utf-8 -*-

class Vozilo:
    def __init__(self, znamka, model, km, servis):
        self.znamka = znamka
        self.model = model
        self.km = km
        self.servis = servis

    def polno_ime(self):
        return self.znamka + " " + self.model

def seznam_vozil(vozni_park):
    print
    print "V voznem parku so naslednja vozila: "
    print
    for index, avto in enumerate(vozni_park):
        print "Vozilo " + str(index+1) + ")"
        print avto.polno_ime()
        print "Prevoženi kilometri: " + avto.km
        print "Datum zadnjega servisa: " + avto.servis
        print

def vnos_kilometrov(vozni_park):
    print
    for index, avto in enumerate(vozni_park):
        print str(index+1) + ") " + avto.polno_ime()
    print
    izbrano = raw_input("Izberi vozilo za katerega želiš spremeniti število prevoženih kilometrov: ")
    print
    izbrano_vozilo = vozni_park[int(izbrano)-1]

    novi_km = raw_input("Vnesi novo število prevoženih kilometrov: ")
    izbrano_vozilo.km = novi_km
    print
    print "Število prevoženih kilometrov je spremenjeno."
    print

def datum_servisa(vozni_park):
    print
    for index, avto in enumerate(vozni_park):
        print str(index+1) + ") " + avto.polno_ime()
    print
    izbrano = raw_input("Izberi vozilo za katerega želiš spremeniti datum zadnjega servisa: ")
    print
    izbrano_vozilo = vozni_park[int(izbrano)-1]

    novi_datum = raw_input("Vnesi nov datum zadnjega servisa: ")
    izbrano_vozilo.servis = novi_datum
    print
    print "Datum zadnjega servisa je spremenjen."
    print

def dodaj_vozilo(vozni_park):
    znamka = raw_input("Vnesi znamko novega službenega vozila: ")
    model = raw_input("Vnesi model novega službenega vozila: ")
    km = raw_input("Vnesi število prevoženih kilometrov novega službenega vozila: ")
    servis = raw_input("Vnesi datum zadnjega servisa novega službenega vozila: ")

    novo_vozilo = Vozilo(znamka, model, km, servis)
    vozni_park.append(novo_vozilo)
    print
    print novo_vozilo.polno_ime() + " je bilo dodano seznamu službenih vozil."

def izbrisi_vozilo(vozni_park):
    print
    for index, avto in enumerate(vozni_park):
        print str(index + 1) + ") " + avto.polno_ime()
    print
    izbrano = raw_input("Izberi vozilo, ki ga želiš izbrisati iz seznama službenihh vozil: ")
    print
    izbrano_vozilo = vozni_park[int(izbrano) - 1]

    vozni_park.remove(izbrano_vozilo)
    print
    print "Vozilo je bilo uspešno odstranjeno iz seznama službenih vozil."

def izpisi_vozila(vozni_park):

    vozila_file = open("Vozni park.txt", "w+")

    vozila_file.write("Seznam službenih vozil:\n")
    vozila_file.write("\n")

    for index, avto in enumerate(vozni_park):
        vozila_file.write("Vozilo " + str(index+1) + ")\n")
        vozila_file.write(avto.polno_ime() + "\n")
        vozila_file.write("Prevoženi kilometri: " + avto.km + "\n")
        vozila_file.write("Datum zadnjega servisa: " + avto.servis + "\n")
        vozila_file.write("\n")

def main():

    avto1 = Vozilo("Toyota", "Yaris", "20.000", "17.5.2017")
    avto2 = Vozilo("Ford", "Mustang", "40.000", "5.11.2017")
    kombi1 = Vozilo("Volkswagen", "Crafter", "100.000", "7.8.2017")
    kombi2 = Vozilo("Fiat", "Ducato", "80.000", "3.3.2017")
    tovornjak1 = Vozilo("Volvo", "FH", "60.000", "6.1.2017")
    tovornjak2 = Vozilo("Mercedes", "Actros", "200.000", "1.2.2017")


    vozila = [avto1, avto2, kombi1, kombi2, tovornjak1, tovornjak2]

    while True:
        print
        print "Pozdravljeni v programu za upravljanje s službenimi vozili!"
        print
        print "1) Prikaži seznam vozil"
        print "2) Uredi število prevoženih kilometrov za posamezno vozilo"
        print "3) Uredi datum zadnjega servisa za posamezno vozilo"
        print "4) Dodaj novo službeno vozilo"
        print "5) Izbriši službeno vozilo iz seznama"
        print "6) Izpiši službena vozila v txt. datoteki"
        print "7) Zapusti program"
        print

        ukaz = raw_input("Vnesi ustrezno številko: ")

        if ukaz == "1":
            seznam_vozil(vozila)
        elif ukaz == "2":
            vnos_kilometrov(vozila)
        elif ukaz == "3":
            datum_servisa(vozila)
        elif ukaz == "4":
            dodaj_vozilo(vozila)
        elif ukaz == "5":
            izbrisi_vozilo(vozila)
        elif ukaz == "6":
            izpisi_vozila(vozila)
        elif ukaz == "7":
            print
            print "Hvala za uporabo programa. Nasvidenje!"
            break
        else:
            print
            "Vaš ukaz je neveljaven. Prosimo ponovno vnesite število pred ukazom."
            continue

if __name__ == '__main__':
    main()

