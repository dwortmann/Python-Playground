import xml.etree.ElementTree as ET

from enum import Enum

#TODO - maybe there's a better way to import these like from jobs import * ?
from epic.parser.jobs.svnJob import SVNJob
from epic.parser.jobs.hswebJob import HSWebJob
from epic.parser.jobs.wilmaJob import WilmaJob
from epic.parser.jobs.cacheJob import CacheJob

class Type(Enum):
        Error = 0
        SVN = 1
        HSWeb = 2
        Cache = 3
        Wilma = 4

class JobParser:
    """Parser for xml configuration files"""
    
    #variables shared by all instances here

    def __init__(self, filePath):
        #Unique to instance
        self.filePath = filePath
        self.tree = self._open()
        self.root = self.tree.getroot()
        self.jobs = []
        self._parse_jobs()

    def _open(self):
        """Open XML file for parsing"""
        return ET.parse(self.filePath)

    def _parse_jobs(self):
        """Parse a single job from configuration"""
        for job in self.root:
            if job.tag != "Job":
                print('Not a job!')
                continue #TODO: Log some kind of error so user knows

            try:
                type = Type[job.attrib['type']]
            except KeyError:
                type = Type['Error'] #TODO: Log some kind of error so user knows
                print('Job type was invalid!')
                continue

            try:
                name = job.attrib['name']
            except KeyError:
                name = 'default name' #TODO - better default name
            
            actions = []
            for action in job:
                actions.append((action.tag, action.attrib))

            #Build appropriate job
            try:
                self.jobs.append(self._create_job(type,name,actions))
            except BadJobTypeException:
                continue #TODO better error handling and logging

    def _create_job(self, type, name, actions):
        """Create job of supported type

        Args:
            type (Type): Job type
            name (string): Job name
            actions (list): List of tuples containg actions and parameters

        Returns:
            Job object

        Raises
            BadJobTypeException: If job type is invalid

        """
        if type == Type.SVN:
            return SVNJob(name, actions)
        if type == Type.HSWeb:
            return HSWebJob(name, actions)
        if type == Type.Wilma:
            return WilmaJob(name, actions)
        if type == Type.Cache:
            return CacheJob(name, actions)

        raise BadJobTypeException('Invalid job type: {}'.format(str(type))) #TODO: Better error handling? Throw exception?

class BadJobTypeException(Exception):
    pass











