import sys
from .hashport import hashport


def main():
    print(hashport(''.join(sys.argv[1:])))


if __name__ == "__main__":
    main()
