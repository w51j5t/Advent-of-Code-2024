# read input file
with open("day-1-input.txt") as f:
    lines = f.readlines()

# get the left and right id as int
left_ids = []
right_ids = []
for line in lines:
    ids = line.split()
    left_ids.append(int(ids[0]))
    right_ids.append(int(ids[1]))

# sort the ids from smallest to largest
left_ids = sorted(left_ids)
right_ids = sorted(right_ids)

# compute total distance
total_distance = 0
for i in range(len(left_ids)):
    total_distance += abs(left_ids[i] - right_ids[i])

print(f"total distance: {total_distance}")

similarity_score = 0
# some variable to help
pointer = 0
previous_left_id = 0
previous_score = 0

# looping left ids
for left_id in left_ids:
    if left_id == previous_left_id:
        # increase the similarity score directly 
        similarity_score += previous_score
        continue
    
    # since both ids have been sorted from smallest to largest
    # if current left id is larger than the right id
    # search the next right id
    try:
        while left_id > right_ids[pointer]:
            pointer += 1
    except IndexError:
        # the remaining left ids are larger than any right id
        break
    
    if left_id <= right_ids[pointer]:
        # initialize the variables below
        previous_left_id = left_id
        previous_score = 0
        
    # if left id is matching right id
    # compute similarity score
    # otherwise just proceed with the next left id
    while left_id == right_ids[pointer]:
        previous_score += right_ids[pointer]
        pointer += 1
    
    similarity_score += previous_score
        
print(f"similarity score: {similarity_score}") 