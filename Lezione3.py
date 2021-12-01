def somma_testo(my_testo):
  somma=0
  for line in my_testo.split('\n'):
    splitted_line=line.split(',')
    if splitted_line[0]!='Date':
      somma= somma+ float(splitted_line[1]) 
  return somma
 
my_file= open('Sales.csv', 'r')
my_stringa= my_file.read()
Risultato=somma_testo(my_stringa)
print(Risultato)