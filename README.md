🔐 API de Autenticação com JWT — FastAPI + PostgreSQL

Este projeto é uma API REST de autenticação de usuários utilizando **FastAPI**, **PostgreSQL** e **JWT (JSON Web Token)**. Ele fornece uma base segura, moderna e escalável para aplicações back-end que exigem controle de acesso, como sistemas de login, áreas protegidas e dashboards administrativos.

---

🚀 Funcionalidades

- ✅ Registro de usuários com senhas criptografadas (bcrypt)
- ✅ Login com verificação de credenciais e geração de token JWT
- ✅ Proteção de rotas usando autenticação via Bearer Token
- ✅ Rota segura `/me` que retorna dados do usuário autenticado
- ✅ Documentação automática com Swagger (acessível via `/docs`)
- ✅ Testes automatizados com `pytest` e `httpx`

---

🛠️ Tecnologias Utilizadas

- **FastAPI** — framework web moderno e assíncrono
- **SQLAlchemy** — ORM para interação com o PostgreSQL
- **PostgreSQL** — banco de dados relacional robusto
- **Pydantic** — validação de dados e schemas
- **Passlib + Bcrypt** — para hashing seguro de senhas
- **JWT (python-jose)** — geração e verificação de tokens
- **dotenv** — variáveis de ambiente seguras
- **pytest** — testes automatizados
- **httpx** — simulação de requisições HTTP nos testes

---

🧠 O que eu aprendi com esse projeto

Durante o desenvolvimento desta API, aprendi conceitos importantes e habilidades práticas fundamentais para atuar como desenvolvedor back-end:

- 📦 **Organização modular** de um projeto com FastAPI
- 🔐 **Segurança na autenticação** usando JWT e criptografia de senhas
- 🧱 **Modelagem de banco de dados relacional** com SQLAlchemy e PostgreSQL
- 🧪 **Criação de testes automatizados** para garantir a estabilidade das rotas
- ⚙️ **Uso de variáveis de ambiente** para proteger informações sensíveis
- 🛠️ **Integração de ferramentas modernas** de autenticação e documentação automática

---

📄 Licença

Desenvolvido por **Caio Silva**.
