import sys

from herbert import interpreter


def entry_point(argv):
    world = None

    if len(argv) > 1:
        source = open(argv[1], 'r').read()

        if len(argv) > 2:
            world = open(argv[2], 'r').read()

        ret = interpreter.interpret(source, world)
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
