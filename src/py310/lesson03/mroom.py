people_list = ["Ehren",[0,1,2,3,4]],["Andy",[0,1,2,3]]
print(type(people_list))


people_list = ["Ehren",[0,1,2,3,4], "Andy",[0,1,2,3]]
print(type(people_list))

choice = "Bob"
donation = 5
for people in people_list:
    if people[0] == choice:
        print(people)
    for donation in people[1]:
        print(donation)
