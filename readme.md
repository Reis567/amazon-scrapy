# Projeto de Web Scraping na Amazon com Scrapy

Este é um projeto de exemplo que demonstra como usar a biblioteca Scrapy para realizar web scraping no site da Amazon em busca de informações sobre produtos.

## Requisitos

Antes de começar, certifique-se de ter os seguintes requisitos instalados em seu ambiente:

- Python 3.x
- Scrapy (instalado via `pip install scrapy`)

## Clonando o Repositório

Para começar a usar este projeto, siga os passos abaixo para clonar o repositório para o seu ambiente local:

1. Abra o terminal ou prompt de comando.
2. Navegue até o diretório onde deseja clonar o repositório.
3. Execute o seguinte comando para clonar o repositório:

```bash
git clone https://github.com/Reis567/amazon-scrapy.git
```

## Executando o Projeto

Depois de clonar o repositório, você pode executar o projeto da seguinte maneira:

1. Navegue até o diretório do projeto:

```bash
cd amazon-scrapy
```

2. Execute a aranha (spider) Scrapy usando o seguinte comando:

```bash
scrapy crawl amazon -o output.json
```

Este comando executará a spider chamada "amazon" e salvará os resultados em um arquivo JSON chamado "output.json".

3. Após a conclusão da execução, você pode encontrar os dados raspados no arquivo "output.json".

## Personalização

Você pode personalizar a aranha Scrapy para atender às suas necessidades, modificando o arquivo `spiders/amazon_spider.py`.

## Contribuindo

Se desejar contribuir para este projeto, sinta-se à vontade para fazer um fork, implementar melhorias e criar uma solicitação pull.
