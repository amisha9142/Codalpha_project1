def generate(end):
    if end < 0:
        return []
    
    numbers = []
    for i in range(0, end + 1, 2):
        numbers.append(i)
    
    return numbers

# Specify the desired range
end_range = 10  # Change this to your desired range

result = generate(end_range)
print(result)


