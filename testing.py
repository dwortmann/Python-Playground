from scripts.parser.jobParser import JobParser
from scripts.hsweb.build import HSWebBuild

TEST_CONFIG_PATH = 'C:\\Scripts\Python-Playground\example.xml'

DRY_RUN_PATHS = [
    #'C:\\Scripts\Python-Playground\_NightlySVN.xml',
    #'C:\\Scripts\Python-Playground\_WeeklySVN.xml',
    #'C:\\Scripts\Python-Playground\_WeeklyWilma.xml',
    #'C:\\Scripts\Python-Playground\_MonthlyWilma.xml'
]

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

p = JobParser(TEST_CONFIG_PATH)

for job in p.jobs:
    #print(job)
    job.run()
    job.log()

# Dry run everything in a list
for path in DRY_RUN_PATHS:
    p = JobParser(path)

    for job in p.jobs:
        #print(job)
        job.run()
        job.log()

#h = HSWebBuild('8.4','App St1')
#h.clean()
#h.build('Nope.sln')
#print('start')
#kwargs={ 'solutions':'Schedule.sln ApplCore.sln Review.sln' }
#h.build(**kwargs)
#h.build_all_clean()
#h.build_all()
#h.build_core()
#h.build_common()
#h.publish()