from scripts.parser.jobParser import JobParser

DRY_RUN_PATHS = [
    'C:\\Scripts\Python-Playground\_AdHoc.xml',
    #'C:\\Scripts\Python-Playground\_WeeklySVN.xml',
    #'C:\\Scripts\Python-Playground\_WeeklyWilma.xml',
    #'C:\\Scripts\Python-Playground\_MonthlyWilma.xml'
]

# Dry run everything in a list
for path in DRY_RUN_PATHS:
    p = JobParser(path)

    for job in p.jobs:
        job.run()
        job.log()