## Instalação com venv.

Instale o pipenv:

```
pip install pipenv

```
ou

```
pip3 install pipenv

```

Após clonar o repositório, dentro do mesmo execute os comandos:

```

virtualenv <nome_da_venv>
pipenv install
source <nome_da_venv>/bin/activate

```

## Execução com venv.

Obs: Após o comando source <nome_da_venv>/bin/activate
Dentro do diretório basta executar: 

```
python bot.py
```

## Instalação sem venv.

Essa API é testada com Python 2.6, Python 2.7, Python 3.4, Pypy e Pypy 3. Há duas maneiras de instalar a biblioteca:

-   Instalação usando pip (gerenciador de pacotes Python) *:

```
$ pip install pyTelegramBotAPI

```

-   Instalação a partir da fonte:

```
$ git clone https://github.com/eternnoir/pyTelegramBotAPI.git
$ cd pyTelegramBotAPI
$ python setup.py install

```

Geralmente, é recomendável usar a primeira opção.

Obs: Não esqueça de atualizá-la regularmente chamando  `pip install pytelegrambotapi --upgrade`

## Execução sem venv.

Dentro do diretório basta executar: 

```

python bot.py

```