sehirler = ["bursa","istanbul"]
plakalar = [16,34]


# key - value

# print(plakalar[0], sehirler[0])


# print(plakalar[sehirler.index("istanbul")])
# print(sehirler[plakalar.index(16)])


#dictionary

plakalar = {
    "bursa": 16, 
    "istanbul": 34,
    "izmir": 36
    }

plakalar["izmir"] = 35

print(plakalar["bursa"])
print(plakalar["istanbul"])
print(plakalar["izmir"])
