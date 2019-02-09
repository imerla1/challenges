from math import pi

def my_pi(n):
    if n > 15:
        return False
    else:
        new_pi = str(pi)
        return new_pi[0:n+1]

print(my_pi(12)
)
