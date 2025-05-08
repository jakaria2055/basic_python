info = {
    "name": "jakaria",
    "age": 23,
    "dept": "cse",
    "class": "4th",
    "sub": ["python", "C", "java"],
    "topics": ("dict", "set"),
    "adult": True,
    12.94: 94.4
}

# print(info)
# print(type(info))


# print(info["name"])
# print(info["age"])
# print(info["sub"])
# print(info["topics"])
# print(info["adult"])


#ERROR
# print(info["fullname"])


# info["name"] = "Mishal"  #modify value
# info["surname"] = "Ahmed"  #add new value
# print(info)



# null_dict = {}
# null_dict["name"] = "Jakaria"
# print(null_dict)



student = {
    "name": "jakaria",
    "sub": {
        "math": 94,
        "ban": 80,
        "eng": 89
    }
}

# print(student)
# print(student["sub"]["eng"])
# print(student.keys())
# print(list(student.keys()))
# print(len(list(student.keys())))



# print(list(student.values()))



# print(list(student.items()))


# print(student["name"])
# print(student.get("name"))

# print(student.get("name1"))  #return none value

add_val = {"thana": "burikuri"}
student.update({"city": "chaka"})
student.update(add_val)
print(student)
