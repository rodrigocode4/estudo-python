# Instalação do VENV

## Intalação de ambiente local
```shell
    python3 -m venv <.venv>
```
> o argumento _.venv_ entre as tags pode ter outros nomes

## Habilitação do ambiente 
```shell
    source .venv/bin/activate
```
> para desativar, basta digitar `deactivate` no terminal

## Salvar depedências
```shell
    pip freeze > <requirements.txt>
```
>o arquimento _requirements.txt_ é uma convensão