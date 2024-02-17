#person_messages 
first_name="richard"
last_name="akukumah"
full_name= f"{first_name} {last_name}"
message= f"Hello {full_name.title()},would you love to study some python courses with me?"
print(message)

#name_case
first_name= "rose"
last_name= "akukumah"
full_name= F"{first_name} {last_name}"
print(full_name.lower())
print(full_name.upper())

#famous_quotes
print("Albert Einstein said,'diamonds don't shine they reflect.'")

famous_person="albert einstein"
message= f"{famous_person.title()} said, 'diamonds don't shine they reflect'"
print(message)

#stripping_names 
name= 'emmanuel '
name
name.rstrip()

#file_extensions
#in_here_i_used_the_removesuffix_function_to_remove_the_extension_".text"
file_name='python_notes.text'
print(file_name.removesuffix(".text"))