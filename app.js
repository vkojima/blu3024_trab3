const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());

let books = [
    {"id": 1, "titulo": "Cem Anos de Solidão", "editora": "Harper & Row", "cidade": "Nova York", "ano": "1967", "pagina": "417", "isbn": "9780060531041", "assunto": ["Realismo mágico", "Ficção latino-americana"]},
    {"id": 2, "titulo": "1984", "editora": "Secker & Warburg", "cidade": "Londres", "ano": "1949", "pagina": "328", "isbn": "9780451524935", "assunto": ["Distopia", "Ficção política"]},
    {"id": 3, "titulo": "O Senhor dos Anéis: A Sociedade do Anel", "editora": "Allen & Unwin", "cidade": "Londres", "ano": "1954", "pagina": "423", "isbn": "9780261103573", "assunto": ["Fantasia épica", "Literatura de aventura"]},
    {"id": 4, "titulo": "O Pequeno Príncipe", "editora": "Reynal & Hitchcock", "cidade": "Nova York", "ano": "1943", "pagina": "96", "isbn": "9780156012195", "assunto": ["Literatura infantojuvenil", "Filosofia"]},
    {"id": 5, "titulo": "Harry Potter e a Pedra Filosofal", "editora": "Bloomsbury Publishing", "cidade": "Londres", "ano": "1997", "pagina": "223", "isbn": "9780747532743", "assunto": ["Fantasia", "Magia", "Aventura infantojuvenil"]}
]; // Armazenamento temporário

app.use(express.static('public'));

// Rota para servir o arquivo HTML na raiz
app.get('/', (req, res) => {
    res.sendFile(path.join(blu3024_trab3, 'public', 'index.html'));
});

app.get('/books', (req, res) => {
    res.json(books);
});

app.post('/books', (req, res) => {
    books.push(req.body);
    res.status(201).send('Livro adicionado');
});

app.get('/books/:isbn', (req, res) => {
    const book = books.find(b => b.isbn === req.params.isbn);
    if (book) {
        res.json(book);
    } else {
        res.status(404).send('Livro não encontrado');
    }
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
    console.log(`Servidor rodando na porta ${PORT}`);
});
