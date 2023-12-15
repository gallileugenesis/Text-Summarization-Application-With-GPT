# Sumarizador de Texto GPT

Este projeto implementa um sumarizador de texto utilizando modelos de linguagem da OpenAI, como GPT-3.5 e GPT-4. A aplicação foi desenvolvida em Python e utiliza a biblioteca Streamlit para criar uma interface web interativa.

## Estrutura do Projeto
O projeto consiste em dois arquivos principais:

- summarizer_model.py: Contém a lógica para se conectar com a API da OpenAI e gerar resumos de texto.
- summarizer_app.py: Script para executar a aplicação Streamlit, fornecendo uma interface de usuário para a entrada de texto e exibição dos resumos.

## Funcionalidades

![png]("images/interface.jpeg")

![png]("https://github.com/gallileugenesis/text-summarization-application-with-gpt/blob/main/images/interface1.jpeg?raw=true")

- Seleção de diferentes modelos de linguagem (GPT-3.5, GPT-4).
- Escolha de estilos de sumarização personalizados com base no tipo de pessoa (Cientista, Estudante, etc.).
- Ajuste de hiperparâmetros como token, temperatura, nucleus sampling e frequência de penalidade.
- Entrada de texto através de área de texto ou upload de arquivos (txt, pdf, docx).
- Sumarização de texto alimentado por modelos de inteligência artificial.

## Como Usar
1) Clone o repositório do GitHub.
2) Instale as dependências utilizando pip install -r requirements.txt.
3) Execute o script summarizer_app.py para iniciar a aplicação Streamlit.
4) Abra o navegador e acesse localhost:8501 ou o endereço indicado no terminal.
5) Interaja com a aplicação conforme desejado para obter resumos de textos.

## Requisitos
- Python 3.7 ou superior.
- Bibliotecas: openai, streamlit, dotenv, os.
- Chave API da OpenAI.

## Contribuição
Contribuições para melhorar a aplicação são bem-vindas. Para contribuir, por favor, abra uma issue ou um pull request no repositório do GitHub.

## Licença
Este projeto está sob a licença MIT. Veja o arquivo [Licença MIT](https://github.com/gallileugenesis/text-summarization-application-with-gpt/blob/main/LICENSE) para mais detalhes.

 