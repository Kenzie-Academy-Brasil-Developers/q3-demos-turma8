# Manual API

### Cadastrar usuário

\
**POST** http://{BASEURL}/validate

PAYLOAD (JSON)
```json
{
    "name": "<String>",
    "last_name": "<String>",
    "email": "<String>",
    "password": "<String>",
    "country": "<String>"
}
```

Se estiver no formato válido:

**POST** http://{BASEURL}/createUser

PAYLOAD (JSON)
```json
{
    "name": "<String>",
    "last_name": "<String>",
    "email": "<String>",
    "password": "<String>",
    "country": "<String>"
}
```

### Mostrar usuários
**POST** http://{BASEURL}/users?country_api=https://restcountries.com/v3.1/name/


### Editar usuário
**POST** http://{BASEURL}/update/users

PAYLOAD (JSON)
```json
{
    "email": "<String>",
    "<field>": "<value>"
}
```

### Deletar usuário
**POST** http://{BASEURL}/delete?email={email}