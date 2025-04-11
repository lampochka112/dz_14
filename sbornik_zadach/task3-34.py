def check_threats(a, b, c, d):
    rook_threat = a == c or b == d

    bishop_threat = abs(a - c) == abs(b - d)

    king_move = max(abs(a - c), abs(b - d)) == 1

    queen_threat = a == c or b == d or abs(a - c) == abs(b - d)

    pawn_move = a == c and b + 1 == d  
    pawn_capture = (a + 1 == c and b + 1 == d) or (a - 1 == c and b + 1 == d)  

    return {
        "rook_threat": rook_threat,
        "bishop_threat": bishop_threat,
        "king_move": king_move,
        "queen_threat": queen_threat,
        "pawn_move": pawn_move,
        "pawn_capture": pawn_capture
    }

a, b = 4, 4 
c, d = 5, 5  

threats = check_threats(a, b, c, d)
print("Угрозы и возможности перемещения:")
print(f"Ладья угрожает: {threats['rook_threat']}")
print(f"Слон угрожает: {threats['bishop_threat']}")
print(f"Король может переместиться: {threats['king_move']}")
print(f"Ферзь угрожает: {threats['queen_threat']}")
print(f"Пешка может сделать обычный ход: {threats['pawn_move']}")
print(f"Пешка может бить: {threats['pawn_capture']}")