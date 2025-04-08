import pyautogui
import time
import pandas as pd

#Pra cada comando abaixo, vai pausar 1 segundo, pra dar tempo pra rodar tudo.
pyautogui.PAUSE = 1

# Abre o botão do windows, onde pode digitar ou procurar que programa abir.
pyautogui.press("win")

#Digita nesse botão para abrir o navegador chrome.
pyautogui.write("chrome")

#Faz com que abra o programa escolhido, nesse caso, o chrome.
pyautogui.press("enter")

#Faz o chrome digitar um site.
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

#Faz com que o navegador mande o usuário para o site digitado.
pyautogui.press("enter")

#Depois que entra no site, espera 3 segundos pra carregar tudo para a próxima ação.
time.sleep(3)

#coordenadas do mouse, ou seja, quando abrir o site, o mouse vai para o campo de email dele.
pyautogui.click(x=684, y=462)

#Escreve o email lá no campo de email do site.
pyautogui.write("wellington_python@teste.com")

#Aperta o botão para ir para outro campo, no caso, a senha.
pyautogui.press("tab")

#No campo senha, escreve a senha
pyautogui.write("senhateste123")

#Agora sai do campo senha e vai para o campo de login
pyautogui.press("tab")

#Clica no botão login e vai para próxima página onde o usuário estará logado.
pyautogui.press("enter")

#Espera mais 3 segundos para carregar a página de formulário.
time.sleep(3)

#Para ler o arquivo(base de dados). Tem que estar na mesma pasta desse código.
#dtype=str - lê todas as colunas como texto, mesmo que pareçam numeros.
tabela = pd.read_csv("produtos.csv", dtype=str)

print(tabela)  #Mostra tabela no console.

#Para cada linha da tabela, vai cadastrar todos os produtos do arquivo produtos.csv, um por um.
#index é um número, uma posição.
# [:5] Cadastra só os 5 primeiros produtos, se quiser cadastrar o restante, é só remover.
for linha in tabela.index[:5]:
    try:
        pyautogui.click(x=640, y=322) #Posição do mouse no primeiro campo do formulário.

        #Vai pegar o código que começa da linha 0 até a última linha. Localiza ela e vira String.
        codigo = str(tabela.loc[linha, "codigo"])
        pyautogui.write(codigo) #Escreve esse código no formulário.

        #Campo Marca
        pyautogui.click(x=662, y=456)
        marca = str(tabela.loc[linha, "marca"]) #Localiza a marca no arquivo em cada linha no formato de string.
        pyautogui.write(marca) #Escreve essa marca no formulário

        #Campo Tipo
        pyautogui.click(x=650, y=576) 
        tipo = str(tabela.loc[linha, "tipo"]) #Localiza o tipo no arquivo em cada linha no formato de string.
        pyautogui.write(tipo) #Escreve esse tipo no campo do formulário.

        #Campo categoria
        pyautogui.click(x=628, y=700) 
        categoria = str(tabela.loc[linha, "categoria"])  #Localiza a categoria no arquivo em cada linha. E transforma em String.
        pyautogui.write(categoria) #Escreve essa categoria no campo do formulário.

        #Campo Preço Unitário
        pyautogui.click(x=628, y=821) 
        preco_unitario = str(tabela.loc[linha, "preco_unitario"]) #Localiza o preço unitário no arquivo em cada linha. E transforma em String.
        pyautogui.write(preco_unitario) #Escreve esse preço unitário no campo do formulário.

        #Campo Custo
        pyautogui.click(x=656, y=949) 
        custo = str(tabela.loc[linha, "custo"]) #Localiza o custo no arquivo em cada linha. E transforma em String.
        pyautogui.write(custo) #Escreve esse custo no campo do formulário.

        #Vai para o próximo campo do formulário
        pyautogui.press("tab") 

        obs = tabela.loc[linha, "obs"] #Localiza observação(ões) no arquivo em cada linha
        
        #Se obs não for NaN(not a number ou não é um número), vai escrever o que estiver em obs.
        if not pd.isna(obs):
            pyautogui.write(str(obs)) #Escreve uma obs, se tiver no campo do formulário no formato de string.

        #Vai para o botão de enviar
        pyautogui.press("tab") 

        #Envia os dados   
        pyautogui.press("enter")

        time.sleep(1) #Espera 1 segundo antes de subir a tela e cadastrar o próximo produto

        #Para garantir que ao fim do formulário, para cadastrar o próximo produto, vá para o topo da página.
        pyautogui.scroll(5000)
    except Exception as erro:
        print(f"Erro ao cadastrar produto na linha {linha}: {erro}")