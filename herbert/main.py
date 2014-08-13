import sys
import json

from herbert import interpreter


def entry_point(argv):
    world = None

    if len(argv) > 1:
        source = open(argv[1], 'r').read()
        ret = interpreter.interpret(source, world)

        if not ret['error']:
            print "= Translated ="
            print "  %s" % ret['code']

            if len(argv) > 2:
                level = json.load(open(argv[2]))

                valid = False
                for line in level['content']:
                    for e in line:
                        if e in ['0', '1', '2', '3']:
                            valid = True

                if not valid:
                    print "Level file does not have starting position"
                    sys.exit(1)


                walk, position, success = interpreter.walk_world(level, source, ret['code'])
                print "\n= Level ="
                print "  walk: %s" % walk
                print "  position: x=%s y=%s" % position
                print "  solved: %s" % u"\u2605 " * success
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
