number_of_lines = int(input("How many lines for Floyd's Triangle?\n"))

first_element_of_the_row = 1

for i in range(1,number_of_lines+1):
    vector_of_elements = []
    for j in range(first_element_of_the_row,first_element_of_the_row+i):
        vector_of_elements.append(j)
        first_element_of_the_row = j
    first_element_of_the_row = first_element_of_the_row + 1
    print(vector_of_elements)    
                                                                               