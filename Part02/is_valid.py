def is_valid(pin):
    return 3 < len(pin) < 7 and pin.isdigit()

print(is_valid('4367'))
print(is_valid('92134'))
print(is_valid('89abc1'))
print(is_valid('900876'))
print(is_valid('49 83'))
