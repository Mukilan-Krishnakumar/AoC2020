passports = []

valid_count = 0
with open("../puzzle_inputs/day_4_1.txt", "r") as file:
    for passport_str in file.read().split("\n\n"):
        passport = []
        for key in passport_str.replace("\n", " ").split():
            passport.append(key.split(":")[0])
        if len(passport) == 8 or (len(passport) == 7 and "cid" not in passport):
            valid_count += 1


print(valid_count)
