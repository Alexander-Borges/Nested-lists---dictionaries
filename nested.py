#1 Update Values in Dictionaries and Lists
x = [ [5,2,3], [10,8,9] ] 
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

#1 Change the value 10 into x to 15
x[1][0]= 15
print(x)

#2 Change the last_name of the first student from 'Jordan' to 'Bryant'
students[0]['last_name'] = 'Bryant'
print(students)

#3 In the sports_directory, change 'Messi' to 'Andres'
sports_directory['soccer'][0]= 'Andres'
print(sports_directory)

#4 
z[0]['y']=30
print(z)

#2 Create a function iterateDictionary(some_list) that, given a list of dictionaries, the function loops through each dictionary in the list and prints each key and the associated value. For example, given the following list:
students = [
    {'first_name':'Michael', 'last_name': 'Jordan'},
    {'first_name':'John', 'last_name': 'Rosales'},
    {'first_name':'Mark', 'last_name': 'Guillen'},
    {'first_name':'KB', 'last_name': 'Tonel'}
]

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
def iterateDictionary(students):
    for dictionary in students:
        for key, value in dictionary.items():
            print(f"{key}- {value}")

iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

def iterateDictionary2(key_name,some_list):
    for dictionary in some_list:
        if key_name in dictionary:
            print(dictionary[key_name])

#list of dictionaries
students = [
    {"first_name": "Michael","last_name": "Jordan"},
    {"first_name": "John","last_name": "Rosales"},
    {"first_name": "Mark","last_name": "Guillen"},
    {"first_name": "KB","last_name": "Tonel"},
    {"first_name": "copy","last_name": "copy"}
]

#Calling the function with the example key name and list
iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)
print()

def printInfo(some_dict):
    for key, value in some_dict.items():
        print(f"{key}: {len(value)}")
        for item in value:
            print(item)

dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC','Burbank'],
    'instructors': ['Michael','Amy', 'Eduardo','Josh','Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)