

import subprocess

def get_service_binding(service_instance):
    # Directly use the service_instance in the command without sanitization
    command = f"cf service {service_instance}"
    result = subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE)
    print(result.stdout.decode())

if __name__ == "__main__":
    # Example of a dangerous service instance name for testing
    service_instance = "my-database-service; rm -rf /"
    try:
        get_service_binding(service_instance)
    except subprocess.CalledProcessError as e:
        print(f"Command failed: {e}")
