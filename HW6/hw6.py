# Homework 6
import re

# REGULAR EXPRESSIONS

# Write patterns for regular expressions a-d here.
# You must use a single regular expression for each item.
# For part d, also include a substitution string.

a = re.compile(r"^[0-9]*5[0-9]*5[0-9]*$")

b = re.compile(r"^(1[0-2]|[1-9]):([0-5][0-9]) (AM|PM)$")

c = re.compile(r"^([a-zA-Z_][a-zA-Z0-9_]*(, [a-zA-Z_][a-zA-Z0-9_]*)*)?$")

d = re.compile(r"^([a-zA-Z0-9_]+)\s*([<]|[<]=)\s*([a-zA-Z0-9_]+)$")
subStr = r"\3 \2 \1"   # Place what you want to substitute (used in sub)

# TESTS

print("----Part a tests that match:")
print(a.search("15445"))
print(a.search("55"))
print(a.search("05563"))

print("----Part a tests that do not match:")
print(a.search("12346789"))
print(a.search("555"))
print(a.search("123a45"))

print("----Part b tests that match:")
print(b.search("1:45 PM"))
print(b.search("12:00 AM"))
print(b.search("9:59 PM"))

print("----Part b tests that do not match:")
print(b.search("20:30"))
print(b.search("0:00 AM"))
print(b.search("1:60 PM"))
print(b.search("1:45pm"))

print("----Part c tests that match:")
print(c.search("hello, get_max, sum3"))
print(c.search(""))
print(c.search("var1, _var2, x3"))

print("----Part c tests that do not match:")
print(c.search("1, 2; hello"))
print(c.search("var1,var2"))
print(c.search("var1, var2,"))

print("----Part d tests:")
print(d.sub(subStr, "a < b"))
print(d.sub(subStr, "x <= y"))
print(d.sub(subStr, "var1 < var2"))
print(d.sub(subStr, "a<b"))
print(d.sub(subStr, "a < b < c"))  # Should not match
print(d.search("a < b < c"))
