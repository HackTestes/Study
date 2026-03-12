import os
import pathlib
import json
import re

# Validation errors
class ValidationError_MissingField(Exception):
    def __init__(self, message, missing_field, file_path, card):
        super().__init__(f"{message}")
        self.missing_field = missing_field
        self.file_path = file_path
        self.card = card

class ValidationError_IncorrectType(Exception):
    def __init__(self, message, field, offending_value, file_path, card):
        super().__init__(message)
        self.field = field
        self.offending_value = offending_value
        self.file_path = file_path
        self.card = card

class ValidationError_DuplicateId(Exception):
    def __init__(self, message, duplicated_id, file_paths, cards):
        super().__init__(message)
        self.duplicated_id = duplicated_id
        self.file_paths = file_paths
        self.cards = cards

class ValidationError_InvalidTemplate(Exception):
    def __init__(self, message, invalid_template, file_path, card):
        super().__init__(f"{message}")
        self.invalid_template = invalid_template
        self.file_path = file_path
        self.card = card

class ValidationError_InvalidLanguage(Exception):
    def __init__(self, message, invalid_language, file_path, card):
        super().__init__(f"{message}")
        self.invalid_language = invalid_language
        self.file_path = file_path
        self.card = card

def is_db_valid(json_db):

    # Rename the schema to make it easier to use
    schema = json_db["schema"]

    # Validate the schema
    # langauges
    if "languages" not in schema:
        raise ValidationError_MissingField("The schema lacks the languages field", "languages", schema["path"], None)

    if type(schema["languages"]) is not list:
        raise ValidationError_IncorrectType("The languages field isn't a list", "languages", str(schema["languages"]), schema["path"], None)

    for lang in schema["languages"]:
        if type(lang) is not str:
            raise ValidationError_IncorrectType("Some languages aren't strings", "languages", str(lang), schema["path"], None)

    # Templates
    if "templates" not in schema:
        raise ValidationError_MissingField("The schema lacks the templates field", "templates", schema["path"], None)

    if type(schema["templates"]) is not dict:
        raise ValidationError_IncorrectType("The templates field isn't a dict", "templates", str(schema["templates"]), schema["path"], None)

    for template_key, template_value in schema["templates"].items():
        if type(template_value) is not dict:
            raise ValidationError_IncorrectType("Some templates aren't dicts", template_key, str(template_value), schema["path"], None)

        if "fields" not in template_value:
            raise ValidationError_MissingField(f"The template ({template_key}) lacks the 'fields' field", template_key, schema["path"], None)

        if type(template_value["fields"]) is not list:
            raise ValidationError_IncorrectType(f"The template ({template_key}) 'fields' isn't a list", template_key, str(template_value["fields"]), schema["path"], None)

        for field in template_value["fields"]:
            if type(field) is not str:
                raise ValidationError_IncorrectType(f"Some template ({template_key}) fields aren't Strings", template_key, str(field), schema["path"], None)


    # {id_key: {"entry_index": entry_index, "card_index", card_index}} (outdated, just kept for future reference)
    # Store all unique IDs for duplication detection
    # {id_key: {"entry": entry, "card", card}} -> this should be referencing the same object in RAM as the original dict
    ids = {}

    # Loop over every entry
    for entry_index, json_entry in enumerate(json_db["entries"]):

        # Validate if entry fields are correct
        if "subject" not in json_entry["data"]:
            raise ValidationError_MissingField("The entry lacks a subject field", "subject", json_entry["path"], None)

        if type(json_entry["data"]["subject"]) is not str:
            raise ValidationError_IncorrectType("The subject field isn't a String", "subject", str(json_entry["data"]["subject"]), json_entry["path"], None)


        if "general_references" not in json_entry["data"]:
            raise ValidationError_MissingField("The card lacks the general_references field", "general_references", json_entry["path"], None)

        if type(json_entry["data"]["general_references"]) is not list:
            raise ValidationError_IncorrectType("The general_references field isn't a list", "general_references", str(json_entry["data"]["general_references"]), json_entry["path"], None)

        for reference in json_entry["data"]["general_references"]:
            if type(reference) is not str:
                raise ValidationError_IncorrectType("Some references aren't strings", "general_references", str(reference), json_entry["path"], None)

        # Now do it for each card
        for card_index, card in enumerate(json_entry["data"]["cards"]):

            # Validate if the normal entries exist and have the correct type
            if "deck" not in card:
                raise ValidationError_MissingField("The card lacks a Deck field", "deck", json_entry["path"], card)

            if type(card["deck"]) is not str:
                raise ValidationError_IncorrectType("The Deck field isn't a String", "deck", str(card["deck"]), json_entry["path"], card)


            if "id" not in card:
                raise ValidationError_MissingField("The card lacks a id field", "id", json_entry["path"], card)

            if type(card["id"]) is not str:
                raise ValidationError_IncorrectType("The id field isn't a String", "id", str(card["id"]), json_entry["path"], card)


            if "template_type" not in card:
                raise ValidationError_MissingField("The card lacks a template field", "template_type", json_entry["path"], card)

            if type(card["template_type"]) is not str:
                raise ValidationError_IncorrectType("The template field isn't a String", "template_type", str(card["template_type"]), json_entry["path"], card)


            if "language" not in card:
                raise ValidationError_MissingField("The card lacks a language field", "language", json_entry["path"], card)

            if type(card["language"]) is not str:
                raise ValidationError_IncorrectType("The language field isn't a String", "language", str(card["language"]), json_entry["path"], card)


            if "tags" not in card:
                raise ValidationError_MissingField("The card lacks the tags field", "tags", json_entry["path"], card)

            if type(card["tags"]) is not list:
                raise ValidationError_IncorrectType("The tags field isn't a list", "tags", str(card["tags"]), json_entry["path"], card)

            for tag in card["tags"]:
                if type(tag) is not str:
                    raise ValidationError_IncorrectType("Some tags aren't strings", "tags", str(tag), json_entry["path"], card)


            if "extended_description" not in card:
                raise ValidationError_MissingField("The card lacks an extended description field", "extended_description", json_entry["path"], card)

            if type(card["extended_description"]) is not str:
                raise ValidationError_IncorrectType("The extended description field isn't a String", "extended_description", str(card["extended_description"]), json_entry["path"], card)


            if "references" not in card:
                raise ValidationError_MissingField("The card lacks the references field", "references", json_entry["path"], card)

            if type(card["references"]) is not list:
                raise ValidationError_IncorrectType("The references field isn't a list", "references", str(card["references"]), json_entry["path"], card)

            for reference in card["references"]:
                if type(reference) is not str:
                    raise ValidationError_IncorrectType("Some references aren't strings", "references", str(reference), json_entry["path"], card)


            # Validate if IDs are unique
            # Does the ID already exist?
            card_id = card["id"]
            if card["id"] in ids:

                # We have a duplicate!
                # Use the id storage to get all the details about the other card with the same ID
                #first_occurrence_entry = json_db["entries"][ids[card_id]["entry_index"]] (outdated, just kept for future reference)
                first_occurrence_entry = ids[card_id]["entry"]
                first_occurrence_path = first_occurrence_entry["path"]

                #first_occurrence_card = first_occurrence_entry["data"]["cards"][ids[card_id]["card_index"]] (outdated, just kept for future reference)
                first_occurrence_card = ids[card_id]["card"]

                raise ValidationError_DuplicateId("Error, you have duplicated IDs. They must be unique", card_id, [first_occurrence_path, json_entry["path"]], [first_occurrence_card, card])
            else:
                # All good, just add it to the IDs storage
                #ids[card["id"]] = {"entry_index": entry_index, "card_index": card_index}
                ids[card["id"]] = {"entry": json_entry, "card": card}

            # Validate if the template type exists in the schema
            if card["template_type"] not in schema["templates"]:
                raise ValidationError_InvalidTemplate("Invalid template type", card["template_type"], json_entry["path"], card)

            # Validate if the template type has all the fields
            # Query the corresponding template fields in the schema and check if they exist in the card
            for field in schema["templates"][card["template_type"]]["fields"]:

                if field not in card:
                    raise ValidationError_MissingField(f"The card lacks the template ({card["template_type"]}) specific field", field, json_entry["path"], card)

                if type(card[field]) is not str:
                    raise ValidationError_IncorrectType(f"The template ({card["template_type"]}) specific field isn't a string", field, str(card[field]), json_entry["path"], card)

            # Validate if the language is available according to the schema
            if card["language"] not in schema["languages"]:
                raise ValidationError_InvalidLanguage("Invalid language", card["language"], json_entry["path"], card)

    return True

