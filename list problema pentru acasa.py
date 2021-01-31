prenume=['Mihai','George','Ana','Dan','Ion','Geta','Vio']
varsta=['14','23','15','14','12','41','39']
#a---------------------------------
print(prenume[0],'are varsta de',varsta[0] ,'ani')
print(prenume[1],'are varsta de',varsta[1] ,'ani')
print(prenume[2],'are varsta de',varsta[2] ,'ani')
print(prenume[3],'are varsta de',varsta[3] ,'ani')
print(prenume[4],'are varsta de',varsta[4] ,'ani')
print(prenume[5],'are varsta de',varsta[5] ,'ani')
print(prenume[6],'are varsta de',varsta[6] ,'ani')
#b---------------------------------
prenume.extend(['Andreea','Ioan'])
varsta.extend(['34','23'])
print(prenume)
print(varsta)
#c---------------------------------
del(prenume[2])
del(varsta[2])
print(prenume)
print(varsta)
#d---------------------------------
lista1=prenume[0:3]
print(lista1)
#e---------------------------------
print(prenume[::-1])
#f---------------------------------
lista1=prenume[2]  + ' ' + prenume[4]
lista2=varsta[2] + ' ' + varsta[4]
print(lista1)
print(lista2)

lista1=prenume[0:5]
lista2=varsta[0:5]
print(lista1)
print(lista2)

