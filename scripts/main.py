import helpers

json_db = helpers.read_json_data()

try:
    print(helpers.is_db_valid(json_db))

except Exception as e:
    print(e)

anki_csv = helpers.JsonToCsv(json_db)

print(anki_csv)

#file = json.loads(open("./data/Portugues/portugues.json", encoding="UTF-8").read())
#print(file.general_references)
#print(json.dumps(file, indent=4, ensure_ascii=False))

