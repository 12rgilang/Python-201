#how you write new file
# with open('new_files.txt', 'w') as file:
#     file.write("this is how you create new files in Python-201") #if we change this text it will replace the documents with newer command
    # file.write("\n\tThis is tabbed!")

#if you want append(add some text) to existing text this the syntax look like
# with open('new_files.txt', 'a') as file:
#     file.write(" this is append ny another code")

#if you want add a new line this is the syntax
# with open('new_files.txt', 'a') as file:
#     file.write("\nSecond line")

# if you want to add new line with tab in it this the syntax
with open('new_files.txt', 'a') as file:
    file.write("\n\tThis line tabbed")
..