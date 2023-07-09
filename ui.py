# CIS 41B Spring 2023
# Surajit A Bose
# Lab 1 ui.py


import states

class UI() :
    
    def __init__(self) :
        '''
        Prompt for filename, create States object from file, then create UI object. 
        UI object has one atribute, self.states, a single States object.
        '''
        valid_file = False
        default = states.States.INPUT_FILE
        while not valid_file :
            print('\nEnter input file name or return to use default', default)
            input_file = input('Input file name: ')
            if not input_file:
                input_file = default
            try: 
                self.states = states.States(input_file)
                valid_file = True
            except FileNotFoundError :
                print(f'Cannot find {input_file}, please try again.')
            except IOError :   # if file is not a valid csv or is not readable
                print(f'Error reading {input_file}, please try again.')
                
    def getValidNumericInput(self, prompt_str) :
        '''
        Get valid integer input from user
        
        @param prompt_str contextual prompt
        @return number valid int 
        '''
        valid_num = False
        while not valid_num :
            try: 
                in_str = input('Enter ' + prompt_str + ': ').strip()
                num = int(in_str)
                valid_num = True
            except ValueError :
                print('Must enter a number')
        return num
                
    def validate_year(self, year) :
        '''
        Check whether user has entered a valid census year. If year
        is invalid, raise ValueError.
        
        @param year the year entered by the user
        @return None
        '''
        if year not in states.States.CENSUS_YEARS :
            raise ValueError(year) 
           
    def listStatesByPop(self) :    
        '''
        Print out the population of the given number of states 
        for the given year, in descending order. If number of states given
        is 50 or greater, print all states + Washington, DC.
    
        @param year the year for which user wants population data
        @param num the number of states for which user wants to see data
        @return None
        '''
        try :
            year = self.getValidNumericInput('year')
            self.validate_year(year)   
            
            num = self.getValidNumericInput('number of states')
            while num <= 0 :
                print('Number must be above zero')
                num = self.getValidNumericInput('number of states')
            # if user enters 50 or more, assume user wants all the data
            length = self.states.total_states
            if num >= length - 1 : 
                num = length     
                print('Displaying all states and Washington, DC')   

            print()
            gen = self.states.genStatesByPop(year)
            for i in range(num):
                state, pop = next(gen)
                print(f'{state:20s} {pop:>10,d}')
            
        except ValueError as err:
            print(f'{err} is not a valid census year')
            
    def listStatesByGrowth(self) :
        '''
        Print states and their positive or negative growth based on input.
        '''
        parity = 'x'
        while parity not in ['p', 'n'] :
            print('p.  positive')
            print('n.  negative')
            parity = input('Enter your choice, p/n: ').lower()
        positive = parity == 'p' 
        
                
        print()
        states_growth = self.states.getGrowthRate(positive)
        state, growth = next(states_growth)
        while state: 
            print(f'{state:20s} {growth * 100:>6.2f}%')
            state, growth = next(states_growth)
            
    def printPopulationDrop(self) :
        '''
        Check whether any state has dropped in population between
        two years specified via user input.
        '''
        try :
            start = self.getValidNumericInput('start year')
            self.validate_year(start)
    
            end = self.getValidNumericInput('end year')
            self.validate_year(end)  
                
            if end <= start :
                print('End year must be later than start year, please try again')
            else: 
                drop = self.states.checkPopulationDrop(start, end)
                if drop :
                    print(f'Population drop in at least one state between {start} and {end}')
                else :
                    print(f'No population drop across all states between {start} and {end}')
                    
        except ValueError as err:
            print(f'{err} is not a valid census year')
          
    def getUserChoice(self) :
        '''
        Print menu and prompts user until there is a valid choice.
        
        @return choice, validated user choice
        '''
        valid_choice = False
        while not valid_choice :
            print('\n\t1. View most populous states')
            print('\t2. View growth in 2021')
            print('\t3. Check population drop')            
            print('\t4. Quit')
            choice = input('\nEnter your choice: ').strip()
            if choice in ['1', '2', '3', '4'] :
                valid_choice = True
            else :
                print('Invalid choice. Please enter a number between 1 and 4')
        return (int(choice))
    
    def run(self) :
        '''
        Code driver. Loop to print the menu and process the user choice
        until the user chooses to quit.
        '''
        keepGoing = True
        funs = [0, self.listStatesByPop, self.listStatesByGrowth, \
                self.printPopulationDrop]
        while keepGoing :
            choice = self.getUserChoice()
            if choice == 4:
                keepGoing = False
                print('bye bye')
            else :
                funs[choice]()
                
UI().run()
