def calculate_pet_years(human_years):
    # Ensure human_years is at least 1
    if human_years < 1:
        return "humanYears must be >= 1"

    # Calculate cat years
    if human_years == 1:
        cat_years = 15
    elif human_years == 2:
        cat_years = 15 + 9
    else:
        cat_years = 15 + 9 + (human_years - 2) * 4

    # Calculate dog years
    if human_years == 1:
        dog_years = 15
    elif human_years == 2:
        dog_years = 15 + 9
    else:
        dog_years = 15 + 9 + (human_years - 2) * 5

    return [human_years, cat_years, dog_years]

# Test examples
print(calculate_pet_years(10))  # [10, 56, 64]
print(calculate_pet_years(1))   # [1, 15, 15]
print(calculate_pet_years(2))   # [2, 24, 24]
