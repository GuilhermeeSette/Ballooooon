import csv

def ranking(nome, dodge):
    texto = csv.writer(open("E:\Ballooooon/PROJETO/Bas.csv", "w",newline=''))
    
    texto.writerow([nome,dodge])

    
    


def le_ranking():
  texto = csv.reader(open("E:\Ballooooon/PROJETO/Bas.csv","r"))
  for row in texto:
    print(row)


ranking("Guilherme", "10")
ranking("sgfgf", "10")
ranking("Gkg", "9")
ranking("hjk", "11")
ranking("gkg", "12")
le_ranking()
