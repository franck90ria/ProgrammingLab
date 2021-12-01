class CSVFile():
  def __init__(self, nomefile):
    self.name = nomefile
    try:
      open(self.name, 'r')
    except:
      print('Il file non esiste')
     
  def get_data(self):
    dati = []
    my_file= open(self.name, 'r')
    for line in my_file:
      splitted_line=line.split(',')
      dati.append(splitted_line)
    return dati

class NumericalCSVFile(CSVFile):
  def __init__(self, nomefile):
    self.name = nomefile  
  
  def get_data(self):
    dati = []
    my_file= open(self.name, 'r')
    for line in my_file:
      splitted_line=line.split(',')
      if splitted_line[0]!='Date':
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


my_file= NumericalCSVFile('Sales3.csv')
print (my_file.get_data())
