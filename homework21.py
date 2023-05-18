def log_txt(dump):
    with open("user_out.txt", "w") as wt:
        wt.write(dump)


def log_json(dump):
    import json

    with open("users.json", "w") as wj:
        wj.write(json.dumps(dump))


def obtain_logs(file_path):
    lines = open(file_path).readlines()
    res_json = []
    res_txt = []

    for line in lines:
        line_strip = line.strip()

        if line_strip != "":
            line_list = line_strip.split(";")
            name = line_list[0]
            age = line_list[1]
            phones = [phone.strip() for phone in line_list[2].split(",")]

            l = []
            for phone in line_list[2].split(","):
                l.append(phone.strip())

            dump_json = {
                "name": name,
                "age": int(age) if age and age.isalnum() else None,
                "phones": phones if line_list[2] else []
            }

            dump_txt = {
                "name": name,
                "age": int(age) if age and age.isalnum() else "",
                "phones": phones if line_list[2] else ""
            }

            res_json.append(dump_json)
            res_txt.append(dump_txt)

    return {
        "txt": str(res_txt),
        "json": res_json,
    }

dumps = obtain_logs('users.txt')

log_txt(dumps["txt"])
log_json(dumps["json"])


