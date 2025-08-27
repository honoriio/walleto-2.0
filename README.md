# walleto-2.0

<h1 align="center">💰 Walleto</h1>
<p align="center">
</p>

<p align="center">
  Um gerenciador de finanças pessoais feito com Python e SQLite. Simples, direto e funcional.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Status-Em desenvolvimento-yellow?style=flat-square"/>
  <img src="https://img.shields.io/github/languages/top/honoriio/walleto?style=flat-square"/>
  <img src="https://img.shields.io/github/last-commit/honoriio/walleto?style=flat-square"/>
</p>

---
## 🧠 Sobre o Projeto

**Walleto** é uma aplicação de terminal feita para ajudar no gerenciamento financeiro pessoal. Com uma arquitetura inspirada em padrões MVC, o projeto está estruturado para facilitar a manutenção, testes e expansão.

---

## ✨ Funcionalidades

- Registro de gastos com nome, valor, categoria, data e descrição
- Visualização de gastos por período e categoria
- Edição e remoção de registros
- Validações robustas de entrada
- Armazenamento local em SQLite
- Organização por camadas: `controllers`, `models`, `views`, `utils`
- Testes automatizados com estrutura pronta

---

## 🧱 Estrutura de Pastas

```bash
walleto/
├── data/                # Banco de dados SQLite
│   └── walleto.db
│
├── doc/                 # Documentações (em breve)
│
├── src/
│   ├── controllers/
│   │   └── database/
│   │       ├── connection.py
│   │       └── gasto_repository.py
│   │
│   ├── models/
│   ├── utils/
│   │   ├── input_utils.py
│   │   └── validacao.py
│   │
│   └── views/           # Interface de apresentação (em desenvolvimento)
│
├── tests/               # Testes automatizados
│
├── venv/                # Ambiente virtual
│
├── main.py              # Arquivo principal
├── README.md
├── TODO.md              # Lista de tarefas
├── coisas_a_fazer.txt   # Anotações do autor
└── LICENSE

---
```
## ⚙️ Tecnologias Utilizadas
<p align="left"> <img align="center" alt="Python" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg">&nbsp; <img align="center" alt="SQLite" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/sqlite/sqlite-original.svg">&nbsp; <img align="center" alt="VSCode" height="30" width="40" src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg"> </p>

---
## 📌 TODO
Você pode acompanhar o progresso nos seguintes arquivos:

- [`TODO.md`](TODO.md)
- [`coisas_a_fazer.txt`](coisas_a_fazer.txt)

---

## 🧠 Futuras Melhorias

- [ ] Interface gráfica com Tkinter ou PyQt  
- [ ] Exportação de dados para CSV  
- [ ] Dashboard com gráficos  
- [ ] Tela de login e múltiplos usuários  

---

### 🔧 Refatoração da função de filtragem

- [ ] Unificar a lógica de filtros em uma única função `filtrar_gastos()`, robusta e flexível.
- [ ] Permitir múltiplos filtros combinados:
  - Categoria
  - Local
  - Data (início e fim)
  - Valor (mínimo e máximo)
  - Descrição ou palavra-chave
- [x] **Decisão tomada:** manter uma única função de filtro "parruda", que aplica apenas os critérios informados.

---

### 📊 Função de soma e média de gastos

- [ ] Criar uma função para calcular a **soma total** e a **média de gastos**.
- [ ] A função usará os dados retornados pela `filtrar_gastos()`.
- [ ] Implementar cálculo de média mensal fixa.
- [ ] Permitir cálculo de totais por categoria ou período (baseado nos filtros aplicados).


---

## 🤝 Contribuições

Contribuições são bem-vindas!  
Sinta-se à vontade para:

- Abrir uma [issue](https://github.com/honoriio/walleto/issues)
- Sugerir melhorias
- Enviar um [pull request](https://github.com/honoriio/walleto/pulls)

---

## 📬 Contato

- 📧 Email: [diegohonoriiio@gmail.com](mailto:diegohonoriiio@gmail.com)  
- 💼 LinkedIn: [Diego Honório](https://www.linkedin.com/in/diego-hon%C3%B3rio-0102581a3/)  
- 📸 Instagram: [@](https://www.instagram.com/seuuser)

---

## 📄 Licença

Este projeto está licenciado sob a **MIT License** – veja o arquivo [LICENSE](LICENSE) para mais informações.
