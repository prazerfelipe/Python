frase = ('Curso em video Python')
frase1 = '  Aprenda Python   '
#Fatiamento
print(frase)
print(frase[3])
print(frase[3:13])
print(frase[:13])
print(frase[1:])
print(frase[1::2])

#Analise
print(len(frase)) #Conta os caracteres
print(frase.count("o")) #com os elemntos especificos
print(frase.count('o',0,13))
print(frase.find('deo'))
print(frase.find('Android'))
print('Curso' in frase)

#Transformação
print(frase.replace('Python', 'Android'))
print(frase.upper())
print(frase.lower())
print(frase.capitalize())
print(frase.title())
print(frase1.strip())
print(frase1.rstrip()) #lado direito
print(frase1.lstrip()) #lado esquerdo

#Divisão
print(frase.split())
#junção
print('-'.join(frase))