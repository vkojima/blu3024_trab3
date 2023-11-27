# Biblioteca Acadêmica
## Sobre o Projeto
Este projeto é um sistema simples de gerenciamento de biblioteca acadêmica desenvolvido em Node.js com Express para o servidor e HTML/JavaScript para o cliente. Ele permite aos usuários adicionar, visualizar, buscar e excluir informações sobre livros.

## Funcionalidades
- Adicionar Livros: Permite aos usuários enviar informações sobre novos livros para serem armazenados no servidor.
- Visualizar Todos os Livros: Os usuários podem ver uma lista de todos os livros disponíveis na biblioteca.
- Buscar Livros por ISBN: Permite aos usuários buscar informações detalhadas de um livro específico usando o ISBN.
- Excluir Livros: Os usuários podem excluir livros da lista.

## Tecnologias Utilizadas
- Backend: Node.js com Express
- Frontend: HTML, JavaScript

## Como Executar
### Pré-requisitos
- Node.js instalado
- NPM (Node Package Manager)

### Instalação
- Clone o repositório: git clone https://github.com/vkojima/blu3024_trab3.git
- Navegue até a pasta do projeto e instale as dependências:
```
cd caminho/para/o/projeto
npm install
```

### Executando o Servidor
Dentro da pasta do projeto, execute:
```
node app.js
```
O servidor estará rodando localmente na porta 3000.

### Acessando a Aplicação
Abra o navegador e acesse http://localhost:3000 para interagir com a aplicação.

## Estrutura do Projeto
- app.js: Arquivo principal do servidor Node.js/Express.
- public/: Pasta contendo arquivos estáticos para o cliente (HTML, JS).
