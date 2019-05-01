import os
import sys
import wallaby

def main():
    print "hi"

if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main()
