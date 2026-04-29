from text_utils import normalize_text
from data_utils import count_items
from file_utils import save_text, load_text
from json_utils import save_json, load_json
from ip_utils import get_public_ip
import random
import os
from ast_utils import get_imports_in_current_file

comp_name = os.environ.get("COMPUTERNAME", "")
user_name = os.environ.get("USERNAME", "")

text = "   Ну, ПОГоДи!   "
imports = get_imports_in_current_file()

print(imports)
clean_text = normalize_text(text)
imports_count = count_items(imports)

save_text("project_note.txt", clean_text)
loaded_text = load_text("project_note.txt")


config = {
    "user_login": f"{comp_name}/{user_name}",
    "temperature": random.randint(15, 100),
    "ip": get_public_ip(),
}

save_json("project_config.json", config)
loaded_config = load_json("project_config.json")

print("Очищенный текст:", clean_text)
print("Прочитанный текст из файла:", loaded_text)
print("Количество импортов в этом файле:", imports_count)
print("Загруженный JSON:", loaded_config)
