## <b> 🖥 Kanvas </b>

## <b> 🛠 Tecnologias utilizadas </b>

#### Framework

- Django

#### Bibliotecas
- python-dotenv
- djangorestframework

<br>

## 🛠 Organização para ambiente do projeto

<p>Caso queira fazer uma clonagem e rodar o processo na sua máquina siga as seguintes instruções:</p>

1 - Inicie um ambiente virtual (<code>venv</code>) no seu projeto:

```sh
$ python -m venv venv && source venv/bin/activate
```

2 - Instale as dependências presentes no arquivo <code>requirements.txt</code> com o seguinte comando no terminal:
<br>

```
$ pip install -r requirements.txt
```

4 - Verifique as variáveis de ambientes de configuração necessárias no arquivo <code>.env.example</code>, crie uma cópia desse arquivo preencha as chaves necessárias e nomeie-o <code>.env</code>

3 - Em seguida, inicie a aplicação django rodando o seguinte comando no terminal:
<br>

```
$ ./manage.py runserver
```

<hr>
<br>

## <b> 🔚 Endpoints </b>

<br>

## <b> > Usuário </b>

<br>

### <b> Registro </b>

<i> POST /api/accounts/ </i>

Qualquer pessoa pode criar qualquer usuário:

```json
{
  "first_name": "John",
  "last_name": "Doe",
  "email": "john_doe@bol.com.br",
  "password": "1234",
  "is_admin": false
}
```

Dessa requisição é esperado um retorno com os dados do usuário cadastrado, como mostrado a seguir:

```json
{
  "uuid": "37c65691-d4fc-47e0-aef4-afe7b09c261f",
  "first_name": "John",
  "last_name": "Doe",
  "email": "john_doe@bol.com.br",
  "is_admin": false
}
```

<br>

### <b> Login </b>

<i> POST /api/login/ </i>

Esta API utiliza verificação por Token de autenticação, na grande maioria das próximas rotas será necessário o uso destes tokens.

```json
{
  "email": "john_doe@bol.com.br",
  "password": "1234"
}
```

Dessa requisição é esperado um retorno com o token de acesso do usuário, como mostrado a seguir:

```json
{
  "token": "76a6683c3a38c40caee04af738d279753e2c4d8d"
}
```

<br>

### <b> Listagem </b>

<i> GET /api/accounts/ </i>

Esse endpoint servirá para fazermos a listagem de usuários no curso:
Requer token de instrutor

<code>
    // REQUEST
</code><br>
<code>
    // Header -> Authorization: Token 'token-do-instrutor'
</code>

```json
[
  {
    "uuid": "61039ae4-7016-48d3-b90e-95a78b39e427",
    "first_name": "Maria",
    "last_name": "Joaquina",
    "email": "maria@bol.com.br",
    "is_admin": true
  },
  {
    "uuid": "af8af8b1-7d19-4032-b93d-04c84c66f8e1",
    "first_name": "João",
    "last_name": "Souza",
    "email": "joao@gmail.com.br",
    "is_admin": true
  },
  {
    "uuid": "5fef85a3-61e3-4e03-b6bd-ee544cd9bcdd",
    "first_name": "Joaquim",
    "last_name": "Ferreira",
    "email": "joaquim@hotmail.com.br",
    "is_admin": false
  },
  {
    "uuid": "5f2747f3-8899-49d9-b7f9-4ade850db837",
    "first_name": "Marcelo",
    "last_name": "Soares",
    "email": "marcelo@bol.com.br",
    "is_admin": false
  },
  {
    "uuid": "f09c6c88-6cd3-4ed9-b818-432e9f8df11c",
    "first_name": "Pedro",
    "last_name": "Martins",
    "email": "pedro@bol.com.br",
    "is_admin": false
  }
]
```

<br>

### <b> Cadastrando um endereço para o usuário </b>

<i> PUT /api/address/ </i>

Esse endpoint deverá fazer a criação do endereço, caso ele não exista e associá-lo ao usuário logado:

<code>
    // REQUEST
</code><br>
<code>
    // Header -> Authorization: Token 'token-do-instrutor'
</code>

```json
{
  "zip_code": "123456789",
  "street": "Rua das Flores",
  "house_number": "123",
  "city": "Curitiba",
  "state": "Paraná",
  "country": "Brasil"
}
```

Exemplo de resposta dessa rota:

```json
{
  "uuid": "7bf9d19a-2c22-4daa-b7dc-30be78bf1047",
  "street": "Rua das Flores",
  "city": "Curitiba",
  "state": "Paraná",
  "zip_code": "123456789",
  "country": "Brasil",
  "users": [
    {
      "uuid": "38f8b8b7-8edc-4685-9369-643bb85169d2",
      "first_name": "John",
      "last_name": "Doe",
      "email": "john_doe@bol.com.br",
      "is_admin": false
    }
  ]
}
```

