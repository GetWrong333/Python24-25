def fun(n):
    # Convert number to binary and remove "0b" prefix
    bin_rep = bin(n)[2:]

    max_gap = 0  # Max gap length
    current_gap = 0  # Current gap length

    counting = False  # did we started counting gaps 

    for bit in bin_rep:
        if bit == '1':
            if counting:  # End gap
                max_gap = max(max_gap, current_gap)
            counting = True  # Start counting 
            current_gap = 0  # Reset gap length
        elif counting:
            # Count zeros
            current_gap += 1

    return max_gap

if __name__ == "__main__":
    N = 529  # Example value, expected result 4
    wynik = fun(N)
    print(f"Reprezentacja binarna {N}: {bin(N)}")
    print(f"fun({N}): {wynik}")
