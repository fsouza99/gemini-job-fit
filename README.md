## Gemini Vitae

O portal Gupy é um dos softwares mais utilizados por empresas para organização de ofertas de vagas de emprego no Brasil, unificando muitas etapas típicas do processo de contratação.

Um dos recursos que o site dá aos empregadores é a possibilidade de ordenar os currículos, enviados sob rígido formato, por grau de compatibilidade com a vaga, estimado segundo uma inteligência artificial.

Apesar de não coincidir necessariamente com as análises da IA do portal, as respostas de um modelo como o Gemini podem incluir valiosos *insights* a um candidato, ajudando-o em sua busca por um novo emprego.

### Uso

Apenas execute o *script* principal para ver como utilizar o projeto. Será preciso criar um arquivo de configuração definindo um currículo para referência, um modelo do Gemini e um destino para as respostas, além de uma variável de ambiente com uma chave de acesso.

Após definir as configurações, bastará reexecutar o *script* com o endereço da vaga almejada.

```
py main.py <url_vaga>
```

*Dica: O [StackEdit](https://stackedit.io/app#) pode ser uma boa opção para ler um texto Markdown com as formatações à mostra.*

### Créditos

* [Portal Gupy](https://portal.gupy.io/?int_ref=navbar-candidatos)
* [Gemini](https://deepmind.google/technologies/gemini/#introduction)
* [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)