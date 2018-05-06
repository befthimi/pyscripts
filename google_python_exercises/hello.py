#!/usr/bin/env python

# import modules used here -- sys is a very standard one
import sys

# Gather our code in a main() function
def main():
    if len(sys.argv) > 3:
        num_args = len(sys.argv) - 1
        print num_args, ' arguements specified'
        print 'Too many arguements specified. This may cause problems.'
        print '\n\n'
    try:
        print 'Hello there', sys.argv[1], sys.argv[2]
    except IndexError:
        print '\n\n***Missed a variable***'
        print '-' * 23
    # Command line args are in sys.argv[1], sys.argv[2] ...
    # sys.argv[0] is the script name itself and can be ignored

# Stanard boilerplate to call the main() function to begin
# the program.
if __name__ == '__main__':
    main()
