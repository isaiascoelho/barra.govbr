# Barra.gov.br

[![Gitter](https://badges.gitter.im/Fale%20conosco.svg)](https://gitter.im/govbr/barra.govbr?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![bitHound Score](https://www.bithound.io/github/govbr/barra.govbr/badges/score.svg)](https://www.bithound.io/github/govbr/barra.govbr)

Barra dinâmica do governo brasileiro. Nesse projeto está incluído o código da barra e do rodapé de governo.


# Captura de tela da barra/rodapé

![Barra e rodapé da identidade do governo brasileiro.](doc/barra-printscreen.png)

# Exemplo de uso da barra/rodapé

O exemplo de como utilizar a barra no seu sítio está publicado em [Manual da Barra do Governo Brasileiro](http://barra.governoeletronico.gov.br/).
A página de testes está disponível em [Teste da Barra do Governo Brasileiro](http://barra.governoeletronico.gov.br/teste/).
Você pode contribuir e melhorar o exemplo no [Código do Manual da Barra do Governo Brasileiro](http://github.com/govbr/brasil.gov.manualbarra/).

# Sugerindo nova campanha/profile

Copie o profile 'vaso' e altere os arquivos referentes a campanha ou a barra e crie um pull request.

# Como gerar a barra/rodapé

## Mudando o profile

Execute o make com o parâmetro de PROFILE. Exemplo:

		PROFILE=outubrorosa make run 

## Dependências:

 * python2.7

 * io.js

 * sass

 * zlib

## Para criar o ambiente de desenvolvimento execute:

>		make venv 

## Para profiling é necessário além dos acima:

 * werkzeug

E execute o

>     make profile

## Usando vagrant:

O Vagrant vai criar o ambiente de desenvolvimento.

```
vagrant up
vagrant ssh
cd barra-govbr
```
 
## Geração da barra

Execute o comando:

>   PROFILE=outubrorosa make run 

O profile selecionado é o outubrorosa nesse exemplo

## Testes da barra

Execute o comando:

>    make teste

Para gerar um teste em XUNIT execute

>    make testReport

# Requisitos da Barra
----

1. A Barra deve ser adaptável a um desenho fluído e fixo
2. A Barra deve suportar diferentes opções de cor de fundo
3. A Barra deve suportar a inclusão dinâmica do nome da organização
4. A Barra deve funcionar nos navegadores: 

>Internet Explorer versão 8 ou superior

>Mozilla Firefox versão 24

>Google Chrome versão C30
	
>Safari versão S6

>Opera versão 12

>Navegadores de dispositivos móveis

5. A Barra deve degradar graciosamente (graceful degradation ou progressive enhancement) clientes que não possuam compatibilidade ou no qual o javascript esteja desligado.

6. A barra deve ser acessível.

7. A Barra deve conter tanto o rodapé como a barra.

# Considerações sobre a arquitetura
-----

1. A barra será hospedada em local centralizado e chamada de forma distribuída pelos portais institucionais;

2. A barra será incluída via javascript minificado.

3. O rodapé será incluído via javascript minificado.


