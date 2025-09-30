# Each component is defined by a list of two elements, component type and value
r = ['Resistor', 100]
c = ['Capacitor', 1e-6]
i = ['Inductor', 0.2]
q = ['Transistor', 'BC108']

# Parts is a list of lists (i.e. a 2-dimensional list)
parts = [r, c, i, q]

# Exercise 1
print(parts[2])     # Print the third line of the list (index = 2)
# Exercise 2
print(parts[1][1])  # Print the capacitor value (second component: index 1, second list entry: index 1)
# Exercise 3
parts[3][1] = '2N0000'  # Change the value of the transistor entry
print(parts)            # Print entire list of lists
