import os

path_folder = input(r'Please enter the path folder: ')

print()
print('Path Folder: {}'.format(path_folder))

old_extension = '.' + input("Enter the old extension (jpg,txt etc.) -> ")
new_extension = '.' + input("Enter the new extension (jpg,txt etc.) -> ")
print()

filesCounter = 0

for cfile in os.scandir(path_folder):
    
    #This method returns True if the entry is a file otherwise returns False
    if cfile.is_file(): 
        
        #These method returns a tuple that represents
        #root and ext part of the specified path name.                          
        root, ext = os.path.splitext(cfile.path) 

        if ext == old_extension:
            new_path = root + new_extension
            os.rename(cfile.path, new_path)
            filesCounter +=1
                
print()
print("Number of files proceesed: {}".format(filesCounter))
print("Extension: from {} to {}".format(old_extension,new_extension))