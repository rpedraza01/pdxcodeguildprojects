#keys_values_fruits.py
name, color
apple, red?
mango, yellow?
lime, green

contents = [
"name, color",
"apple, red?",
"mango, yellow?",
"lime, green"
]

keys = contents[0].split(",") -> ["name", "color"]
apples = contents[1].split(",") -> ["apple", "red?"]
mango = contents[2].split(",") -> ["mango", "yellow?"]
lime = contents[3].split(",") -> ["lime", "green"]

