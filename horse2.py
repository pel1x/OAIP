

def horse2(position):
    moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    

    stolb = position[0]
    ryd = int(position[1])

    stolb_index = 'abcdefgh'.index(stolb) + 1

    possible_moves = []
    
    for move in moves:
        new_stolb = stolb_index + move[0]
        new_ryd = ryd + move[1]
        
        if 1 <= new_stolb <= 8 and 1 <= new_ryd <= 8:
            new_position = 'abcdefgh'[new_stolb - 1] + str(new_ryd)
            possible_moves.append(new_position)
    
    return possible_moves

