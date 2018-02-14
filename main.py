import sys
import codecs
from regularizer import regularization


def main():
    print("Enter Katakana")
    sys.stdout.write("> ")
    sys.stdout.flush()
    line = sys.stdin.readline().strip()
    line = codecs.decode(line, 'utf-8')
    while line and line != 'quit':
        print(regularization(line))
        sys.stdout.write("> ")
        sys.stdout.flush()

        line = sys.stdin.readline().strip()
        line = codecs.decode(line, 'utf-8')
        if line == 'quit':
            break


if __name__ == "__main__":
    main()
