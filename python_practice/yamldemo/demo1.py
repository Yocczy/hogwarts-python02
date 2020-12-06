import yaml

document = """
    a: 1
    b: 
        c: 3
        d: 4
"""

print(yaml.safe_load(document))
print(yaml.dump(yaml.safe_load(document)))
