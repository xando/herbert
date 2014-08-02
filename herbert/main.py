import sys

from herbert import interpreter


def entry_point(argv):
    if len(argv) > 1:
        filename = argv[1]
        f = open(filename, 'r')
        source = f.read()
        f.close()

        ret = interpreter.interpret(source)
        if not ret['error']:
            print ret['code']
        else:
            print ret['error']['location']
            print ret['error']['message']
            print ret['error']['help']

        sys.exit()


    return 1


def target(driver, args):
    driver.exe_name = 'progpac-interpreter'
    return entry_point, None

def main():
    entry_point(sys.argv)

if __name__ == "__main__":
    main()
