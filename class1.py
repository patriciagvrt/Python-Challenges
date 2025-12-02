import platform
import sys

if __name__ == "__main__":
    print("Hello world")
    print(f"python {sys.version}")
    name = platform.system()
    version = platform.version()
    print(f"on {name} ({version})")
    