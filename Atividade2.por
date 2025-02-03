programa
{
    funcao inicio()
    {
        // Variáveis
        cadeia nome[6]
        real gasto[6], desconto, total[6]
        inteiro total2 = 0, clientes = 0

        // Entrada: Valor do desconto do dia
        escreva("Qual o valor do desconto do dia? ")
        leia(desconto)

      escreva ("\n------------------------\n")
        

        // Entrada: Dados dos clientes
        para (inteiro i = 0; i < 6; i++)
        {
            escreva("\nQual o nome do cliente ", i + 1, "? ")
            leia(nome[i])
            escreva("Quanto ", nome[i], " gastou? " )
            
            leia(gasto[i])
        }

       
          	 escreva ("\n------------------------")


        para (inteiro i = 0; i < 6; i++)
        {
            se (gasto[i] >= 100)
            {
                total[i] = gasto[i] - desconto
                clientes++
                escreva ("\n\n-> ",nome[i], " recebeu desconto.\n")
                escreva("Valor total (com desconto): ",total[i])
                
                
            }

                    
            senao
            {
                total[i] = gasto[i]


              se (gasto[i] < 100)
            { 
            	escreva("\n\n",nome[i], " NÃO recebeu desconto \n")
            	escreva("Valor total: ", total[i])
            
            }

			   
            }		
            	// Soma ao total da loja
			 total2 += total[i]
       }
			escreva ("\n\n------------------------\n")
       		escreva("\nValor total recebido pela loja: ", total2, "\n")
        		escreva("Quantos usuários tiveram desconto: ", clientes, "\n")
			
	   
		
	   
      
      }
}

/* $$$ Portugol Studio $$$ 
 * 
 * Esta seção do arquivo guarda informações do Portugol Studio.
 * Você pode apagá-la se estiver utilizando outro editor.
 * 
 * @POSICAO-CURSOR = 722; 
 * @PONTOS-DE-PARADA = ;
 * @SIMBOLOS-INSPECIONADOS = ;
 * @FILTRO-ARVORE-TIPOS-DE-DADO = inteiro, real, logico, cadeia, caracter, vazio;
 * @FILTRO-ARVORE-TIPOS-DE-SIMBOLO = variavel, vetor, matriz, funcao;
 */