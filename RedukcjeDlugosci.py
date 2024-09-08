import numpy as np

nr = 12

s0 = 1642.560  #surowa odleglosc
t = 17          #stopniCelsjusza
p = 751         #mmHg

k0 = -0.006     #stala dodawania
HD = 721.39     #wysokosc wzgl qazigeoidy (stanowisko)
iD = 1.83       #wysokosc instrumentu
HC = 495.00     #wysokokosc pkt wzgl quazigeoidy (cel)
iC = 1.46       #wysokosc pryzmatu
alfa = -8.8240  #kat pochylenia celowej

#odleglosc skosna
ka = s0/1000 * (281.948 - 105.786 * (p / (273.15 + t))) / 1000
S = s0 + k0 + ka
print(S)

#redukcje geometryczne
Dc = S * np.cos(alfa * np.pi / 200)

hD = HD + iD
hC = HC + iC
hm = (hD + hC) / 2
dh = (hC - hD)
Dm = np.sqrt(S ** 2 - dh ** 2)

D1 = np.sqrt((S ** 2 - dh ** 2) * (1 - dh / 6383000))
D2 = S * np.cos(alfa * np.pi / 200) - (S ** 2 / (2*6383000)) * np.sin(2 * alfa * np.pi / 200)

print(f'REDUKCJE ODLEGLOSCI SKOSNEJ NA POZIOM...\n'
      f'PRYZMAT      \t:\t Dc = {Dc: .3f} \n'
      f'SREDNI       \t:\t Dm = {Dm: .3f} \n'
      f'INSTRUMENT POZ\t:\t D  = {D1: .3f} \n'
      f'INSTRUMENT KAT\t:\t D  = {D2: .3f} \n')

print(f'REDUKCJE NA POZIOM...\n'
      f'poziom  \t \t     odleglosc    popr \n'
      f'pryzmat \t:\t d = {Dc: .4f} - {Dc * hC/6383000: .4f} = {Dc * (1 - hC/6383000): .3f} m\n'
      f'sredni  \t:\t d = {Dm: .4f} - {Dm * hm/6383000: .4f} = {Dm * (1 - hm/6383000): .3f} m\n'
      f'dalmierz \t:\t d = {D1: .4f} - {D1 * hD/6383000: .4f} = {D1 * (1 - hD/6383000): .3f} m\n'
      f'dalmierz \t:\t d = {D2: .4f} - {D2 * hD/6383000: .4f} = {D2 * (1 - hD/6383000): .3f} m\n')

# redukcja na poziom odniesienia
d = np.sqrt((S ** 2 - dh ** 2) * (1 - (hD + hC) / 6383000))
print(f'REDUKCJE BEZPOSREDNIO NA POZIOM ODNIESIENIA\n'
      f'd = {d: .3f} m\n')

pd = d * 0.999923 * 45000 ** 2 / (6383000 ** 2 * 2)
print(f'REDUKCJE NA PLASCZYZNE PL-2000\n'
      f'dGM = {d * 0.999923: .3f} + {pd: .4f} = {d * 0.999923 + pd: .3f} m\n')