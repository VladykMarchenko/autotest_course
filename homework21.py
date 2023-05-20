import json

file_name = 'users.txt'
out_file_txt = 'user_out.txt'
out_file_json = 'users.json'

def log_txt(dump):
    with open(out_file_txt, "w") as wt: #wt alliace
        wt.writelines(dump)


def log_json(dump):

    with open(out_file_json, "w") as wj:
        wj.write(json.dumps(dump))


def obtain_logs_json(file_path):
    lines = open(file_path).readlines()
    res_json = []

    for line in lines:
        line_strip = line.strip()

        if line_strip != "":
            line_list = line_strip.split(";")
            name = line_list[0].split()
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
            res_json.append(dump_json)


    return {
        "json": res_json
    }

dumps = obtain_logs_json(file_name)

log_json(dumps["json"])


def obtain_logs_txt(file_path):
    lines = open(file_path).readlines()
    result_txt = []
    for line in lines:
        line_strip = line.strip()

        if line_strip != "":
            line_list = line_strip.split(";")
            name = line_list[0].strip()
            age = line_list[1] if line_list[1].isalnum() else ""
            phones = [phone.strip() for phone in line_list[2].split(",")]
            phone1 = phones if line_list[2] else ""
            phones_users = ''
        for ph_users in phone1:
            phones_users += str(ph_users)

        l = []
        for phone in line_list[2].split(","):
            l.append(phone.strip())
        result_txt.append(name  + ";" + age + ";" + phones_users + "\n")

    return result_txt

dumps2 = obtain_logs_txt(file_name)

log_txt(dumps2)