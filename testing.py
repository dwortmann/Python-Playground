from scripts.parser.jobParser import JobParser

GLOBAL = 10
GLOBAL_2 = 'this'
CONFIG_PATH = 'C:\\Users\Dan Wortmann\Documents\Python Projects\Python-Playground\example.xml'

def print_info(element):
    print('Tag: ' + element.tag)
    print('Attribute: ' + str(element.attrib), end='\n\n')

def svn_update_tests(job):
    job._update("this/is/a/path")
    job._update("this/is/a/path",12312)
    job._update("this/is/a/path/",'123536')
    job._update("/this/is/a/path",'0000099123536')
    job._update("this/is/a/path",'0000099df123536')

def svn_checkout_tests(job):
    job._checkout("this/is/a/path")
    job._checkout("this/is/a/path/",12312)
    job._checkout("/this/is/a/path",'123536')
    job._checkout("this/is/a/path",'0000099123536')
    job._checkout("this/is/a/path",'0000099df123536')

p = JobParser(CONFIG_PATH)

for job in p.jobs:
    #print(job)
    job.run()
    job.log()