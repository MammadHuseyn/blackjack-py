def print_card(rank, suit):
    top = "┌─────────┐"
    bottom = "└─────────┘"
    side = "│         │"

    if rank == "10":
        rank_right = rank
        rank_left = rank
    else:
        rank_right = rank + " "
        rank_left = " " + rank

    suit_line = f"│    {suit}    │"
    rank_line_left = f"│{rank_left}       │"
    rank_line_right = f"│       {rank_right}│"

    print(top)
    print(rank_line_left)
    print(side)
    print(suit_line)
    print(side)
    print(rank_line_right)
    print(bottom)