# Parses all the the JSON files in the data folder
# This allows me to just update the JSON files, since the code will adapt itself automatically
def read_json_data(data_folder="./data"):

    parsed_json_data = {"schema": {}, "entries": [], "entries_idx_path": {}}

    # Add the schema information
    print(f"Parsing schema information at: {data_folder}/schema.json")
    parsed_json_data["schema"] = json.loads(open(f"{data_folder}/schema.json", encoding="UTF-8").read())
    parsed_json_data["schema"]["path"] = f"{data_folder}/schema.json" # Attach path info for better error messages

    for (root,dirs,files) in os.walk(data_folder, topdown=True):

        for file in files:
            if pathlib.Path(file).suffix == ".json" and file != "schema.json":

                # Parse and save the file

                # Append the full path so we can save it and use it for open
                # Also make the slashes style consistent (the OS.walk mixes them on Windows). The open function works regardless
                path = f"{root}/{file}".replace("\\", "/")

                # Make sure we report what we are doing to the user
                print(f"Parsing JSON file: {path}")
                parsed_json_data["entries"].append( {"data": json.loads(open(path, encoding="UTF-8").read()), "path": path} )
                parsed_json_data["entries_idx_path"][path] = parsed_json_data["entries"][-1]

    return parsed_json_data


# Takes a text string and transform some special characters into HTML equivalents
# This is useful for CSV files that Anki can import, especially since some chars (like the "line-break") con completely break the CSV file
def TextToHTML(input_text):

    transformed_text = input_text
    transformed_text = transformed_text.replace("\n", "<br/>")
    transformed_text = re.sub(r"\*\*(.*?)\*\*", r"<b>\1<b/>", transformed_text)
    transformed_text = re.sub(r"\*(.*?)\*", r"<i>\1<i/>", transformed_text)

    return transformed_text

