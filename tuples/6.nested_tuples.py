nested_tuple = (1, (2, 3), (4, (5, 6)))
print("Nested tuple:", nested_tuple)

#accessing the elements in a nested tuple
inner_tuple = nested_tuple[1]
second_level_nesting = nested_tuple[2][1]
deep_nested_element = nested_tuple[2][1][1]
deep_nested_element1 = nested_tuple[2][1][0]

print("Inner Tuple:", inner_tuple)
print("Second level nesting:", second_level_nesting)
print("Deep nested element:", deep_nested_element)
print("Deep nested element1:", deep_nested_element1)

