def somma_lista(my_list):
  risultato=0
  for item in my_list:
    risultato= risultato + item 
  return risultato

my_list= range (50)
print (somma_lista(my_list))
