def parse(text: str) -> dict:
    data = {}
    section = ""

    for line in text.split("\n"):
        if line.startswith(";"):
            continue

        elif line.startswith("[") and line.endswith("]"):
            line = line.replace("[", "")
            line = line.replace("]", "")

            section = line.strip()

            if not data.get(section):
                data[section] = {}
        
        elif "=" in line:
            key, value = line.split("=")[0], "=".join(line.split("=")[1:])
            key = key.replace('"', "")
            key = key.replace("'", "")
            key = key.strip()

            value = value.replace('"', "")
            value = value.replace("'", "")
            value = value.strip()

            data[section][key] = value

    return data


def convert(data: dict) -> str:
    text = ""
    for section in data:
        text += "[%s]\n" % section

        for key in data[section]:
            text += "%s=%s\n" % (key, data[section][key])

        text += "\n"

    return text.strip()


def load(file: str) -> dict:
    with open(file, "r") as f:
        text = f.read()
    return parse(text)

def dump(data: dict, file: str) -> str:
    with open(file, "w") as f:
        text = convert(data)
        f.write(text)
    return text