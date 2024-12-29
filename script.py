from datetime import datetime
import re
from time import sleep

def formatar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if not validar_cpf(cpf):
        return "CPF inválido"
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf_formatado

def validar_cpf(cpf):
    cpf = re.sub(r'\D', '', cpf)
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:
        return False

    def calcular_digito(cpf, peso):
        soma = sum(int(cpf[i]) * peso[i] for i in range(len(peso)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    peso1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    digito1 = calcular_digito(cpf, peso1)
    if digito1 != int(cpf[9]):
        return False

    peso2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    digito2 = calcular_digito(cpf, peso2)
    if digito2 != int(cpf[10]):
        return False

    return True

def formatar_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)
    if not validar_cnpj(cnpj):
        return "CNPJ inválido"
    cnpj_formatado = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
    return cnpj_formatado

def validar_cnpj(cnpj):
    cnpj = re.sub(r'\D', '', cnpj)
    if len(cnpj) != 14:
        return False
    if cnpj == cnpj[0] * 14:
        return False

    def calcular_digito(cnpj, pesos):
        soma = sum(int(cnpj[i]) * pesos[i] for i in range(len(pesos)))
        resto = soma % 11
        return 0 if resto < 2 else 11 - resto

    pesos1 = [5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    digito1 = calcular_digito(cnpj, pesos1)
    if digito1 != int(cnpj[12]):
        return False

    pesos2 = [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]
    digito2 = calcular_digito(cnpj, pesos2)
    if digito2 != int(cnpj[13]):
        return False

    return True

def formatar_valor(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def obter_valor_formatado(mensagem):
    while True:
        entrada = input(mensagem)
        try:
            valor = float(entrada.replace(".", "").replace(",", "."))
            return valor
        except ValueError:
            print("Entrada inválida. Digite o valor no formato X.XXX,XX")

def imprimir_ratificacao(c_contrato, c_modelo, c_cor, c_ano, c_parcelas, c_novas_parcelas, c_valor, c_carencia):
    print('')
    print('Formalizamos um refinanciamento referente ao seu veículo:')
    print('Contrato: ', c_contrato)
    print('Modelo: ', c_modelo)
    print('Cor: ', c_cor)
    print('Ano: ', c_ano)
    print('Parcelas em atraso: ', c_parcelas)
    print('Quantidade de parcelas: ', c_novas_parcelas)
    print('Valor: ', formatar_valor(c_valor))
    print('Carência: ', c_carencia)

def imprimir_ratificacao_fisico(f_contrato, f_modelo, f_cor, f_ano, f_parcelas, f_novas_parcelas, f_valor, f_carencia):
    print('')
    print('Formalizamos um refinanciamento referente ao seu veículo:')
    print('Contrato: ', f_contrato)
    print('Modelo: ', f_modelo)
    print('Cor: ', f_cor)
    print('Ano: ', f_ano)
    print('Parcelas em atraso: ', f_parcelas)
    print('Quantidade de parcelas: ', f_novas_parcelas)
    print('Valor: ', formatar_valor(f_valor))
    print('Carência: ', f_carencia)

while True:
    print('\n MENU:')
    print('\n1 - Calculo de Refin')
    print('2 - Solicitar Boleto')
    print('3 - Formatar CPF/CNPJ')
    print('4 - Contra proposta do refin')
    print('5 - Ratificação de Boleto')
    print('6 - Ratificação de Refin')
    print('7 - Formatar texto')
    print('8 - Não posso ouvir áudio...')
    print('9 - Sair')

    escolha = input('\nEscolha uma das opções acima: ')

    if escolha == '1':
        valor_total = obter_valor_formatado('Digite o valor total do contrato (R$ X.XXX,XX): ')
        parcelas = int(input('Digite o total de parcelas desejadas: '))

        if valor_total >= 10000:
            valor_total += 4000
            novo_valor = valor_total / parcelas
        else:
            valor_total += 3000
            novo_valor = valor_total / parcelas

        carencia = int(input('Digite a carência desejada (30, 60 ou 90 dias): '))
        print(f"\nSem entrada, com {parcelas}X de {formatar_valor(novo_valor)}, e uma carência de {carencia} dias.\n")
        print('Lembrando que é apenas uma simulação, para solicitar o refinanciamento,\no banco irá analisar e pode retornar uma proposta com entrada, ou uma proposta diferente da solicitada')

    elif escolha == '2':
        contrato_input = input('Digite um número do contrato: ')
        valor_boleto = obter_valor_formatado('Valor do boleto a ser gerado (R$ X.XXX,XX): ')
        vencimento = input('Digite a data de vencimento do boleto (DD/MM/AAAA): ')

        try:
            data = datetime.strptime(vencimento, '%d/%m/%Y')
            nova_data = data.strftime("%d/%m/%Y")
        except ValueError:
            print('Formato de data inválido. Por favor, use o formato DD/MM/AAAA.')

        parcelas_input = input('Digite a(s) parcela(s) referente a esse boleto: ')
        parcelas = list(map(int, parcelas_input.split()))
        ho = float(input('Digite o valor do HO: '))
        login = input('Login: ')

        print('Poderia gerar esse boleto por gentileza: ')
        print('Contrato: ', contrato_input)
        print('Valor: ', formatar_valor(valor_boleto))
        print('Vencimento: ', nova_data)
        print('Parcela(s): ', parcelas)
        print(f'HO: {ho}%')
        print('Login: ', login)

    elif escolha == '3':
        while True:
            print('\n1 - CPF')
            print('2 - CNPJ')
            print('3 - Voltar')

            escolha2 = input('Escolha uma das opções acima: ')

            if escolha2 == '1':
                cpf_input = input("Digite o CPF (apenas números): ")
                if validar_cpf(cpf_input):
                    print("CPF formatado:", formatar_cpf(cpf_input))
                    break
                else:
                    print("CPF inválido!")

            elif escolha2 == '2':
                cnpj_input = input("Digite o CNPJ (apenas números): ")
                if validar_cnpj(cnpj_input):
                    print("CNPJ formatado:", formatar_cnpj(cnpj_input))
                    break
                else:
                    print("CNPJ inválido!")

            elif escolha2 == '3':
                break
            else:
                print("Opção inválida, tente novamente.")

    elif escolha == '4':
        entrada_input = obter_valor_formatado('Digite o valor da entrada (Se não tiver, digite 0): R$ ')
        ho = float(input('Digite a porcentagem de HO da entrada: '))
        parcela_entrada = int(input('Digite a parcela relacionada à entrada (Se não tiver, digite 0): '))

        novas_parcelas = int(input('Digite a quantidade de parcelas do refinanciamento: '))
        novo_valor = obter_valor_formatado('Digite o valor das novas parcelas: R$ ')
        carencia = int(input('Digite a carência (30, 60 ou 90 dias): '))

        entrada = entrada_input + (entrada_input * ho / 100)

        if entrada == 0 and parcela_entrada == 0:
            print(f'\n*Sem entrada, com {novas_parcelas} parcelas de {formatar_valor(novo_valor)}, com a carência de {carencia} dias.*')
        else:
            print(f'\n*Entrada de {formatar_valor(entrada)}, referente à parcela {parcela_entrada}, com {novas_parcelas} parcelas de {formatar_valor(novo_valor)}, com a carência de {carencia} dias.*')

    elif escolha == '5':
        contrato = int(input('Digite o contrato a ser ratificado: '))
        modelo = input('Digite o modelo do veículo: ')
        cor = input('Digite a cor do veículo: ')
        ano = int(input('Digite o ano do veículo: '))
        parcelas_in = input('Digite a(s) parcela(s) do boleto: ')
        parcelas_rat = list(map(int, parcelas_in.split()))
        vencidas = input('Digite quando venceu a parcela mais antiga (DD/MM/AAAA): ')
        novo_valor = obter_valor_formatado('Digite o valor do boleto (R$ X.XXX,XX): ')
        vencimento_para = input('Digite a nova data de vencimento (DD/MM/AAAA): ')

        print('\nFico feliz em saber que encontramos uma solução que atende às suas necessidades.\nPara formalizar nosso acordo, vou realizar algumas confirmações e a ratificação do contrato.')
        print('Formalizamos um acordo referente ao seu veículo:')

        print('Contrato:', contrato)
        print('Modelo:', modelo)
        print('Cor:', cor)
        print('Ano:', ano)
        print('Parcelas em atraso:', parcelas_rat)
        print('Vencidas desde:', vencidas)
        print('Novo valor do boleto:', formatar_valor(novo_valor))
        print('Novo vencimento:', vencimento_para)
        print("Não é possível modificar ou cancelar o acordo.\n"
      "A baixa de restrição ocorre em até 5 dias úteis.\n"
      "As linhas de crédito continuarão ativas.\n"
      "Em caso de não recebimento do boleto, favor entrar em contato por meio dos números 0800 722 0371 ou 0800 941 9296,\n"
      "o nosso horário de funcionamento é de segunda à sexta das 08h00 às 20h30 ou me contatar por aqui e assim que\n"
      "efetuar pagamento nos envie em seguida seu comprovante, por gentileza!\n"
      "Vou te contatar no dia do vencimento do boleto para verificar se possui alguma dúvida,\n"
      "se está tudo certo com o boleto e pagamento. É importante que atenda, tudo bem?\n"
      "O pagamento pode ser efetuado através de agências bancárias, aplicativo ou casas lotéricas.\n"
      "Em 15 minutos encaminho o boleto.\n"
      "Ficou com alguma dúvida? Te ajudo em algo mais?")


    elif escolha == '6':

        while True:
            print('\nEscolha o tipo de refinanciamento:')
            print('1 - Refin físico')
            print('2 - Refin coração')
            print('3 - Sair')

            sub_escolha = input('\nEscolha uma das opções acima: ')

            if sub_escolha == '1':
                print('\nRefin físico selecionado.')
                f_contrato = input('Digite o contrato a ser ratificado: ')
                f_modelo = input('Digite o modelo do veículo: ')
                f_cor = input('Digite a cor do veículo: ')
                f_ano = input('Digite o ano do veículo: ')
                f_parcelas = input('Digite as parcelas em atraso: ')
                f_novas_parcelas = int(input('Digite a quantidade de novas parcelas: '))
                f_valor = obter_valor_formatado('Digite o valor total (R$ X.XXX,XX): ')
                f_carencia = int(input('Digite a carência (30, 60 ou 90 dias): '))

                imprimir_ratificacao_fisico(f_contrato, f_modelo, f_cor, f_ano, f_parcelas, f_novas_parcelas, f_valor, f_carencia)

                print("\nÓtimo! Fico feliz em saber que encontramos uma solução que atende às suas necessidades. Para formalizar nosso acordo, vou realizar algumas confirmações e a ratificação do contrato. Antes de prosseguirmos, gostaria de confirmar alguns detalhes.")
                print('Formalizamos um refinanciamento referente ao seu veículo:')
                print(f'Contrato: {f_contrato}')
                print(f'Modelo: {f_modelo}')
                print(f'Cor: {f_cor}')
                print(f'Ano: {f_ano}')
                print(f'Parcelas em atraso: {f_parcelas}')
                print(f'Quantidade: {f_novas_parcelas}')
                print(f'Valor: {formatar_valor(f_valor)}')
                print(f'Carência: {f_carencia}')
                print("\nLembrando que é apenas uma simulação, o banco irá analisar e retornar uma proposta para sua solicitação, onde o setor responsável, entrará em contato.")
                print("O banco passa o retorno da proposta dentro de 5 a 7 dias úteis. Assim que a proposta voltar entraremos em contato para a finalização do acordo e envio do link, onde o financiado irá acessar e seguir com o passo a passo, inclusive realizar a validação através de uma selfie.")
                print("Não é possível modificar ou cancelar o acordo.")
                print("A baixa de restrição ocorre em até 5 dias úteis.")
                print("As linhas de crédito continuarão ativas.")
                print("Em caso de não recebimento do link, favor entrar em contato por meio dos números 0800 722 0371 ou 0800 941 9296, o nosso horário de funcionamento é de segunda à sexta das 08h00 às 20h30 ou me contatar por aqui.")
                print("É importante que responda o setor de refinanciamento, para receber o contrato para assinatura.")
                print("Ficou com alguma dúvida? Te ajudo em algo mais?")

            elif sub_escolha == '2':
                print('\nRefin coração selecionado.')
                c_contrato = input('Digite o contrato a ser ratificado: ')
                c_modelo = input('Digite o modelo do veículo: ')
                c_cor = input('Digite a cor do veículo: ')
                c_ano = input('Digite o ano do veículo: ')
                c_parcelas = input('Digite as parcelas em atraso: ')
                c_novas_parcelas = int(input('Digite a quantidade de novas parcelas: '))
                c_valor = obter_valor_formatado('Digite o valor total (R$ X.XXX,XX): ')
                c_carencia = int(input('Digite a carência (30, 60 ou 90 dias): '))

                imprimir_ratificacao(c_contrato, c_modelo, c_cor, c_ano, c_parcelas, c_novas_parcelas, c_valor, c_carencia)

                print("\nÓtimo! Fico feliz em saber que encontramos uma solução que atende às suas necessidades. Para formalizar nosso acordo, vou realizar algumas confirmações e a ratificação do contrato. Antes de prosseguirmos, gostaria de confirmar alguns detalhes.")
                print('Formalizamos um refinanciamento referente ao seu veículo:')
                print(f'Contrato: {c_contrato}')
                print(f'Modelo: {c_modelo}')
                print(f'Cor: {c_cor}')
                print(f'Ano: {c_ano}')
                print(f'Parcelas em atraso: {c_parcelas}')
                print(f'Quantidade: {c_novas_parcelas}')
                print(f'Valor: {formatar_valor(c_valor)}')
                print(f'Carência: {c_carencia}')
                print("\nLembrando que como é uma proposta de um refinanciamento pode ser que a parcela venha com uma alteração de R$20,00 para mais ou R$20,00 para menos.")
                print("O banco passa o retorno da proposta dentro de 5 a 7 dias úteis. Assim que a proposta voltar entraremos em contato para a finalização do acordo e envio do link, onde o financiado irá acessar e seguir com o passo a passo, inclusive realizar a validação através de uma selfie.")
                print("Não é possível modificar ou cancelar o acordo.")
                print("A baixa de restrição ocorre em até 5 dias úteis.")
                print("As linhas de crédito continuarão ativas.")
                print("Em caso de não recebimento do link, favor entrar em contato por meio dos números 0800 722 0371 ou 0800 941 9296, o nosso horário de funcionamento é de segunda à sexta das 08h00 às 20h30 ou me contatar por aqui.")
                print("É importante que responda o setor de refinanciamento para poder finalizar o link.")
                print("Ficou com alguma dúvida? Te ajudo em algo mais?")

            elif sub_escolha == '3':
                print('\nSaindo do menu de refinanciamento.')
                break

            else:
                print('Opção inválida. Por favor, escolha uma das opções.')


    elif escolha == '7':
        texto = input('Digite o texto para formatação: ')
        print(texto.upper())
        print(texto.lower())
        print(texto.title())

    elif escolha == '8':
        print('\nDesculpe, mas atualmente não posso ouvir áudios. Que tal digitar a sua dúvida ou solicitar algo por texto?\n')

    elif escolha == '9':
        print('\nSaindo do sistema. Obrigado!\n')
        sleep(2)
        break

    else:
        print('Opção inválida. Por favor, escolha uma das opções do menu.')
