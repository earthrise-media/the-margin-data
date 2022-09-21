
import pandas as pd
from glob import glob
from tqdm import tqdm

military_key_words = ["army", "air force", "navy", "military", "weapons", "defense", "marines"]
federal_government_key_words = ["federal government"]

superfund_data = pd.read_csv("superfund_data.csv")

superfund_data["Military"] = 0
superfund_data["Federal Government"] = 0

# For each Superfund, look at it's associated report and tag as a "Military" or "Federal" site if
#   the correct keywords are present.
for superfund_index in tqdm(superfund_data.index):
    current_superfund = superfund_data.loc[superfund_index]
    current_superfund_name = current_superfund["Site Name"].replace("/", "-") # So we can match the name from the pull

    current_superfund_filename = glob(f"./npl_narrative_texts/{current_superfund_name}*")
    if len(current_superfund_filename) > 0:
        current_superfund_filename = glob(f"./npl_narrative_texts/{current_superfund_name}*")[0]
    else:
        continue

    text_file = open(current_superfund_filename, "r")
    text = text_file.read().lower()
    text_file.close()

    for key_word in military_key_words:
        if key_word in text:
            superfund_data.loc[superfund_index, "Military"] = 1
            break

    for key_word in federal_government_key_words:
        if key_word in text:
            superfund_data.loc[superfund_index, "Federal Government"] = 1
            break

superfund_data.to_csv("superfund_data_tagged.csv")
