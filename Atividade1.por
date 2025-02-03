programa
{
	
	funcao inicio()
	{
	
	cadeia nome,opcao1, opcao2,pagamento, pagamento2

	// ** Pergunta nome do cliente **
		escreva("Qual seu nome?\n")
		leia(nome)
		limpa()
		
	// ** Pergunta sobre o cliente **
		escreva("Vegetariano(a)? sim/nao\n")
		leia(opcao1)
		limpa()
		
	// ** Pergunta sobre o cliente **
		escreva("Está de dieta? sim/nao\n")
		leia(opcao2)
		limpa()
		 
	// ** Exibe nome do cliente **
			escreva ("Cliente: " ,nome)
			
	// ** lógica de respostas para o cliente de acordo com sua escolha **
			
		se (opcao1 == "sim") {
			
		se (opcao2 == "sim")
		
		  escreva ("\nSugestão de prato: Salada")}
		  
		  
		se (opcao1 =="nao"){

		se (opcao2 =="nao")	

		  escreva ("\nSugestão de prato: Feijoada")}

		  
		se (opcao1 =="nao"){
	     se (opcao2 =="sim")	

		  escreva ("\nSugestão de prato: Frango Grelhado")}
		  
		se (opcao1 =="sim"){
	     se (opcao2 =="nao")	

		  escreva ("\nSugestão de prato: Macarrao")}

	// ** Pergunta sobre a forma de pagamento **
	
		  escreva("\nQual a forma de pagamento? (dinheiro/cartao): ")
		  leia(pagamento)
		
	// ** Lógica para desconto caso seja pago em dinheiro **
		se (pagamento =="dinheiro")	{

		  escreva ("\n**Cliente possui 15% de desconto**")}

	

		  
}
}


/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 1137; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */