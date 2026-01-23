import pandas as pd
import shutil
from pathlib import Path

GROUP_ID = 0
PATH_RAW = Path("./data")
PATH_PROCESSED = Path("./data/group_data")

PATH_IMGS = PATH_PROCESSED/"imgs/"
PATH_MASKS = PATH_PROCESSED/"masks/"

PATH_PROCESSED.mkdir(parents=True, exist_ok=True)
PATH_IMGS.mkdir(parents=True, exist_ok=True)
PATH_MASKS.mkdir(parents=True, exist_ok=True)

df_labels = pd.read_csv(f"{PATH_RAW}/metadata_with_group.csv")
df_labels_group = df_labels[df_labels["group_id"]==GROUP_ID]

for img_path in df_labels_group["img_id"]:
    shutil.copyfile(f"{PATH_RAW}/imgs/{img_path}", f"{PATH_IMGS}/{img_path}")
    shutil.copyfile(f"{PATH_RAW}/masks/{img_path.replace('.png','_mask.png')}", f"{PATH_MASKS}/{img_path.replace('.png','_mask.png')}")

df_labels_group.to_csv(f"{PATH_PROCESSED}/metadata.csv")