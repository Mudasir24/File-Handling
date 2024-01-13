# Opening the original file in read mode
fptr = open("C:\\Users\\Mohammed Mudasir\\OneDrive\\Desktop\\MSS projects\\product_description.txt","r")

# Opening the new file in write mode
fpnew = open("C:\\Users\\Mohammed Mudasir\\OneDrive\\Desktop\\MSS projects\\formatted_descriptions.txt","w")

if fptr and fpnew:
    print("The files are opened successfully.")
    lines = fptr.readlines()

# Capitalizing the first letter of each word and writing them in the new file
    for line in lines:
        new_lines = [line.title()]
        fpnew.writelines(new_lines)
    
# Closing the files
    fptr.close()
    fpnew.close()
else:
    print("The files are not opened.")