from scripts.parser.jobParser import JobParser

DRY_RUN_PATHS = [
    'C:\\Scripts\Python-Playground\_NightlySVN.xml',
    'C:\\Scripts\Python-Playground\_NightlyWilma.xml',
]

# Dry run everything in a list
for path in DRY_RUN_PATHS:
    p = JobParser(path)

    for job in p.jobs:
        job.run()
        job.log()