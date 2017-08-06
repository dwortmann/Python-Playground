from scripts.parser.jobParser import JobParser

GLOBAL = 10
GLOBAL_2 = 'this'
CONFIG_PATH = 'C:\\Users\Dan Wortmann\Documents\Python Projects\Python-Playground\example.xml'

def print_info(element):
    print('Tag: ' + element.tag)
    print('Attribute: ' + str(element.attrib), end='\n\n')

p = JobParser(CONFIG_PATH)

for job in p.jobs:
    print(job)
    print(job.report())
    if job.name == 'optional 1':
        job.update()
        job.checkout()
        job.revert()
        job.cleanup()
    
print(len(p.jobs))