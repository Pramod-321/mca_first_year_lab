#string manipulation 
text="python"
char_array=list(text) # this  convert string to array 
print(char_array)
print(type(char_array))
#modifying element using a index 
char_array[0]="p"
char_array[1]="y"
print(type(char_array))
new_text = "".join(char_array)
print(new_text)
print(type(new_text))