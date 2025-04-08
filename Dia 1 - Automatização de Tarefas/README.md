# 🖱️ Automatização de Cadastro de Produtos com PyAutoGUI

Este projeto automatiza o processo de cadastro de produtos em um site utilizando a biblioteca `PyAutoGUI` e dados contidos em um arquivo CSV. A automação abre o navegador, acessa o site, realiza o login e preenche um formulário com os dados dos produtos, um por um.

---

## 🚀 Tecnologias Utilizadas

- Python 🐍  
- Pandas 📊  
- PyAutoGUI 🖱️  
- Arquivo CSV como base de dados

---

## 🗂️ Estrutura dos Dados

A planilha `produtos.csv` deve conter as seguintes colunas:

```csv
codigo,marca,tipo,categoria,preco_unitario,custo,obs
```

Exemplo:

```csv
MOLO000251,Logitech,Mouse,1,25.95,6.50,
TEDE000341,Redragon,Teclado,1,149.90,60.00,Teclado mecânico
```

---

## 📋 Pré-requisitos

- Python instalado
- Instalar as bibliotecas necessárias:

```bash
pip install pyautogui pandas
```

---

## ⚙️ Como usar

1. Coloque o arquivo `produtos.csv` na mesma pasta do script.
2. Execute o script Python:

```bash
python main.py
```

3. O script fará:
   - Abertura do navegador
   - Acesso ao site de login
   - Login com as credenciais
   - Cadastro automático dos produtos contidos no CSV

> **Atenção:** Certifique-se de que a tela do computador esteja na resolução correta e que os elementos da tela (campos do formulário) estejam exatamente nas posições (coordenadas) esperadas pelo script.

---

## 🎥 Demonstração

Você pode ver uma demonstração de como o projeto funciona clicando no vídeo abaixo:





https://github.com/user-attachments/assets/786c65be-0507-4a84-bf9d-0595412caee1





---

## 📌 Observações

- O script está configurado para cadastrar apenas os **5 primeiros produtos**. Para cadastrar todos, remova o `[:5]` no loop:

```python
for linha in tabela.index:  # sem [:5]
```

- O campo `obs` só será preenchido se contiver informação (não será escrito "nan").
- Use com cuidado, pois o PyAutoGUI controla o mouse e o teclado — evite usar o computador enquanto o script estiver em execução.
