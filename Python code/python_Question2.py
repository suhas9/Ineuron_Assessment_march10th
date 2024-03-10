def print_welcome_mat(N, M):
    # Print the top part
    for i in range(N // 2):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(M, '-'))

    # Print the middle part with "WELCOME"
    print('WELCOME'.center(M, '-'))

    # Print the bottom part
    for i in range(N // 2 - 1, -1, -1):
        pattern = '.|.' * (2 * i + 1)
        print(pattern.center(M, '-'))

# Example usage
N = 7  # Example odd natural number
M = 3 * N  # M should be 3 times N
print_welcome_mat(N, M)
