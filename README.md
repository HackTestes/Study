# Resumos formatados para a inserção no Anki

Meu objetivo é formatar todos os catões de um Deck em um único arquivo de texto estruturado. Dessa forma, eu posso versionar os Decks e salvar em diferentes formatos (além de ser bem mais simples a adição se comparado à interface do Anki).

Logo, eu vou ter uma base unificada capaz de criar flash-cards e resumos em texto corrido de forma automatizada.

## Formato

Eu optei pelo json por ser legível por humanos e por possuir bibliotecas padrão no python (ou JS no Browser caso eu queira migrar).

Ele vai ser separado em duas partes principais: o "esquema" e os dados em si. O arquivo de "esquema" define quais valores vão ser válidos em alguns dos campos (línguas disponíveis, tipos de cartão...). A parte dos dados vai representar os cartões em si com cada assunto possuindo um arquivo próprio.

O arquivo de esquema vai ser útil para validar erros nos cartões de forma automática.

**schema.json**
```json
{
    "languages": ["en-US", "pt-BR"],
    "templates": {
        "Frente-Verso_pt-BR": {"fields": ["front", "back"]},
        "Front-Back_en-US": {"fields": ["front", "back"]}
    }
}
```

**subject.json**
```json
{
    "subject": "subject",
    "general_references": ["https://aReferenceValidForAllCards.com"],
    "cards": [

        {
            "deck": "Deck Name::Sub Deck",
            "id": "test_card_pt_BR",
            "template_type": "Frente-Verso_pt-BR",
            "language": "pt-BR",
            "tags": ["tag"],
            "front": "Template specific field reserved usually for questions",
            "back": "Template specific field reserved usually for answers",
            "extended_description": "Extra information for the card that may not be included in the anki card, but might be useful in a summary",
            "references": ["https://something.com"]
        },

        {
            "deck": "Deck Name::Different Sub Deck",
            "id": "test_card_en_US",
            "template_type": "Front-Back_en-US",
            "language": "en-US",
            "tags": [],
            "front": "Template specific field reserved usually for questions",
            "back": "Template specific field reserved usually for answers",
            "extended_description": "Extra information for the card that may not be included in the anki card, but might be useful in a summary",
            "references": ["https://something.com", "https://anotherthing.com"]
        }
    ]
}
```

## Detalhes

* A ordem importa! Quando não for configurado nenhuma ordem (alfabética por exemplo), será usada a ordem de inserção.
* Pode ser usado HTML ou caracteres especiais ("\n", "\t", ...) nos campos de texto
* O campo "id" é utilizado para permitir ao Anki atualizar corretamente cada cartão, mantendo assim o histórico do aplicativo. O ideal é utilizar IDs **não numéricos** para evitar problemas em eventuais reordenações.

## Limitações

Esse projeto não suporta arquivos de imagem, o foco é apenas em informações de texto.

## Executando

**Gerando os arquivos de resumo e os cartões Anki**
```cmd
python ./scripts/main.py
```

* Saídas
    * `./out/Anki/anki_import.csv`: arquivos CSV para importar no Anki
    * `./out/Resumos/<ASSUNTO_GERAL>/*_<LÍNGUA>.txt`: arquivos em texto corrido (podem ser usados na geração de áudio)

## Referências do Anki

* https://docs.ankiweb.net/getting-started.html
* https://docs.ankiweb.net/importing/text-files.html