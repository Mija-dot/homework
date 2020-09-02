def zbraja(broj1, broj2):
    rezultat = broj1 + broj2
    return rezultat

br1 = int(input("Upisi prvi broj "))
br2 = int(input("Upisi drugi broj "))

zbroj= zbraja(br1,br2)
print("Zbroj brojeva iznosi ", zbroj)

def kub(broj1):
    rez= broj1 * broj1
    return rez

br1 = int(input("Upisi broj "))

kubni= kub(br1)
print("Kub zadanog broja iznosi ", kubni)

def brojac_koraka (br_koraka,duz_koraka):
    udaljenost= br1 * br2
    return udaljenost

br1 = int(input("Upisi broj koraka"))
br2 = float(input("Upisi duljinu koraka u metrima"))

brojac= brojac_koraka(br1, br2)
print("Prijedena udaljenost iznosi ", brojac ,"metara")

def apsolutna_razlika(br1,br2):
    if br1 > br2:
        return br1 - br2
    else:
        return br2 - br1

br1 = int(input("Upisi prvi broj"))
br2 = int(input("Upisi drugi broj"))

razlika= apsolutna_razlika(br1,br2)
print("Apsolutna razlika izmedu navedena dva broja iznosi ", razlika)





