# haml-flask

Use HAML on Flask project and rendering Jinja2 example.

# HAML

[haml.info](haml.info)

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

