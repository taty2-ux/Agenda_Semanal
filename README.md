# 📚 Agenda Semanal

Aplicação desenvolvida para auxiliar na organização da rotina de estudos, permitindo gerenciar horários, atividades e acompanhar o progresso semanal de forma simples e personalizada.

O projeto consiste em uma aplicação web desenvolvida com **Python e Flask**, integrada à **API Google Gemini** para gerar cronogramas de estudos personalizados. Além da aplicação web, o projeto disponibiliza um aplicativo desktop para gerenciamento das tarefas e acompanhamento do progresso dos estudos.

---

## ✨ Principais recursos

* 🤖 Geração automática de cronogramas utilizando Inteligência Artificial
* 🌐 Aplicação Web desenvolvida com Flask
* 💻 Aplicação Desktop desenvolvida com Tkinter
* 📄 Exportação da agenda em formato CSV
* 📊 Compatível com Microsoft Excel
* 📥 Download da agenda e do aplicativo diretamente pelo site

---

## 🖥️ Demonstração

### Site

<img width="1920" height="1080" alt="download (1)" src="https://github.com/user-attachments/assets/3c5eab86-9bf0-419b-9bbc-2c9b84324458" />

### Aplicativo Desktop

<img width="1920" height="1080" alt="download" src="https://github.com/user-attachments/assets/beccab00-82e5-4bb2-9bf5-230ea68e350d" />

---

## 📸 Interface

### Página inicial

<img width="1365" height="767" alt="Captura de tela 2026-07-23 014509" src="https://github.com/user-attachments/assets/5d55fb49-f44d-49e8-96db-bf39dfb40b37" />

### Agenda gerada

<img width="742" height="273" alt="Captura de tela 2026-07-23 225018" src="https://github.com/user-attachments/assets/627e1ef5-6964-4b0a-a037-638fa8341592" />

### Aplicativo Desktop

<img width="918" height="536" alt="Captura de tela 2026-07-23 154740" src="https://github.com/user-attachments/assets/e6886947-a322-4192-8cd0-64ff20582321" />


---

## 🚀 Funcionalidades

* Geração personalizada da agenda baseada na rotina informada pelo usuário (IA Gemini);
* Organização de horários semanais;
* Cadastro de tarefas;
* Exclusão de tarefas;
* Marcação de tarefas concluídas;
* Download da agenda em formato CSV;
* Download do aplicativo desktop;
* Leitura automática do arquivo CSV utilizado pela aplicação;
* Atualização das informações quando o arquivo CSV é alterado.

---

## 🤖 Como funciona

O usuário informa sua rotina de estudos, horários disponíveis, disciplinas e demais informações importantes através da aplicação web.

Esses dados são enviados para a **API Google Gemini**, que analisa as informações fornecidas e gera uma agenda personalizada.

Após a geração, o usuário pode:

* Baixar a agenda em formato CSV compatível com Microsoft Excel;
* Baixar o aplicativo desktop para gerenciar as tarefas localmente.

O aplicativo utiliza o mesmo arquivo CSV como fonte de dados. Dessa forma, qualquer alteração realizada diretamente nesse arquivo também é refletida automaticamente na aplicação.

---

## 📦 Download

Após gerar a agenda personalizada, o sistema disponibiliza:

* 📄 Agenda em formato CSV;
* 💻 Aplicativo desktop para gerenciamento das tarefas.

O executável encontra-se em:

```text
app/apk/arquivo_apk.exe
```

Basta executá-lo para utilizar a aplicação.

---

## 🛠️ Tecnologias utilizadas

### Linguagens

* Python
* HTML5
* CSS3
* JavaScript

### Frameworks e Bibliotecas

* Flask
* Tkinter
* Requests

### Integrações

* API Google Gemini

### Persistência de Dados

* Arquivos CSV

---

## 📂 Estrutura do projeto

```text
Agenda_Semanal/
│
├── app/
│   ├── apk/
│   ├── services/
│   ├── static/
│   ├── templates/
│   └── routes.py
│
├── main.py
├── .gitignore
└── README.md
```

---

## ⚙️ Como executar o projeto

### Pré-requisitos

* Python 3.10

### Instalação

Clone o repositório:

```bash
git clone https://github.com/taty2-ux/Agenda_Semanal.git
```

Acesse a pasta:

```bash
cd Agenda_Semanal
```

Crie um ambiente virtual:

```bash
py -m venv venv
```

Ative o ambiente virtual:

```bash
venv\Scripts\activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

Execute a aplicação:

```bash
python main.py
```

---

## 🎯 Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de aplicar conhecimentos em desenvolvimento web, organização de aplicações Python e integração com APIs de Inteligência Artificial.

Durante o desenvolvimento foram utilizados conceitos como:

* Arquitetura modular em Python;
* Desenvolvimento web utilizando Flask;
* Consumo de APIs REST;
* Manipulação e persistência de dados em arquivos CSV;
* Desenvolvimento de aplicações desktop utilizando Tkinter;
* Controle de versão com Git e GitHub.

---

## 📄 Licença

Este projeto foi desenvolvido para fins educacionais e composição de portfólio.

---

## 👩‍💻 Desenvolvedora

**Taiane Silva Santos**

GitHub: https://github.com/taty2-ux
