markdown
# 💰 Walleto API 1.0

<p align="center">
  Evolução do <strong>Walleto</strong> para uma arquitetura de backend escalável, mantendo uma base sólida já construída em CLI.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/status-em%20desenvolvimento-yellow?style=flat-square"/>
  <img src="https://img.shields.io/badge/cli-finalizada-brightgreen?style=flat-square"/>
  <img src="https://img.shields.io/badge/api-em%20constru%C3%A7%C3%A3o-blue?style=flat-square"/>
  <img src="https://img.shields.io/github/languages/top/honoriio/walleto-2.0?style=flat-square"/>
</p>

---

## 🧠 Sobre o Projeto

O **Walleto API 1.0** é a evolução do projeto **Walleto**, um gerenciador de finanças pessoais desenvolvido em Python.

A versão original (CLI) já está **finalizada, funcional e organizada**, com regras de negócio bem definidas.  
Nesta nova etapa, o objetivo é transformar essa base em uma **API REST**, preparada para integração com interfaces web, dashboards e aplicações futuras.

---

## ✅ Status do Projeto

| Módulo          | Status         |
|----------------|---------------|
| CLI            | ✅ Finalizado |
| Core lógica    | ✅ Estável    |
| Dashboard      | ✅ Funcional  |
| Exportação XLS | ✅ Implementado |
| API            | 🚧 Em desenvolvimento |
| PDF Export     | 🚧 Em desenvolvimento |

---

## ✨ Funcionalidades

### 🔹 Já implementadas
- Cadastro de gastos
- Edição de registros
- Remoção de gastos
- Listagem de dados financeiros
- Filtros por data e categoria
- Validações robustas
- Persistência com SQLite
- Exportação para **Excel (XLSX)**
- Dashboard com visualização de dados

### 🔹 Em evolução (API 1.0)
- Exposição via endpoints REST
- Estrutura desacoplada por camadas
- DTOs e casos de uso organizados
- Base para autenticação
- Exportação em PDF
- Integração com front-end

---

## 🧱 Arquitetura

### Estrutura atual (CLI consolidada)

```bash
walleto-2.0/
├── data/
├── docs/
├── logs/
├── src/
│   ├── core/
│   ├── models/
│   ├── repositories/
│   ├── services/
│   ├── utils/
│   └── views/
├── tests/
├── main.py
├── requirements.txt
````

---

### Estrutura nova (Walleto API 1.0)

```bash
walleto-api-1.0/
├── src/
│   ├── core/
│   ├── domain/
│   ├── application/
│   ├── infrastructure/
│   ├── presentation/
│   └── api/
├── tests/
├── main.py
├── requirements.txt
```

---

## ⚙️ Tecnologias

### Base atual

* Python
* SQLite
* Pandas
* OpenPyXL
* Streamlit
* Pytest

### API (stack prevista)

* FastAPI
* Pydantic
* SQLAlchemy

---

## 🛠️ Instalação

```bash
# Clonar o repositório
git clone https://github.com/honoriio/walleto-2.0.git

# Entrar na pasta
cd walleto-2.0

# Criar ambiente virtual
python3 -m venv env

# Ativar ambiente
source env/bin/activate  # Linux/macOS
env\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt
```

---

## ▶️ Como executar

### Rodar versão CLI

```bash
python main.py
```

---

### Rodar dashboard

```bash
streamlit run src/services/dashboard.py
```

---

## 📊 Exemplo de uso

```bash
Opção: 1
Nome: Mercado
Valor: 150.75
Categoria: Alimentação
Descrição: Compra do mês
Data: 25/01/2026
```

✔ Gasto registrado com sucesso.

---

## 🎯 Roadmap

### Concluído

* [x] CLI funcional
* [x] CRUD completo de gastos
* [x] Persistência com SQLite
* [x] Exportação XLSX
* [x] Dashboard

### Em andamento

* [ ] Implementação de exportação para PDF
* [ ] Refatoração para arquitetura limpa
* [ ] Criação da API REST
* [ ] Organização dos casos de uso

### Próximos passos

* [ ] Autenticação
* [ ] Múltiplos usuários
* [ ] Deploy
* [ ] Interface web

---

## 📈 Visão

O objetivo do Walleto é evoluir de uma aplicação local para um **ecossistema completo de gestão financeira**, com backend estruturado, integração com múltiplas interfaces e capacidade de escala.

---

## 🤝 Contribuições

Sinta-se à vontade para contribuir:

* Abrir issues
* Sugerir melhorias
* Enviar pull requests

---

## 📬 Contato

* 📧 Email: [diegohonoriiio@gmail.com](mailto:diegohonoriiio@gmail.com)
* 💼 LinkedIn: Diego Honório

---

## 📄 Licença

MIT License

```
