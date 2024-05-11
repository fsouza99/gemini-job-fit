## Gemini Vitae

### Intro

O portal Gupy é um dos softwares mais utilizados por empresas para organização de ofertas de vagas de emprego no Brasil, unificando muitas etapas típicas do processo de contratação.

Um dos recursos que o site dá aos empregadores é a possibilidade de ordenar os currículos, enviados sob rígido formato, por grau de compatibilidade com a vaga, estimado segundo uma inteligência artificial.

Apesar de não coincidir necessariamente com as análises da IA do portal, as respostas de um modelo como o Gemini podem incluir valiosos *insights* a um candidato, ajudando-o em sua busca por um novo emprego.

### Uso

Inicialmente, o *script* em *main.py* cria as dependências necessárias para o esquema de consulta:

- O currículo deve estar escrito em *files/curriculum.md*, aconselhavelmente fazendo uso da sintaxe *Markdown* para aprimorar o entendimento do Gemini sobre a entrada (veja o exemplo em *files*).
- O *prompt* será construído conforme o *template* em *files/prompt_model.md*.
- Para consultar o Gemini, é necessário fornecer uma chave de acesso no arquivo *files/apikey*.

Com esses dados devidamente informados, execute o *main.py* novamente para solicitar ao Gemini que retorne sua análise de compatibilidade entre o currículo e uma vaga no portal Gupy, indicada por uma URL passada como parâmetro na execução:

	py main.py <url>

Como resultado, o programa registra em arquivos o *prompt* enviado e a resposta do modelo.

*Dica: O [StackEdit](https://stackedit.io/app#) pode ser uma boa opção para ler um texto Markdown com as formatações à mostra.*

### Créditos

* [Portal Gupy](https://portal.gupy.io/?int_ref=navbar-candidatos)
* [Gemini](https://deepmind.google/technologies/gemini/#introduction)
* [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)