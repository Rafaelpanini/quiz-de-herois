nome=input("qual e o seu nome?: ")
idade=int(input("qual a sua idade?: "))
cor=input("voce prefere qual dessas cores(verde, vermelho, amarelo)?: ")
tipo=input("voce prefere qual tipo de poder(magia, força, velocidade): ")
if cor=="vermelho":
   if tipo=="magia":
      print("feiticeira escarlate")
   elif tipo=="força":
       print('hulk vermelho')
   else:
       print("voce e o flash")
elif cor=="verde":
   if tipo=="magia":
       print("ben 10")
   elif tipo=="força":
       print("hulk")
   else:
       print("lanterna verde")
else:
   if tipo=="magia":
       print("doutor estranho")
   elif tipo=="força":
       print("wolverine")
   else:
       print("kid flash")