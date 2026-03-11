import helpers
import json
from pprint import pprint

# Global configuration
ERROR_HEADER = "\n--------------------ERROR--------------------"
json_db_path = "./data"
json_db = helpers.read_json_data()

# Execute the validation and report the errors in detail back to the user
try:
    helpers.is_db_valid(json_db)

except helpers.ValidationError_MissingField as e:
    print(ERROR_HEADER)
    print(f"Message: {e} \nMissing field: {e.missing_field} \nFile path: {e.file_path} \nCard: {json.dumps(e.card, indent='\t', ensure_ascii=False)}\n")
    exit()

except helpers.ValidationError_IncorrectType as e:
    print(ERROR_HEADER)
    print(f"Message: {e} \nErrored field: {e.field} \nOffending value: {e.offending_value} \nFile path: {e.file_path} \nCard: {json.dumps(e.card, indent='\t', ensure_ascii=False)}\n")
    exit()

except helpers.ValidationError_DuplicateId as e:
    print(ERROR_HEADER)
    print(f"Message: {e} \nDuplicated ID: {e.duplicated_id} \nFile paths: {e.file_paths} \nCards: {json.dumps(e.cards, indent='\t', ensure_ascii=False)}\n")
    exit()

except helpers.ValidationError_InvalidTemplate as e:
    print(ERROR_HEADER)
    print(f"Message: {e} \nInvalid template: {e.invalid_template} \nFile path: {e.file_path} \nCard: {json.dumps(e.card, indent='\t', ensure_ascii=False)}\n")
    exit()

except helpers.ValidationError_InvalidLanguage as e:
    print(ERROR_HEADER)
    print(f"Message: {e} \nInvalid language: {e.invalid_language} \nFile path: {e.file_path} \nCard: {json.dumps(e.card, indent='\t', ensure_ascii=False)}\n")
    exit()

# Other errors will raise just fine may causes "crashes" with the stack trace output

# Now perform all of the file operations

# Generate the CSV for Anki
anki_csv = helpers.JsonToAnkiCsv(json_db)
print(anki_csv)

# Generate the summaries
# One for audio generation

# One for regular viewing (I expect a Markdown viewer to be used)


#file = json.loads(open("./data/Portugues/portugues.json", encoding="UTF-8").read())
#print(file.general_references)
#print(json.dumps(file, indent=4, ensure_ascii=False))