<br>

## <b> > Cursos </b>

<br>

### <b> Registro </b>

<i> POST /api/courses/ </i>

Esse endpoint servirá para realizar a criação de cursos na plataforma Kanvas, somente instrutores poderão criar, atualizar, deletar e matricular estudantes nos cursos:

<code>
    // REQUEST
</code><br>
<code>
    // Header -> Authorization: Token 'token-do-instrutor'
</code><br><br>

```json
{
  "name": "Django",
  "demo_time": "9:00",
  "link_repo": "https://gitlab.com/turma_django/"
}
```

Dessa requisição é esperado um retorno com os dados do curso cadastrado, como mostrado a seguir:

```json
{
  "uuid": "7c32c787-83c3-4994-8f45-b6ef113cde5e",
  "name": "Django",
  "demo_time": "09:00:00",
  "created_at": "2022-02-15T19:12:44.914032Z",
  "link_repo": "https://gitlab.com/turma_django/",
  "instructor": null,
  "students": []
}
```

<br>

### <b> Listagem </b>

<br>

<i> GET /api/courses/ </i>

Este endpoint pode ser acessado por qualquer client (mesmo sem autenticação). A resposta do servidor deve trazer uma lista de cursos, mostrando cada aluno inscrito, no seguinte formato:

```json
[
  {
    "uuid": "87556b7e-ac9a-4a8d-9b9f-c2ea7e956a94",
    "name": "Django",
    "demo_time": "09:00:00",
    "created_at": "2022-02-15T19:08:15.927682Z",
    "link_repo": "https://gitlab.com/turma_django/",
    "instructor": null,
    "students": [
      {
        "uuid": "5fef85a3-61e3-4e03-b6bd-ee544cd9bcdd",
        "first_name": "Joaquim",
        "last_name": "Ferreira",
        "email": "joaquim@hotmail.com.br",
        "is_admin": false
      }
    ]
  },
  {
    "uuid": "696e31d3-2dd4-42b5-9d2d-4f92035a13fb",
    "name": "Node",
    "demo_time": "09:00:00",
    "created_at": "2022-02-15T19:09:29.898611Z",
    "link_repo": "https://gitlab.com/turma_node/",
    "instructor": null,
    "students": [
      {
        "uuid": "5f2747f3-8899-49d9-b7f9-4ade850db837",
        "first_name": "Marcelo",
        "last_name": "Soares",
        "email": "marcelo@bol.com.br",
        "is_admin": false
      }
    ]
  },
  {
    "uuid": "787673a7-fa4e-4bb8-9ec1-eabbba02fca5",
    "name": "React",
    "demo_time": "09:00:00",
    "created_at": "2022-02-15T19:10:43.883684Z",
    "link_repo": "https://gitlab.com/turma_django/",
    "instructor": {
      "uuid": "61039ae4-7016-48d3-b90e-95a78b39e427",
      "first_name": "Maria",
      "last_name": "Joaquina",
      "email": "maria@bol.com.br",
      "is_admin": true
    },
    "students": [
      {
        "uuid": "5f2747f3-8899-49d9-b7f9-4ade850db837",
        "first_name": "Marcelo",
        "last_name": "Soares",
        "email": "marcelo@bol.com.br",
        "is_admin": false
      },
      {
        "uuid": "f09c6c88-6cd3-4ed9-b818-432e9f8df11c",
        "first_name": "Pedro",
        "last_name": "Martins",
        "email": "pedro@bol.com.br",
        "is_admin": false
      }
    ]
  }
]
```

<i> GET /api/courses/\<id\>/ </i>

Este endpoint pode ser acessado por qualquer client (mesmo sem autenticação). A resposta do servidor deve trazer o elemento filtrado pelo id do curso informado na url, e deverá ter o seguinte formato:<br>

```json
{
  "uuid": "87556b7e-ac9a-4a8d-9b9f-c2ea7e956a94",
  "name": "Django",
  "demo_time": "09:00:00",
  "created_at": "2022-02-15T19:08:15.927682Z",
  "link_repo": "https://gitlab.com/turma_django/",
  "instructor": null,
  "students": [
    {
      "uuid": "5fef85a3-61e3-4e03-b6bd-ee544cd9bcdd",
      "first_name": "Joaquim",
      "last_name": "Ferreira",
      "email": "joaquim@hotmail.com.br",
      "is_admin": false
    }
  ]
}
```

<br>

