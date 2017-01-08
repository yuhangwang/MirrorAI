import sys

def hello(msg):
    print("Hello from Python, {}".format(msg))

if __name__ == '__main__':
    hello(sys.argv[0])