class CSVFile():
  #definizione classe CSVFile
  def __init__(self, nomefile):
    #definisco le caratteristiche della            'medesima classe'= self, la classe avrà un nomefile
    self.name = nomefile
    #quando dico self.name= nome file, sto affermando che la caratteristica nome della classe è nomefile

    #l'obiettivo del try:(...) except:(...) è quello di aprire il file e leggerlo, nel caso non dovesse riuscirci, questo implicherebbe l'inesistenza
    try:
      open(self.name, 'r')
    except:
      print('Il file non esiste')
    #
      if not isinstance(self.name, str ):
        raise Exception('Il nome del file non è una stringa!')

   #definizione funzione get_data che ha come argomenti, self(ovvero la classe); start, che viene assegnato per nome ed end,anche lui assegnato per nome  
  def get_data(self, start=None, end=None):
    #definizione lista 'dati=[]' vuota. 
    #accoglienza nuovi valori
    dati = []
    #if (...) else(...), verifica argomenti start,end diversi dal valore none.Esistenza intervallo per lo slicing 
    if start!=None and end!=None:
      my_file= open(self.name, 'r')
      
    else
      
      
      
    #ciclo iterativo. Controllo line nel file.  
    for line in my_file:
      #creazione nuova linea 'splitted_line'. Assegnamento valore linea slittata alla ','
      splitted_line=line.split(',')
      #aggiunta 'splitted_line' (nuovo elemento) alla lista vuota. Comando .append(..)
      dati.append(splitted_line)
      #conclusione funzione. Return Lista Dati con elementi splittati
   return dati


#definizione sottoclasse della classe CSVFile. Principio ereditarietà classi, caratterestiche classe madre.
class NumericalCSVFile(CSVFile):
#definizione caratteristica classe
  def __init__(self, nomefile):
    self.name = nomefile  
  #definizone funzione di aggiunta di dati. creazione nuovi elementi. trasformazione in float.
  def get_data(self):
    dati = []
    #assegnamento variabile 'my_file' al valore self.name. Apertura. lettura.
    my_file= open(self.name, 'r')
    #ripetizione precedente.
    for line in my_file:
      #split linea alla ','. assegnamento valore splittato.
      splitted_line=line.split(',')
      #test valore splittato.
      #if valore splittato != da 0, ovvero colonna della 'Date', esecuzione...
      if splitted_line[0]!='Date':
        #dichiarazione nuova lista 'new_line[]' vuota.
        new_line= []
        
        for (i,element) in list(enumerate(splitted_line)):
          if(i==0):
            new_line.append(element)  
          else:
            try:
              new_line.append(float(element))
            except Exception as e:              
              print('L\'elemento non convertibile a float è: {}'.format(element))
              print('Aggiungo l\'elemento non convertito!')
              new_line.append(element)

        dati.append(new_line)
      else:
        dati.append(splitted_line)
    return dati

