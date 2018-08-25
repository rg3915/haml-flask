# haml-flask

Use HAML on Flask project and rendering Jinja2 example.

# Haml

[haml.info](http://haml.info/)

![haml01.png](haml01.png)

> Haml (HTML abstraction markup language)

É baseado em um princípio básico: marcação deve ser bonita.

```
*.haml
%section.container
  %h1= post.title
  %h2= post.subtitle
  .content
    = post.content
```

Em 2010 Jesse Miller criou [github.com/jessemiller/HamlPy](https://github.com/jessemiller/HamlPy)

Logo depois, Appknox (XYSec Labs) criou [github.com/appknox/HamlPy3](https://github.com/appknox/HamlPy3)


## Instalação

```
python3 -m venv .venv
source .venv/bin/activate
pip install hamlpy3
```

### Como usar?

Convertendo .haml em .html

```
hamlpy example.haml templates/index.html
```

### Criando um projetinho

```
pip install flask
vim run.py
mkdir templates
```

Conteúdo de `run.py`:

```python
from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route('/')
def run():
    names = [
        {
            'id': 1,
            'name': 'Regis',
            'email': 'regis@email.com'
        },
        {
            'id': 2,
            'name': 'Abel',
            'email': 'abel@hotmail.com'
        },
        {
            'id': 3,
            'name': 'Fernanda',
            'email': 'fernanda@gmail.com'
        },
    ]
    return render_template("index.html", names=names)
```

#### Rodando

```
export FLASK_APP=run.py
flask run
```

### Voltemos ao Haml

Veja `example.haml`


Convertendo .haml em .html

```
hamlpy example.haml templates/index.html
```


#### Referências

https://github.com/appknox/HamlPy3

https://github.com/jessemiller/HamlPy/blob/master/reference.md

https://github.com/jessemiller/HamlPy/blob/master/reference.md#python

http://xahlee.info/comp/haml_basics_tutorial.html