# Takes all the JSON files and formatts it as a CSV file compatible with Anki (please refer to: https://docs.ankiweb.net/importing/text-files.html)
# Useful for importing all the data into Anki at once
def JsonToAnkiCsv(json_db, separator="|||", dry_run=False):

    # Insert header information
    csv_str = ""
    csv_str += f"#separator:{separator}\n"
    csv_str += f"#deck column:1\n"
    csv_str += f"#guid column:2\n"
    csv_str += f"#notetype column:3\n"
    csv_str += f"#tags column:4\n"
    csv_str += f"#html:true\n"

    # Iterate over every entry and add it to the csv file
    # I expect the input to be an array with each entry being the parsed JSON file
    for json_file in json_db["entries"]:
        for card in json_file["data"]["cards"]:

            if card["template_type"] == "Frente-Verso_pt-BR" or card["template_type"] == "Front-Back_en-US":
                csv_str += card["deck"] + separator
                csv_str += card["id"] + separator
                csv_str += card["template_type"] + separator
                csv_str += " ".join(card["tags"]) + separator
                csv_str += TextToHTML(card["front"]) + separator
                csv_str += TextToHTML(card["back"]) + "\n"

    return csv_str


# If the file has entries with different languages, put each language in a separate linear array
def split_by_language():
    pass

# Takes each JSON file and creates a TXT out of it
# The goal here is to create a text file that can be consumed individually by a Text-to-Speech (TTS) program
def JsonToTxt(json_data, dry_run=False):
    pass