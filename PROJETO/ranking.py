import csv

def ranking(dodge, nome):
    with open(r'Bas.csv','a') as data:
        writer = csv.writer(data)
        writer.writerow([int(dodge),nome])

def le_ranking():
    lista = []
    maxi = 0
    texto = csv.reader(open("Bas.csv","r"))
    for row in texto:
        if len(row) != 0:
            lista.append(row)
    lista2 = []
    lista3 = []
    for i in range(0,len(lista)-1,1):
        if len(lista[i][0]) == 1:
            lista2.append(lista[i])
        elif len(lista[i][0]) == 2:
            lista3.append(lista[i])
    lista2 = (sorted(lista2))
    lista3 = (sorted(lista3))
    for j in lista2:
        print(j)
    for k in lista3:
        print(k)
            

##ranking("1", "Luiz")
##ranking("7", "dffd")
##ranking("43", "asdafg")
##ranking("0", "sgjjgh")
##ranking("78", "frhytjt")
##ranking("sgfgf", "10")
##ranking("Gkg", "9")
##ranking("hjk", "11")
##ranking("gkg", "12")
##ranking("Guilherme", "10")
##ranking("sgfgf", "10")
##ranking("Gkg", "9")
##ranking("hjk", "11")
##ranking("gkg", "12")
##ranking("Guilherme", "10")
##ranking("sgfgf", "10")
##ranking("Gkg", "9")
##ranking("hjk", "11")
##ranking("gkg", "12")
le_ranking()
