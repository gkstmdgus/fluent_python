# """
# 딕셔너리와 집합
#
# 딕셔너리 (__builtins__.__dict__)
#
# 딕셔너리와 집합은 해시 테이블을 이용하므로 우선 해시 테이블이 어떤 것인지 알아야 한다.
# """
#
# import os
# import pathlib
# from pathlib import Path
# from datetime import datetime
# from typing import Dict, Any
#
#
# def get_extra_meta_data(file: Path) -> Dict[str, Any]:
#     stats = file.stat()
#     value = {
#         "owner": file.owner(),
#         "created_at": datetime.fromtimestamp(int(stats.st_birthtime)),
#         "updated_at": datetime.fromtimestamp(int(stats.st_mtime)),
#     }
#     if file.is_file():
#         value["size"] = {
#             "value": round(stats.st_size / 10**6, 2),
#             "unit": "MB"
#         }
#     return value
#
#
# def check_stl_file(file: Path) -> bool:
#     _, ext = os.path.splitext(file.name)
#     if ext == '.stl':
#         return True
#     return False
#
#
# pth = "/Users/han/Downloads"
# is_ext = os.path.exists(pth)
# result = []
# if is_ext:
#     entries = Path(pth)
#     print(f"location : {entries.absolute()}")
#     for data in entries.iterdir():
#         value = {
#             "name": data.name,
#             "type": "folder",
#         }
#         if data.is_file():
#             if not check_stl_file(data):
#                 continue
#             value["type"] = "file"
#         elif not data.is_dir():
#             print("!!")
#             continue
#         value.update(get_extra_meta_data(data))
#         result.append(value)
# else:
#     print(is_ext)
#
# print(f"total_count : {len(result)}")
# for data in result:
#     print(data)

import pandas as pd

# data = pd.read_parquet("/Users/han/Desktop/lc_to_coords_act.parquet")
# eval = pd.read_parquet("/Users/han/Desktop/eval.parquet")
#
# data["mass"] = 1.0
# data["freq1"] = 1.0
# data["freq2"] = 1.0
#
# print(data.columns)
# print(eval.columns)
#
#
#
# for _, da_val in data.iterrows():
#     filename = da_val["file_name"]
#     ev_val = eval.loc[eval["item"] == filename]
#     for i, value in ev_val.iterrows():
#         ev_val = value
#         break
#     mass = ev_val["mass"]
#     freq1 = ev_val["freq1"]
#     freq2 = ev_val["freq2"]
#     # print(f"mass : {mass}, freq1 : {freq1}, freq2 : {freq2}")
#     # ==
#     # print(f"eval_name : {eval}")
#     # ==
#     data.loc[data["file_name"] == filename, "mass"] = mass
#     data.loc[data["file_name"] == filename, "freq1"] = freq1
#     data.loc[data["file_name"] == filename, "freq2"] = freq2
# #
# #
# #
# for _, val in data.iterrows():
#     mass = val["mass"]
#     freq1 = val["freq1"]
#     freq2 = val["freq2"]
#     print(f"mass : {mass}, freq1 : {freq1}, freq2 : {freq2}")

# data.to_parquet("test.parquet")

df = pd.read_parquet("result.parquet")
print(df)
print(df.columns)

# new_df = df[:1010]
# new_df.to_parquet("result.parquet")
#
name_list = []

count = 0

for _, data in df.iterrows():
    name_list.append(data["file_name"])
    if data["mass"] == 1.0 or data["freq2"] == 1.0 or data["freq1"] == 1.0:
        count += 1

set_list = list(set(name_list))
# print(len(name_list) - len(set_list))
print(len(name_list))
