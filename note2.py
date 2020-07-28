longer_phrase = "Hello, {}. Today is {}."

formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)

l = ["Bob", "Rolf", "Anne"]
t = ("Bob", "Rolf", "Anne")
s = {"Bob", "Rolf", "Anne"}

s.add('Smith')
s.add('Smith')
print(s)

### Advanced set operations

local = {"Bob", "Rolf"}
abroad = {"Bob", "Anne"}

friends = abroad.union(abroad)

friends = local.union(abroad)
print(friends)


art = {"Bob", "Jen", "Rolf", "Charlie"}
science = {"Bob", "Jen", "Adam", "Anne"}

both = art.intersection(science)
print(both)