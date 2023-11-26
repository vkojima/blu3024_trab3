const express = require('express');
const bodyParser = require('body-parser');
const app = express();
app.use(bodyParser.json());

let books = []; // Armazenamento temporário

app.post('/books', (req, res) => {
    books.push(req.body);
    res.status(201).send('Livro adicionado');
});

app.get('/books', (req, res) => {
    res.json(books);
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
