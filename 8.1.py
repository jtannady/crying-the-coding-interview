# 8.1 Triple Step
# A child is running up a staircase with n steps and can hope either 1 step, 2 steps, or 3 steps at a time.
# Implement a method to count how many possible ways the child can run up the stairs.

def count(steps):
    if (steps == 0):
        return 1
    
    steps_from_above = [1]
    for a in range(1, steps):
        steps_from_above.append(sum(steps_from_above[:a]))
    return sum(steps_from_above[:steps])

print count(0)
print count(5)
print count(12)