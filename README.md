## Gemini Vitae

### Intro

O portal Gupy é um dos mais softwares mais utilizados por empresas para organização de ofertas de vagas de emprego no Brasil, unificando muitas etapas típicas do processo de contratação.

Um dos recursos que o site dá aos empregadores é a possibilidade de ordenar os currículos, enviados sob rígido formato, por grau de compatibilidade com a vaga, estimado segundo uma inteligência artificial.

Apesar de não coincidir necessariamente com as análises da IA do portal, as respostas de um modelo como o Gemini podem incluir valiosas recomendações a um candidato.

### Uso

O script *main.py* solicita ao Gemini que retorne análise de compatibilidade entre um currículo e uma vaga no portal Gupy indicada por uma URL passada como parâmetro na execução:

	> py main.py <url>

O currículo deve estar escrito no arquivo em *files/curriculum.txt*, enquanto o *prompt* será construído conforme o *template* em *files/prompt_model*. Para consultar o Gemini, é necessário fornecer uma chave de acesso no arquivo *files/apikey*. Como resultado, o programa registra em arquivos a vaga, o *prompt* enviado e a resposta do modelo.

### Créditos

* [Portal Gupy](https://www.gupy.io)
* [Gemini](https://deepmind.google/technologies/gemini/#introduction)
* [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)



