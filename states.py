# CIS 41B Spring 2023
# Surajit A Bose
# Lab 1 states.py

import csv


class States() :
    '''
    States object has two attributes:
        1. self.data, a dictionary
            key: state name (str)
            value: tuple that has two elements:
                1. list of ints which are populations for census years
                2. float with population change between 2020 and 2021
        2. self.num_states, number of states in self.data
    
    States class has three attributes:
        1. INPUT_FILE string specifying the input file with population data
        2. OUTPUT_FILE string specifying the log file of method calls
        3. CENSUS_YEARS list of census years whose data is given in input file
    '''
    
    # Class attributes
    INPUT_FILE = 'statesPop.csv'
    OUTPUT_FILE = 'logfile.txt'
    CENSUS_YEARS = [1990, 2000, 2010, 2020]
    
    def __init__(self, input_file = INPUT_FILE) :
        '''Create States object from specified or default input file'''
        self.data = {}
        with open (input_file) as infile :
            reader = csv.reader(infile)
            for line in reader: 
                self.data[line[0]] = (list(map(int, line[1:-2])), float(line[-1]))
        self.num_states = len(self.data)
        
    # getter method for the maximum number of states
    @property 
    def total_states (self) :
        return self.num_states 
  
    # decorator to log function calls
    def logger(fun) :
        def wrapper(*args, **kwargs) :
            try:
                with open(States.OUTPUT_FILE, 'a') as logfile:
                    logfile.write(f'{fun.__name__}\n')
                    result = fun(*args, **kwargs)
            except IOError :
                print('Unable to write to ' + States.OUTPUT_FILE + \
                      '. Continuing without logging.')
            return result
        return wrapper         
     
    @logger
    def genStatesByPop(self, year) :
        '''
        List the states with their population for a given year,
        sorted in descending order
        
        @param year the year for which the user wants the state populations
        @return generator for state population data for given year
        '''
        year_index = States.CENSUS_YEARS.index(year)
        return ((state, self.data[state][0][year_index]) \
                for state in sorted(self.data, \
                key = lambda k : self.data[k][0][year_index], reverse = True))    
                
    @logger 
    def getGrowthRate(self, positive):
        '''
        Yield a state and its growth rate based on user choice of
        positive or negative growth. When out of states, yield None, None
        
        @param positive Boolean indicating whether user wants positive growth
        @return None
        '''
        growth_iter = self.data.items().__iter__()   
        while True :
            try :
                item = next(growth_iter)
                if positive ^ (item[1][1] < 0) :
                    yield item[0], item[1][1]    
            except StopIteration :
                yield None, None
                break
              
    @logger
    def checkPopulationDrop(self, start, end) :
        '''
        Check whether at least one state has dropped in population between 
        two given years
        
        @param start starting year
        @param end ending year
        @return Boolean indicating whether any state has dropped in population
        '''
        start_index = States.CENSUS_YEARS.index(start)
        end_index = States.CENSUS_YEARS.index(end)
        return any(val[0][start_index] > val[0][end_index] \
                   for val in list(self.data.values()))
    
