import os

# Especifique o caminho do arquivo que você deseja apagar
arquivo_a_apagar = 'C:/Users/Arthur Coutinho/Desktop/Arthur Coutinho/final/final.xlsx'

# Verifique se o arquivo existe antes de tentar apagá-lo
if os.path.exists(arquivo_a_apagar):
    try:
        os.remove(arquivo_a_apagar)  # Use os.remove para apagar um arquivo
        print(f'O arquivo {arquivo_a_apagar} foi apagado com sucesso!')
    except Exception as e:
        print(f'Ocorreu um erro ao apagar o arquivo: {str(e)}')
else:
    print(f'O arquivo {arquivo_a_apagar} não existe.')
