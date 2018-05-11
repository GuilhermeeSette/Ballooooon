import csv

def ranking(nome, dodge):
    with open(r'Bas.csv','a') as data:
    
        writer = csv.writer(data)
        writer.writerow([nome,dodge])

    
    


def le_ranking():
  texto = csv.reader(open("Bas.csv","r"))
  for row in texto:
    print(row)


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
##ranking("Guilherme", "10")
##ranking("sgfgf", "10")
##ranking("Gkg", "9")
##ranking("hjk", "11")
##ranking("gkg", "12")
le_ranking()
