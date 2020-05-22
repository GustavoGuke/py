
print("************************\n"
            "Aprendendo Python\n"
            "Projeto Mini Pizzaria\n"
      "************************\n")

pizzaPadrao = ['Calabreza','mussarela','Frango c/ catupiry']
cardapio = input("Faça o seu pedido\n"
                   "Calabreza: codigo = 1\n"
                   "mussarela: codigo = 2\n"
                   "Frango com catupiry: codigo = 3: \n")

if cardapio == '1':
    print ("Obrigado pela preferencia \n"
           "sua pizza de",pizzaPadrao[0], "ja esta sendo preparada!")
    
elif cardapio == '2':
    print ("Obrigado pela preferencia \n"
           "sua pizza de",pizzaPadrao[1], "ja esta sendo preparada!")
else:
      print ("Obrigado pela preferencia \n"
           "sua pizza de",pizzaPadrao[2], "ja esta sendo preparada!")


        
                   
                   
