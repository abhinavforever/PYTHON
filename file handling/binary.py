some_bytes = b'apple'
 
# Open in "wb" mode to
# write a new file, or
# "ab" mode to append
with open("fi.txt", "wb") as binary_file:
   
    # Write bytes to file
    binary_file.write(some_bytes)

bytes=b"\n\tmango"
with open("fi.txt","ab") as bf:
    bf.write(bytes)

import pickle

with open ("fi2.bin","wb") as fi2:
    pickle.dump("apple is great\n and the best",fi2)
with open ("fi2.bin","rb") as rb:
    e=pickle.load(rb)
    print(e)

binary_content="\nbest in the world"
with open("fi2.bin","ab") as fi2:
    pickle.dump(binary_content,fi2)

with open("fi2.bin","rb") as fi2:
    content=pickle.load(fi2)
    print(content)