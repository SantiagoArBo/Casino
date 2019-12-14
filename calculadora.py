def comp(prob1,prob2,prob3,prob4):#prob1 y prob3 son las mismas pero de otras paginas
    valor1 = prob3/(prob1+prob3)
    valor2 = prob4/(prob2+prob4)
    respuesta = [[((valor1*prob1)-1)*100,valor1*100],[((valor2*prob2)-1)*100,valor2*100]]
    return respuesta
