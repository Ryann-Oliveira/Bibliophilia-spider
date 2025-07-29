# 🕸️ Bibliophilia, uma spider simples com Scrapy

Este repositório contém uma spider simples desenvolvida com [Scrapy](https://scrapy.org/), com o objetivo de praticar meus conhecimentos em coleta de dados web — mais comumente conhecida como **Web Scraping** — bem como com o de compartilhar um pouco daquilo que aprendi. 

## 🎯 Objetivo

O projeto foi criado como parte do meu aprendizado em ciência de dados, com foco em:

- Entender o funcionamento de spiders e crawlers
- Aprender a estruturar projetos com Scrapy
- Extrair dados de forma organizada
- Salvar os dados em formatos úteis (JSON, CSV, etc.)

## 🛠️ Tecnologias Utilizadas

- **Python 3**  
- **Scrapy**

## 📦 Estrutura (somente partes principais)
```
retalhos/
├── retalhos/                 # Pasta principal do Scrapy
│   ├── spiders/
│   │   └── bibliphilia.py    # Spider principal
│   ├── items.py              
│   ├── middlewares.py
|   ├── pipelines.py
|   ├── results.json          # Amostras de resultados
│   └── settings.py           # Configurações do Scrapy
├── requirements.txt          # Lista de dependências
└── README.md                 # Documentação do projeto
```

## Disclaimer
Os dados foram coletados a partir de um website de conteúdo **explicitamente** público e voltado **unicamente** à pratica de web scraping. **Nenhum** dado foi violado.
Os preços e disponibilidades em estoque de cada um dos livros são fictícios, e seus títulos e sinopses são informações de conhecimento público, então **os direitos autorais permanecem inviolados**.
> Todos os direitos de propriedade legal sobre os livros mencionados são de seus respectivos autores.
