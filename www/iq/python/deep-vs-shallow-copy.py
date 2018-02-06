# List Bag1 one has fruits
bag1 = ['apple', 'banana']

# Lets create a Bag2 which has the same fruits as Bag1
bag2 = bag1  # Assignment statements in Python do not create a copy of object

import objgraph

objgraph.show_backrefs([bag1, bag2], filename='sample-graph.png')

print('Bag1: ', bag1)
print('Bag2: ', bag2)

# remove apple from bag1 which will effect bag2 as well
del bag1[0]

# Notice apple is removed from both the bags instead from bag1
print('Bag1: ', bag1)
print('Bag2: ', bag2)
