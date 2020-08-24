<h1 align="center">Desafio 4Intelligence</h1>
<p align="center">Desafio proposto para vaga de estágio na empresa 4Intelligence, em Santa Rita do Sapucaí. O objetivo é obter a coleta de dados de eventos econômicos de forma automática, processar esses dados e gerar um arquivo .csv</p>

-----

<h3 align="center"> 
  <img src="https://github.com/jpgSouza/4i-python-challenge/blob/master/testing_gif.gif" >
</h3>

-----

<h3 align="center"> 
  <img src="https://github.com/jpgSouza/4i-python-challenge/blob/master/table.png" >
</h3>

-----

## Funcionalidades
A aplicação conta com algumas funcionalidades já implementadas:
- [X] Fazer o request da URL do site
- [X] Aplicar o filtro
- [X] Resgatar as informações das tabelas econômicas
- [X] Estruturar em um dataframe
- [X] Gerar o arquivo .csv

## Tecnologias
As seguintes ferramentas foram usadas na construção do projeto:
- [Beautifulsoup](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://requests.readthedocs.io/pt_BR/latest/)
- [Selenium](https://www.selenium.dev)
- [Pandas](https://pandas.pydata.org)

## Como utilizar? 

### Requisitos
 - Python 3
 - Firefox
 - Geckodriver

### Instalando as bibliotecas
 - Beautifulsoup: Extração de dados HTML
 ```
pip install beautifulsoup4
```

 - Requests: Requisição HTTP
 ```
pip install requests
```

 - Selenium: Automatização Web 
 ```
pip install selenium
```

 - Pandas: Manipulação dos datos em dataframe
 ```
pip install pandas
```

### Clone
- Clone este repositório na sua máquina local
```
git clone https://github.com/jpgSouza/4i-python-challenge.git
```

### Comando
- Dentro da pasta do projeto, na subpasta 'bin' rode o comando no seu terminal
```sh
python main.py
```

## License

[![License](https://img.shields.io/apm/l/vim-mode?color=blue)](http://badges.mit-license.org)

- **[MIT license](http://opensource.org/licenses/mit-license.php)**
- Copyright 2015 © <a href="http://fvcproductions.com" target="_blank">FVCproductions</a>.
