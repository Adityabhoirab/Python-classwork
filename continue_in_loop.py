# Program: Using 'continue' to skip the number 10 in the loop

print("\nUsing 'continue' to skip the number 10:")
for i in range(1, 21):
    if i == 10:  # Skip the iteration when i equals 10
        continue
    print(i)
