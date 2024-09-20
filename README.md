# Movie Up 📽️😎
## Descrição
**MovieUp** é um sistema web desenvolvido com Django que permite o cadastro, visualização e manipulação de informações sobre filmes em três categorias:
1. Filmes em cartaz.
2. Filmes que serão lançados em breve.
3. Filmes disponíveis em formato digital.

Os usuários podem gerenciar esses filmes através de um painel de administração, além de visualizar detalhes sobre os filmes diretamente no site.

## Funcionalidades
- **Cadastro de filmes**: Adicione novos filmes ao sistema, especificando sua categoria (em cartaz, em breve, digital).
- **Filtragem de filmes**: Filtre filmes por categoria e visualize detalhes.
- **Atualização de informações**: Edite as informações dos filmes cadastrados.
- **Remoção de filmes**: Exclua filmes que não estão mais disponíveis.

## Pré-requisitos
Antes de começar, você precisará ter as seguintes ferramentas instaladas em sua máquina:
- **Python 3.x**
- **Django 3.x ou superior**
- **Banco de Dados**: SQLite (por padrão no Django) ou outro de sua preferência (PostgreSQL, MySQL, etc.).

## Instalação

1. **Clone o repositório**:
   ```bash
   git clone https://github.com/seu-usuario/movieup.git
   ```

2. **Entre no diretório do projeto**:
   ```bash
   cd movieup
   ```

3. **Crie e ative um ambiente virtual**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate     # Windows
   ```

4. **Instale as dependências**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Realize as migrações do banco de dados**:
   ```bash
   python manage.py migrate
   ```

6. **Crie um superusuário para acessar o painel de administração**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Execute o servidor de desenvolvimento**:
   ```bash
   python manage.py runserver
   ```

## Uso

### Acesso ao Sistema
1. Após iniciar o servidor com o comando `runserver`, acesse o sistema no navegador:
   ```
   http://127.0.0.1:8000/
   ```

2. Para acessar o painel de administração e gerenciar os filmes cadastrados:
   ```
   http://127.0.0.1:8000/admin/
   ```

   Faça login com as credenciais do superusuário criadas anteriormente.

### Funcionalidades Principais

#### 1. Cadastrar Filmes
- No painel de administração, navegue até a seção **Filmes**.
- Clique em **Adicionar Filme**.
- Preencha os campos necessários, como o **nome do filme**, **descrição**, **categoria** (em cartaz, em breve, digital), e **data de lançamento**.

#### 2. Visualizar Filmes
- No site principal, os filmes estarão organizados em três seções:
  - **Filmes em Cartaz**
  - **Próximos Lançamentos**
  - **Disponível em Digital**

#### 3. Filtrar e Editar Filmes
- Filtre os filmes no painel de administração por sua categoria.
- Edite qualquer informação do filme clicando no título correspondente e salvando as alterações.

#### 4. Remover Filmes
- No painel de administração, selecione os filmes que deseja remover e utilize a opção de exclusão.

## Contribuição
1. Faça um fork do projeto.
2. Crie uma branch para sua funcionalidade: `git checkout -b minha-funcionalidade`.
3. Faça commit de suas alterações: `git commit -m 'Minha nova funcionalidade'`.
4. Envie para o repositório remoto: `git push origin minha-funcionalidade`.
5. Abra um pull request.

## Licença
Este projeto está licenciado sob a licença MIT - veja o arquivo [LICENSE](LICENSE) para mais detalhes.


# Movie Up 📽️😎
## Description
**MovieUp** is a web system developed with Django that allows the registration, viewing, and management of information about movies in three categories:
1. Movies currently showing.
2. Upcoming movies.
3. Movies available in digital format.

Users can manage these movies through an admin panel, and view details directly on the website.

## Features
- **Movie registration**: Add new movies to the system, specifying their category (currently showing, upcoming, digital).
- **Movie filtering**: Filter movies by category and view details.
- **Information update**: Edit the information of registered movies.
- **Movie removal**: Remove movies that are no longer available.

## Requirements
Before starting, you will need to have the following tools installed on your machine:
- **Python 3.x**
- **Django 3.x or higher**
- **Database**: SQLite (default in Django) or another of your choice (PostgreSQL, MySQL, etc.).

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/movieup.git
   ```

2. **Enter the project directory**:
   ```bash
   cd movieup
   ```

3. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate   # Windows
   ```

4. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run database migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser to access the admin panel**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Usage

### Accessing the System
1. After starting the server with the `runserver` command, access the system in your browser:
   ```
   http://127.0.0.1:8000/
   ```

2. To access the admin panel and manage the registered movies:
   ```
   http://127.0.0.1:8000/admin/
   ```

   Log in with the superuser credentials created earlier.

### Main Features

#### 1. Register Movies
- In the admin panel, go to the **Movies** section.
- Click on **Add Movie**.
- Fill in the required fields, such as **movie name**, **description**, **category** (currently showing, upcoming, digital), and **release date**.

#### 2. View Movies
- On the main website, movies will be organized into three sections:
  - **Currently Showing Movies**
  - **Upcoming Releases**
  - **Available in Digital**

#### 3. Filter and Edit Movies
- Filter movies in the admin panel by their category.
- Edit any movie's information by clicking on the corresponding title and saving the changes.

#### 4. Remove Movies
- In the admin panel, select the movies you want to remove and use the delete option.

## Contribution
1. Fork the project.
2. Create a branch for your feature: `git checkout -b my-feature`.
3. Commit your changes: `git commit -m 'My new feature'`.
4. Push to the remote repository: `git push origin my-feature`.
5. Open a pull request.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