### <b> Atualização </b>

<i> PATCH /api/courses/\<id\>/ </i>

Esse endpoint servirá para fazermos atualizações dos curso,

A aplicação permite a atualização parcial sem perca de dados existentes:

```json
{
  "name": "Node", // Campo opcional
  "demo_time": "8:00", // Campo opcional
  "link_repo": "https://gitlab.com/turma_node/" // Campo opcional
}
```

Exemplo de resposta dessa rota:

```json
{
  "uuid": "7c32c787-83c3-4994-8f45-b6ef113cde5e",
  "name": "Node",
  "demo_time": "08:00:00",
  "created_at": "2022-02-15T19:12:44.914032Z",
  "link_repo": "https://gitlab.com/turma_node/",
  "instructor": null,
  "students": []
}
```

<br>

### <b> Cadastro de instrutor no curso </b>

<i> PUT /api/courses/<id>/registrations/instructor/ </i>

Esse endpoint será responsável pela inserção de um Instrutor no curso.

Essa rota sempre atualizará o instrutor no curso:

<code>
    // REQUEST
</code><br>
<code>
    // Header -> Authorization: Token 'token-do-instrutor'
</code><br><br>

```json
{
  "instructor_id": "61039ae4-7016-48d3-b90e-95a78b39e427"
}
```

Resposta:

```json
{
  "uuid": "87556b7e-ac9a-4a8d-9b9f-c2ea7e956a94",
  "name": "Django",
  "demo_time": "09:00:00",
  "created_at": "2022-02-15T19:08:15.927682Z",
  "link_repo": "https://gitlab.com/turma_django/",
  "instructor": {
    "uuid": "61039ae4-7016-48d3-b90e-95a78b39e427",
    "first_name": "Maria",
    "last_name": "Joaquina",
    "email": "maria@bol.com.br",
    "is_admin": true
  },
  "students": [
    {
      "uuid": "5fef85a3-61e3-4e03-b6bd-ee544cd9bcdd",
      "first_name": "Joaquim",
      "last_name": "Ferreira",
      "email": "joaquim@hotmail.com.br",
      "is_admin": false
    }
  ]
}
```

<br>

### <b> Cadastro de estudantes no curso </b>

<i> PUT /api/courses/<id>/registrations/students/ </i>

Esse endpoint será responsável pela matrícula de estudantes no curso.

A lista de estudantes matriculados no curso sempre será atualizada, conforme as informações são enviadas:

<code>
    // REQUEST
</code><br>
<code>
    // Header -> Authorization: Token 'token-do-instrutor'
</code><br><br>

```json
{
  "students_id": [
    "5fef85a3-61e3-4e03-b6bd-ee544cd9bcdd",
    "5f2747f3-8899-49d9-b7f9-4ade850db837",
    "f09c6c88-6cd3-4ed9-b818-432e9f8df11c"
  ]
}
```

Resposta:

```json
{
  "uuid": "87556b7e-ac9a-4a8d-9b9f-c2ea7e956a94",
  "name": "Django",
  "demo_time": "09:00:00",
  "created_at": "2022-02-15T19:08:15.927682Z",
  "link_repo": "https://gitlab.com/turma_django/",
  "instructor": {
    "uuid": "61039ae4-7016-48d3-b90e-95a78b39e427",
    "first_name": "Maria",
    "last_name": "Joaquina",
    "email": "maria@bol.com.br",
    "is_admin": true
  },
  "students": [
    {
      "uuid": "5fef85a3-61e3-4e03-b6bd-ee544cd9bcdd",
      "first_name": "Joaquim",
      "last_name": "Ferreira",
      "email": "joaquim@hotmail.com.br",
      "is_admin": false
    },
    {
      "uuid": "5f2747f3-8899-49d9-b7f9-4ade850db837",
      "first_name": "Marcelo",
      "last_name": "Soares",
      "email": "marcelo@bol.com.br",
      "is_admin": false
    },
    {
      "uuid": "f09c6c88-6cd3-4ed9-b818-432e9f8df11c",
      "first_name": "Pedro",
      "last_name": "Martins",
      "email": "pedro@bol.com.br",
      "is_admin": false
    }
  ]
}
```

<br>

### <b> Deleção de Cursos </b>

<i> PUT DELETE /api/courses/<course_id>/ </i>

Este endpoint somente poderá ser acessado por um instrutor e ele realizará a exclusão do curso no sistema.

<code>
    // REQUEST
</code><br>
<code>
    // Header -> Authorization: Token 'token-do-instrutor'
</code><br><br>

Resposta:

```json
// RESPONSE STATUS -> HTTP 204 NO CONTENT
```

<br>
