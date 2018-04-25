#!/usr/bin/python
""" 
pyapi.py <options>
  --list displays all saved urlnames (overrides all over options)
  --action GET, POST, PUT, or DELETE HTTP action to call (required this or save)
  --url the URL string to send the request too (overrides urlname)
  --urlname the name to use from ~/.pyapi config file 
  --save persists the provided <URL> to <URLNAME> (requires this or action)


Author: Matt Cliff
Created: 25 Apr 201:    
"""
import argparse



def main():
    """
    Utility to call/invoke API
    """


    parser = argparse.ArgumentParser(prog='pyapi', description='PYthon API caller utlity')
    parser.add_argument('-l', '--list', nargs='?', help='print list of saved names and exit', default=False)
    parser.add_argument('-s', '--save', nargs='?', help='saves <url> to <name>', default=False)
    parser.add_argument('-a', '--action', help='HTTP action - POST GET PUT DELETE')
    parser.add_argument('-n', '--name', help='name to reference the url in ~/.pyapi')
    parser.add_argument('-u', '--url', nargs='?', help='URL to post to (overrides --name)')
    parser.add_argument('-d', '--data', help='JSON formatted string to pass in')
    args = vars(parser.parse_args())

    print args
    if args['list'] is not False:
        print "we have a list"
        exit()

    if args['save'] is not False:
        print "we have a save"

    if args['url'] is None and args['name'] is None:
        print "you must include either a url or name"
        exit(-2)

    if args['action'] is None and args['save'] is False:
        print "you must include either a action or save"
        exit(-2)

    


if __name__ == "__main__":
    main()
