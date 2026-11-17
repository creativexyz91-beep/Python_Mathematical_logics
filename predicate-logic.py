"""
Nested Quantifiers in Python
----------------------------
L(x, y) means "x loves y". The domain is a small group of people.

Key idea:
    "for all x"    ->  all(...)
    "there exists" ->  any(...)
"""

people = ["Ann", "Bob", "Cat", "Dan"]

# Each pair (x, y) means "x loves y".
loves = {
    ("Ann", "Bob"),
    ("Bob", "Cat"),
    ("Cat", "Ann"),
    ("Dan", "Dan"),   # Dan loves only himself
}


def L(x, y):
    """L(x, y): does x love y?"""
    return (x, y) in loves


# 1a) Everybody loves somebody:  ∀x ∃y L(x, y)
q1a = all(any(L(x, y) for y in people) for x in people)

# 1b) Somebody is loved by everybody:  ∃y ∀x L(x, y)
q1b = any(all(L(x, y) for x in people) for y in people)

# 1c) Nobody loves everybody:  ¬∃x ∀y L(x, y)
q1c = not any(all(L(x, y) for y in people) for x in people)

# 1d) Everyone loves himself or herself:  ∀x L(x, x)
q1d = all(L(x, x) for x in people)

# 1e) Someone loves no one besides himself/herself:
#     ∃x ∀y ( y ≠ x → ¬L(x, y) )
q1e = any(all(not L(x, y) for y in people if y != x) for x in people)

print("1a  Everybody loves somebody      :", q1a)
print("1b  Somebody is loved by everybody:", q1b)
print("1c  Nobody loves everybody        :", q1c)
print("1d  Everyone loves themself       :", q1d)
print("1e  Someone loves only themself   :", q1e)

# Sanity check: negation flips every quantifier.
#   ¬∃x ∀y L(x,y)  ≡  ∀x ∃y ¬L(x,y)
q1c_flipped = all(any(not L(x, y) for y in people) for x in people)
assert q1c == q1c_flipped
print("\nNegation rule verified: ¬∃x∀y L  ==  ∀x∃y ¬L")