import re
passports = []

valid_count = 0
with open("../puzzle_inputs/day_4_1.txt", "r") as file:
    for passport_str in file.read().split("\n\n"):
        passport = []
        for key in passport_str.replace("\n", " ").split():
            passport.append((key.split(":")[0], key.split(":")[-1]))
        passport_keys = [passport_val[0] for passport_val in passport]
        passport_val = [passport_val[1] for passport_val in passport]
        passport_dict = dict(zip(passport_keys, passport_val))
        if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport_keys):
            byr_check = 1920 <= int(passport_dict["byr"]) <= 2002
            iyr_check = 2010 <= int(passport_dict["iyr"]) <= 2020
            eyr_check = 2020 <= int(passport_dict["eyr"]) <= 2030
            hgt_units = passport_dict["hgt"][-2:]
            hgt_conditions = {
                "cm" : (150, 193),
                "in" : (59, 76),
            }
            hgt_check = False
            if hgt_units in ["cm", "in"]:
                hgt_val = int(passport_dict["hgt"][:-2])
                lower_bound = hgt_conditions[hgt_units][0]
                upper_bound = hgt_conditions[hgt_units][1]
                hgt_check = lower_bound <= hgt_val <= upper_bound

            hcl_check = re.fullmatch("#[a-z0-9]{6}", passport_dict["hcl"])
            ecl_check = passport_dict["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
            pid_check = re.fullmatch("[0-9]{9}", passport_dict["pid"])
            if byr_check and iyr_check and eyr_check and hgt_check and hcl_check and ecl_check and pid_check:
                valid_count += 1       

print(valid_count)
