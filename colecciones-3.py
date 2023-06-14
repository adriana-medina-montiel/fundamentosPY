teacher = {
    "name":"francisco",
    "l_name":"lopez",
    "phone":"247123456",
    "groups":["3ADSM","3BDSM"]

}
print(type(teacher))
print(teacher)
print(teacher["name"])
print(teacher["groups"])
teacher["groups"].append("3cdsm")
teacher["phone"]="2471070644"
teacher["city"]="huamantla"
print(teacher)