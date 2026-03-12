import unittest
import helpers
import pprint
import copy

# Path to JSON schemas 
test_path = "./scripts/test_data"

# Use the helper function to read the JSONs for testing.
# This way, if there is an error in the reading function, all the tests will break
valid_db = helpers.read_json_data(test_path)

class TestMethods(unittest.TestCase):

    # Schema
    # languages
    def test_db_validation_error_missing_field_schema_languages(self):

        missing_field_db = copy.deepcopy(valid_db)
        missing_field_db["schema"].pop("languages")

        with self.assertRaises(helpers.ValidationError_MissingField) as e:
            result = helpers.is_db_valid(missing_field_db)

        self.assertEqual(e.exception.missing_field, "languages")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/schema.json")
        self.assertEqual(e.exception.card, None)

    def test_db_validation_error_incorrect_type_schema_languages(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["schema"]["languages"] = 1

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "languages")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/schema.json")
        self.assertEqual(e.exception.card, None)

    def test_db_validation_error_incorrect_type_items_schema_languages(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["schema"]["languages"].append(1)

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "languages")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/schema.json")
        self.assertEqual(e.exception.card, None)

    # templates
    def test_db_validation_error_missing_field_schema_templates(self):

        missing_field_db = copy.deepcopy(valid_db)
        missing_field_db["schema"].pop("templates")

        with self.assertRaises(helpers.ValidationError_MissingField) as e:
            result = helpers.is_db_valid(missing_field_db)

        self.assertEqual(e.exception.missing_field, "templates")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/schema.json")
        self.assertEqual(e.exception.card, None)

    def test_db_validation_error_incorrect_type_schema_templates(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["schema"]["templates"] = 1

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "templates")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/schema.json")
        self.assertEqual(e.exception.card, None)

    def test_db_validation_error_incorrect_type_items_schema_templates(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["schema"]["templates"]["errored_template"] = 1

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(str(e.exception), "Some templates aren't dicts")
        self.assertEqual(e.exception.field, "errored_template")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/schema.json")
        self.assertEqual(e.exception.card, None)

    def test_db_validation_error_missing_field_items_schema_templates_fields(self):

        missing_field_db = copy.deepcopy(valid_db)
        missing_field_db["schema"]["templates"]["errored_template"] = {}

        with self.assertRaises(helpers.ValidationError_MissingField) as e:
            result = helpers.is_db_valid(missing_field_db)

        self.assertEqual(str(e.exception), "The template (errored_template) lacks the 'fields' field")
        self.assertEqual(e.exception.missing_field, "errored_template")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/schema.json")
        self.assertEqual(e.exception.card, None)

    def test_db_validation_error_incorrect_type_items_schema_templates_fields(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["schema"]["templates"]["errored_template"] = {"fields": 1}

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(str(e.exception), "The template (errored_template) 'fields' isn't a list")
        self.assertEqual(e.exception.field, "errored_template")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/schema.json")
        self.assertEqual(e.exception.card, None)

    def test_db_validation_error_incorrect_type_items_schema_templates_each_field(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["schema"]["templates"]["errored_template"] = {"fields": ["A", "B", 1]}

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(str(e.exception), "Some template (errored_template) fields aren't Strings")
        self.assertEqual(e.exception.field, "errored_template")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/schema.json")
        self.assertEqual(e.exception.card, None)

    # Entry fields
    # subject
    def test_db_validation_error_missing_field_subject(self):

        missing_field_db = copy.deepcopy(valid_db)
        missing_field_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"].pop("subject")

        with self.assertRaises(helpers.ValidationError_MissingField) as e:
            result = helpers.is_db_valid(missing_field_db)

        self.assertEqual(e.exception.missing_field, "subject")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card, None)

    def test_db_validation_error_incorrect_type_subject(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["subject"] = 1

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "subject")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card, None)

    # general_references
    def test_db_validation_error_missing_field_general_references(self):

        missing_field_db = copy.deepcopy(valid_db)
        missing_field_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"].pop("general_references")

        with self.assertRaises(helpers.ValidationError_MissingField) as e:
            result = helpers.is_db_valid(missing_field_db)

        self.assertEqual(e.exception.missing_field, "general_references")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card, None)

    def test_db_validation_error_incorrect_type_general_references(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["general_references"] = 1

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "general_references")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card, None)

    def test_db_validation_error_incorrect_type_items_general_references(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["general_references"].append(1)

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "general_references")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card, None)

    # Card fields
    # deck
    def test_db_validation_error_missing_field_deck(self):

        missing_field_db = copy.deepcopy(valid_db)
        missing_field_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0].pop("deck")

        with self.assertRaises(helpers.ValidationError_MissingField) as e:
            result = helpers.is_db_valid(missing_field_db)

        self.assertEqual(e.exception.missing_field, "deck")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card, {
            "id": "Test_json",
            "template_type": "Frente-Verso_pt-BR",
            "language": "pt-BR",
            "tags": [],
            "front": "Front test",
            "back": "Back test",
            "extended_description": "",
            "references": []
        })

    def test_db_validation_error_incorrect_type_deck(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0]["deck"] = 1

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "deck")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card["deck"], 1)

    # id
    def test_db_validation_error_missing_field_id(self):

        missing_field_db = copy.deepcopy(valid_db)
        missing_field_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0].pop("id")

        with self.assertRaises(helpers.ValidationError_MissingField) as e:
            result = helpers.is_db_valid(missing_field_db)

        self.assertEqual(e.exception.missing_field, "id")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card, {
            "deck": "Test",
            "template_type": "Frente-Verso_pt-BR",
            "language": "pt-BR",
            "tags": [],
            "front": "Front test",
            "back": "Back test",
            "extended_description": "",
            "references": []
        })

    def test_db_validation_error_incorrect_type_id(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0]["id"] = 1

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "id")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card["id"], 1)

    # template_type
    def test_db_validation_error_missing_field_template_type(self):

        missing_field_db = copy.deepcopy(valid_db)
        missing_field_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0].pop("template_type")

        with self.assertRaises(helpers.ValidationError_MissingField) as e:
            result = helpers.is_db_valid(missing_field_db)

        self.assertEqual(e.exception.missing_field, "template_type")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card, {
            "deck": "Test",
            "id": "Test_json",
            "language": "pt-BR",
            "tags": [],
            "front": "Front test",
            "back": "Back test",
            "extended_description": "",
            "references": []
        })

    def test_db_validation_error_incorrect_type_template_type(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0]["template_type"] = 1

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "template_type")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card["template_type"], 1)

    # language
    def test_db_validation_error_missing_field_language(self):

        missing_field_db = copy.deepcopy(valid_db)
        missing_field_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0].pop("language")

        with self.assertRaises(helpers.ValidationError_MissingField) as e:
            result = helpers.is_db_valid(missing_field_db)

        self.assertEqual(e.exception.missing_field, "language")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card, {
            "deck": "Test",
            "id": "Test_json",
            "template_type": "Frente-Verso_pt-BR",
            "tags": [],
            "front": "Front test",
            "back": "Back test",
            "extended_description": "",
            "references": []
        })

    def test_db_validation_error_incorrect_type_language(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0]["language"] = 1

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "language")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card["language"], 1)

    # tags
    def test_db_validation_error_missing_field_tags(self):

        missing_field_db = copy.deepcopy(valid_db)
        missing_field_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0].pop("tags")

        with self.assertRaises(helpers.ValidationError_MissingField) as e:
            result = helpers.is_db_valid(missing_field_db)

        self.assertEqual(e.exception.missing_field, "tags")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card, {
            "deck": "Test",
            "id": "Test_json",
            "template_type": "Frente-Verso_pt-BR",
            "language": "pt-BR",
            "front": "Front test",
            "back": "Back test",
            "extended_description": "",
            "references": []
        })

    def test_db_validation_error_incorrect_type_tags(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0]["tags"] = 1

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "tags")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card["tags"], 1)

    def test_db_validation_error_incorrect_type_items_tags(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0]["tags"].append(1)

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "tags")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card["tags"][0], 1)

    # extended_description
    def test_db_validation_error_missing_field_extended_description(self):

        missing_field_db = copy.deepcopy(valid_db)
        missing_field_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0].pop("extended_description")

        with self.assertRaises(helpers.ValidationError_MissingField) as e:
            result = helpers.is_db_valid(missing_field_db)

        self.assertEqual(e.exception.missing_field, "extended_description")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card, {
            "deck": "Test",
            "id": "Test_json",
            "template_type": "Frente-Verso_pt-BR",
            "language": "pt-BR",
            "tags": [],
            "front": "Front test",
            "back": "Back test",
            "references": []
        })

    def test_db_validation_error_incorrect_type_extended_description(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0]["extended_description"] = 1

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "extended_description")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card["extended_description"], 1)

    # references
    def test_db_validation_error_missing_field_references(self):

        missing_field_db = copy.deepcopy(valid_db)
        missing_field_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0].pop("references")

        with self.assertRaises(helpers.ValidationError_MissingField) as e:
            result = helpers.is_db_valid(missing_field_db)

        self.assertEqual(e.exception.missing_field, "references")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card, {
            "deck": "Test",
            "id": "Test_json",
            "template_type": "Frente-Verso_pt-BR",
            "language": "pt-BR",
            "tags": [],
            "front": "Front test",
            "back": "Back test",
            "extended_description": "",
        })

    def test_db_validation_error_incorrect_type_references(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0]["references"] = 1

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "references")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card["references"], 1)

    def test_db_validation_error_incorrect_type_items_references(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][0]["references"].append(1)

        with self.assertRaises(helpers.ValidationError_IncorrectType) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.field, "references")
        self.assertEqual(e.exception.offending_value, "1")
        self.assertEqual(e.exception.file_path, "./scripts/test_data/test.json")
        self.assertEqual(e.exception.card["references"][0], 1)

    def test_db_validation_error_duplicate_id(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][1]["id"] = "Test_json"

        with self.assertRaises(helpers.ValidationError_DuplicateId) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.duplicated_id, "Test_json")
        self.assertEqual(e.exception.file_paths, ["./scripts/test_data/test.json", "./scripts/test_data/test.json"])
        self.assertEqual(e.exception.cards[0]["front"], "Front test")
        self.assertEqual(e.exception.cards[0]["back"], "Back test")
        self.assertEqual(e.exception.cards[1]["front"], "Front test 002")
        self.assertEqual(e.exception.cards[1]["back"], "Back test 002")

    def test_db_validation_error_duplicate_id_differnt_files(self):

        incorrect_type_db = copy.deepcopy(valid_db)
        incorrect_type_db["entries_idx_path"]["./scripts/test_data/test.json"]["data"]["cards"][1]["id"] = "Test_json"

        with self.assertRaises(helpers.ValidationError_DuplicateId) as e:
            result = helpers.is_db_valid(incorrect_type_db)

        self.assertEqual(e.exception.duplicated_id, "Test_json")
        self.assertEqual(e.exception.file_paths, ["./scripts/test_data/test.json", "./scripts/test_data/test.json"])
        self.assertEqual(e.exception.cards[0]["front"], "Front test")
        self.assertEqual(e.exception.cards[0]["back"], "Back test")
        self.assertEqual(e.exception.cards[1]["front"], "Front test 002")
        self.assertEqual(e.exception.cards[1]["back"], "Back test 002")

    def test_TextToHTML_regular_case(self):
        result = helpers.TextToHTML("A **simple** *text* for testing\n")
        self.assertEqual("A <b>simple<b/> <i>text<i/> for testing<br/>", result)

    def test_TextToHTML_regular_case_multiple(self):
        result = helpers.TextToHTML("A **simple** *text* for testing\n But I **like** to make things difficult *for me*!\n\n")
        self.assertEqual("A <b>simple<b/> <i>text<i/> for testing<br/> But I <b>like<b/> to make things difficult <i>for me<i/>!<br/><br/>", result)


if __name__ == '__main__':
    unittest.main()