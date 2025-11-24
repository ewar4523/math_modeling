name = "Egor Krivorak"
arr = []

name_ = "_".join(name)

NAME_ = name_.upper()

ch_NAME_ = [ord(i) for i in NAME_]

name__ = name_.lower()

ch_name__ = [ord(i) for i in name__]

print(max(ch_NAME_), min(ch_NAME_), max(ch_name__), min(ch_name__))