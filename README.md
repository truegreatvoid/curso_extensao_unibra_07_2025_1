# 👥 Projeto – Curso de Extensão UNIBRA | 07.2025

**Título do Curso:** GitHub Pro: Domine a Colaboração e o Código na Prática  
**Objetivo:** Este projeto foi desenvolvido como parte das atividades práticas do curso de extensão da UNIBRA, com foco em colaboração via GitHub, versionamento de código e construção de aplicações em grupo.

O sistema proposto é uma aplicação simples com autenticação de usuários com a funcionalidade do to-do como modulação, implementada com foco em boas práticas, organização de código e trabalho em equipe. A stack utilizada será majoritariamente baseada em Python/Django.

---

## 👨‍💻 Equipe – Grupo 2

| Nome             | Função    | GitHub                                             |
| ---------------- | --------- | -------------------------------------------------- |
| Kledson Vinicius | POO       | [@KledsonV](https://github.com/KledsonV)           |
| Tiago Xavier     | Backend   | [@truegreatvoid](https://github.com/truegreatvoid) |
| Carlos           | Frontend  | [@carloosph1](https://github.com/carloosph1)       |
| Warley           | Frontend  | [@warleyLucas](https://github.com/warleyLucas)     |
| Guilherme Brito  | Backend   | [@Dyadss](https://github.com/Dyadss)               |
| Gabriel Arnaud   | Professor | [@unibragabriel](https://github.com/unibragabriel) |

---

## 📘 Docs

### 🛠️ Ferramentas Necessárias

Para rodar este projeto localmente, é necessário ter as seguintes ferramentas instaladas:

- **[Python 3.13](https://www.python.org/downloads/release/python-3130/)**
- **[uv – Gerenciador de Pacotes Python](https://docs.astral.sh/uv/getting-started/installation/)**

> Certifique-se de que ambas estão corretamente configuradas no seu ambiente (variáveis de ambiente e PATH).

---

### 🚀 Executando o Projeto Localmente

Siga os passos abaixo para iniciar o ambiente de desenvolvimento:

#### 1. Instalar as dependências

No diretório raiz do projeto, execute:

```bash
uv sync
```

Esse comando irá criar o ambiente virtual automaticamente e instalar todas as dependências listadas no `pyproject.toml`.

#### 2. Iniciar o servidor de desenvolvimento

Após a instalação das dependências, execute:

```bash
uv run python manage.py runserver
```

Pronto! O servidor estará rodando em `http://127.0.0.1:8000/` por padrão.

---

### 🔑 Acesso Rápido

Você pode utilizar as credenciais abaixo para acessar o sistema com um usuário administrador pré-configurado:

- **Email:** `admin@admin.com.br`
- **Senha:** `1234`
