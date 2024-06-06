import math
class Path():
    def __init__(self, curr_path, curr_score):
        self.curr_path = curr_path
        self.curr_score = curr_score
    
    def get_path(self):
        return self.curr_path

    def set_path(self, path):
        self.curr_path = path

    def get_score(self):
        return self.curr_score

    def set_score(self, score):
        self.curr_score = score

rooms = {'A': [40, ['B', 'C']], 'B': [50, ['C', 'D']], 'C': [75, ['B', 'D']], 'D': [100]}
paths = {'AB': math.ceil(2 + 3 * 4 - 5 / 10 + 5**2), 'AC': math.ceil(2**3 + 4 * 5 - 6 /10 + 1), 'BC': math.ceil(5 * 4 - 2 + 5**2 - 7), 'BD': math.ceil(3 + 4 * 5 - 8 / 2 + 1), 'CD':  math.ceil(3**3 + 8 - 5 * 3 + 8)}

temp_paths = []
best_path = ''
max_gold = 0

for i in range(2):
    new_path = Path('A' + rooms['A'][1][i], 40)
    temp_paths.append(new_path)

while len(temp_paths) != 0:
    entire_path = temp_paths[0].get_path()
    curr_path = entire_path[len(entire_path) - 2:len(entire_path)]
    curr_room = entire_path[-1]
    prev_room = entire_path[len(entire_path) - 2]
    if curr_path not in paths.keys():
        curr_path = curr_path[::-1]

    temp_paths[0].set_score(temp_paths[0].get_score() + rooms[curr_room][0] - paths[curr_path])
   
    if curr_path[1] == 'D':
        if temp_paths[0].get_score() > max_gold:
            max_gold = temp_paths[0].get_score()
            best_path = entire_path
    else:
        for i in range(2):
            if rooms[curr_path[1]][1][i] not in entire_path:
                new_path = Path(entire_path + rooms[curr_path[1]][1][i], temp_paths[0].get_score())
                temp_paths.append(new_path)
    
    temp_paths.pop(0)

print(best_path)
print(max_gold)
