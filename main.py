def main():
    input("Pense em um personagem do universo dos incriveis, e eu tentarei adivinhar! \n Pressione Enter quando estiver pronto para começar...")

    #definindo se o persaongem é heroi ou não:
    personagem = input("Seu personagem é um super heroi? (Sim/Não/Não Sei): ").lower()

    #definido que é HEROI, vamos definir se é um heroi que morreu ou esta vivo
    if personagem == "sim": 
        personagem_heroi = input("Seu personagem já morreu? (Sim/Não/Não Sei): ").lower()
        if personagem_heroi == "não" or "nao": 
            perguntas_super_humano()
        elif personagem_heroi == "sim":
            perguntas_morreram()

    #definido que é HEROI, vamos definir se é um heroi que morreu ou esta vivo         
    elif personagem == "não" or "nao":
        personagem_outros = input("Seu personagem é humano? (Sim/Não/Não Sei): ").lower()
        if personagem_outros == "sim": 
            perguntas_humano()
        elif personagem_outros == "não" or "nao":
            print("Seu personagem é uma das versões do Omnidroid")
            

    elif personagem == "não sei" or "nao sei":
        print("Você não sabe??? só responda se seu personagem tem poderes ou não.")
    else:
        print("Resposta inválida. Por favor, responda com 'Sim', 'Não' ou 'Não Sei'.")




#Aqui já sabemos que é SUPER HEROI
def perguntas_super_humano():
    perguntas_super_humano_dict = {
        "familia_pera": "Seu super heroi faz parte da família Pera? (Sim/Não/Não Sei): ",
        "amigo_familia": "Seu super heroi é um amigo da família Pera? (Sim/Não/Não Sei): ",
        "feminino": "Seu super heroi é feminino? (Sim/Não/Não Sei): ",
        "masculino": "Seu super heroi é masculino? (Sim/Não/Não Sei): "
        # Continuar com mais perguntas para outros personagens se desejar
    }

    for caracteristica, pergunta in perguntas_super_humano_dict.items():
        resposta = input(pergunta).lower()
        if resposta == "sim":
            #perguntas finais referente a familia pera
            if caracteristica == "familia_pera":
                perguntas_familia_pera_dict = {
                    "Roberto Pera": "Seu super heroi tem super força? (Sim/Não/Não Sei): ",
                    "Helena Pera": "Seu super heroi anda de moto e estica? (Sim/Não/Não Sei): ",
                    "Zezé Pera": "Seu super heroi é um bebê metamorfo? (Sim/Não/Não Sei): ",
                    "Violeta Pera": "Seu super heroi fica invisível? (Sim/Não/Não Sei): ",
                    "Flexa Pera": "Seu super heroi está sempre com pressa? (Sim/Não/Não Sei): "
                    # Continuar com mais perguntas para outros personagens se desejar
                }

                for personagem, pergunta in perguntas_familia_pera_dict.items():
                    resposta_familia_pera = input(pergunta).lower()
                    if resposta_familia_pera == "sim":
                        print(f"Seu personagem é o {personagem.capitalize()}!")
                        return

                print("Não consegui adivinhar seu personagem da família Pera.")
                return

            # Adicionar mais condições para outros grupos de perguntas aqui, se necessário








#Função final
if __name__ == "__main__":
    main()
