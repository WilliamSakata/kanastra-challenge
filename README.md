# Kanastra-challenge

Teste prático realizado utilizando python com fast api no backend juntamente com a base Mysql e react.

Devido a alguns problemas o front-end não está rodando dentro de um container.

Para rodar o projeto basta executar o comando:

```bash
docker compose up
```

E para rodar o front-end executar os comandos:

```bash
cd kanastra-challenge-boilerplate
npm i
npm run dev:node
```

Ocorreram alguns problemas que impossibilitaram a conclusão do front-end, portanto é necessário fazer o upload do arquivo diretamente. Isso pode ser feito utilizando a própria interface do FastAPI. Basta acessar a url:

```
localhost:8000
```

e realizar o upload do arquivo pela rota

```
/post/debts
```

Uma vez que existam débitos cadastrados, o sistema irá fazer o envio de e-mails automático para os pagadores (feature não desenvolvida, pois segundo instruções não era necessário).
