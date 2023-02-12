country_code={"America":1, "Korea":82, "China":86, "Japan":81}
print(country_code)
print(country_code.keys())
print(country_code.values())
print(country_code.items())

country_code["Germany"]=49
print(country_code)
print(country_code.keys())
print(country_code.values())
print(country_code.items())

for k,v in country_code.items():
    print("Key:",k)
    print("Value:",v)

print("Korea" in country_code.keys())
print("Italy" in country_code.keys())