items = 'zero one two three'.split()
print(items)
items='zero,one,two,three'.split(',')
print(items)
items='zero.one.two.three'.split('.')
print(items)
items='zero. one. two. three'.split('. ')
print(items)

items_list=''.join(items)
print(items_list)
items_list=','.join(items)
print(items_list)
items_list='.'.join(items)
print(items_list)
items_list='. '.join(items)
print(items_list)