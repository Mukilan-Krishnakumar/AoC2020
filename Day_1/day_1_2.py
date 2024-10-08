puzzle_input = [int(line.rstrip()) for line in open("../puzzle_inputs/day_1_1.txt",  "r")]

def brute_force(input_list):
    final_sum = 0
    for num_i, i in enumerate(input_list):
        for num_j, j in enumerate(input_list):
            for num_k, k in enumerate(input_list):
                if num_i != num_j != num_k and i + j + k == 2020:
                    final_sum += i * j * k
                    input_list.remove(i)
                    input_list.remove(j)
                    input_list.remove(k)
    return final_sum

answer = brute_force(puzzle_input)
print(answer)
