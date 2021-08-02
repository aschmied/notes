# An example util module that we want to test.

# `reverse` takes a list and returns a new list with the same
# elements, but with their order reversed.
def reverse(l):
    return [element for element in reversed(l)]
