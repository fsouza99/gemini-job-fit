## Gemini Vitae

O portal Gupy é um dos softwares mais utilizados por empresas para organização de ofertas de vagas de emprego no Brasil, unificando muitas etapas típicas do processo de contratação.

Um dos recursos que o site dá aos empregadores é a possibilidade de ordenar os currículos, enviados sob rígido formato, por grau de compatibilidade com a vaga, estimado segundo uma inteligência artificial.

Apesar de não coincidir necessariamente com as análises da IA do portal, as respostas de um modelo como o Gemini podem incluir valiosos *insights* a um candidato, ajudando-o em sua busca por um novo emprego.

### Uso

Crie um arquivo *settings.json* na pasta raiz, seguindo o modelo de exemplo:

```json
{
	"cv_file": "path\\to\\curriculum.md",
	"model": "gemini-2.5-flash",
	"output_dir": "dir\\where\\output\\must\\be\\saved"
}
```

Há um modelo de currículo em *files* que pode servir de referência para o que será indicado no arquivo de configuração, em um formato semelhante ao da Gupy (o que não é obrigatório).

Para solicitar ao Gemini que retorne sua análise de compatibilidade entre o currículo e uma vaga no portal, fazemos:

```
py main.py <url_vaga>
```

Também é possível, com a opção *-p*, apenas gerar o *prompt* e sair, permitindo que o usuário o utilize em qualquer IA de sua preferência.

```
py main.py <url_vaga> -p
```

*Dica: O [StackEdit](https://stackedit.io/app#) pode ser uma boa opção para ler um texto Markdown com as formatações à mostra.*

### Créditos

* [Portal Gupy](https://portal.gupy.io/?int_ref=navbar-candidatos)
* [Gemini](https://deepmind.google/technologies/gemini/#introduction)
* [Beautiful Soup](https://pypi.org/project/beautifulsoup4/)