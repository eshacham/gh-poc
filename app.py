import os
import subprocess

AWS_SECRET_ACCESS_KEY = 'AKIA1234567890ABCDEF'


def insecure():
    # BAD: reading a shell command from an environment variable
    # and passing it straight into subprocess.run with shell=True
    cmd = os.getenv("BAD_CMD", 'echo "This is a bad command"')
    subprocess.run(cmd, shell=True)


def mask_key(key):
    # BAD: masking the key in the logs
    # This is not a secure way to handle sensitive information
    return '*' * (len(key) - 4) + key[-4:]
    # return  key[-4:].rjust(len(key), '*')


def main():
    print(f"Hello from GitHub Secure CI/CD POC!: {mask_key(AWS_SECRET_ACCESS_KEY)}")
    insecure()


if __name__ == "__main__":
    main()


