# 📦 Sistema de Gestão de Estoque — Full-Stack

Aplicação web completa para controle de inventário e monitoramento de reposição de produtos, desenvolvida com foco em **regras de negócio reais de e-commerce**, persistência de dados e experiência do usuário.

![Preview do Sistema](./preview.png)
*(Dica: Suba o print da sua tela funcionando na pasta do projeto com o nome `preview.png` para que ele apareça automaticamente aqui!)*

---

## 🎯 Sobre o Projeto

Em operações de varejo e e-commerce, a falta de visibilidade sobre o estoque mínimo gera perda de vendas e atrasos logísticos. Este sistema resolve esse problema permitindo o cadastro dinâmico de itens e emitindo **alertas visuais automáticos** sempre que a quantidade atual fica abaixo do limite de segurança definido.

### ✨ Funcionalidades Principais
* **Cadastro de Produtos:** Registro de nome, preço unitário, quantidade em estoque e estoque mínimo exigido.
* **Monitoramento Inteligente (Alertas):** Identificação automática via interface dos itens que atingiram nível crítico de reposição.
* **Persistência em Banco de Dados:** Armazenamento relacional garantindo que os dados permaneçam salvos mesmo após reiniciar a aplicação.
* **Validação e Integridade:** Tratamento de entradas no back-end para impedir cadastros com valores inválidos ou campos vazios.
* **Exclusão Dinâmica:** Remoção rápida de registros diretamente pela interface sem necessidade de recarregar a página.

---

## 🛠️ Tecnologias Utilizadas

* **Front-end:** HTML5, CSS3 (Grid Layout & Design Responsivo) e JavaScript (Fetch API / Async-Await).
* **Back-end:** Python 3 com microframework **Flask** (Arquitetura RESTful).
* **Banco de Dados:** **SQLite3** (SQL relacional).
* **Versionamento:** Git & GitHub.

---

## 📂 Estrutura de Arquivos

```text
sistema-gestao-estoque/
│
├── app.py          # Servidor back-end, rotas da API REST e conexão com o banco SQL
├── index.html      # Interface web responsiva e consumo assíncrono da API
├── preview.png     # Captura de tela do sistema em funcionamento
└── README.md       # Documentação do projeto
```

---

## 🚀 Como Executar o Projeto Localmente

Siga os passos abaixo para testar a aplicação na sua máquina:

1. **Clone este repositório:**
   ```bash
   git clone https://github.com
   ```

2. **Acesse a pasta do projeto:**
   ```bash
   cd sistema-gestao-estoque
   ```

3. **Instale a dependência necessária (Flask):**
   ```bash
   pip install flask
   ```

4. **Inicie o servidor:**
   ```bash
   python app.py
   ```

5. **Acesse no navegador:**
   Abra `http://127.0.0.1:5000` para utilizar o sistema. *(O banco de dados `estoque.db` será criado automaticamente na primeira execução).*

---

## 👩‍💻 Autora

**Anauã Maria de Oliveira Silva**  
Engenheira de Software Full-Stack | HTML • CSS • JavaScript • Python • Java • C# • SQL

* 🔗 **LinkedIn:** [Anauã Maria](https://linkedin.com) *(substitua pelo link direto do seu perfil)*
* 💻 **GitHub:** [@anauaoliveira](https://github.com)
* ✉️ **E-mail:** anabrady49@gmail.com

