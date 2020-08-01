## Practice Dictionary

dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
a = {1:'hi'}
a = {'a':[1,2,3]}

a = {1:'a'}
a[2] = 'b'          # add up {2: 'b'}
a['name'] = 'pey'   
a
a[3] = [1,2,3]
a

del a[1]
a

# application
grade = {'pey': 10, 'julliet': 99}
grade['pey']
grade['julliet']

a = {1: 'a', 2:' b'}
a[1]
a[2]

a = {'a': 1, 'b': 2}
a['a']
a['b']

dic = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
dic['name']
dic['phone']
dic['birth']

# errors
a = {1:'a', 1:'b'}
a

a = {[1,2]: 'hi'}   # no list as a key(which should not be changed)

# functions
a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}

a.keys()            # show keys in the dictionary
list(a.keys())      # change the dict_keys object as a list

a.values()          # show values
a.items()           # show pairs of each key and value

a.clear()           # clear the dictionary

a.get('name')       # get values by keys
a.get('phone')

print(a.get('nokey'))
print(a.get['nokey'])   # syntax error

a.get('foo', 'bar')     # show invalid values

'name' in a             # investgate whether a key is in the dictionary
'email' in a

# question
b = {'name': 'hong', 'birth': '1128', 'age': '30'}