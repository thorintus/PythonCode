'''
Created on Oct 28, 2015

@author: Lex Hokanson
'''
import re

class Icd10_search(object):
    '''
    ICD-CM 10 Term/Code search
    '''
    def __init__(self, search_parameter='', search_results=''):
        '''
        Search parameter and search results as attributes.
        Create the codes dictionary from the source file.
        '''
        self.search_parameter = search_parameter
        self.search_results = list(search_results)
        
        icd10_codes = open("icd10cm.txt", 'r')
        self.icd10_dict = {}
        for line in icd10_codes:
            line = line.strip()
            elements = line.split('\t')
            self.icd10_dict.update({elements[0]: elements[1]})
            
        icd10_codes.close()
    
    def result_presenter(self, search_parameter, search_results):
        '''
        Print out the search parameter and all corresponding codes
        '''
        print("Your search parameter: {}".format(search_parameter + "\n"))
        if len(search_results) == 0:
            print("There were no results for that search.")
        elif len(search_results) == 1:
            print("{}".format(search_results[0]))
        else:
            for i in search_results:
                print("{}".format(i))
            print("Search found {} results.".format(len(search_results)))
            
    def result_logger(self, search_parameter, search_results):
        '''
        Write to an external file the search parameter and corresponding codes
        '''
        outfile = open("ICD10SearchResults.txt", 'a')
        outfile.write("Search parameter: {}".format(search_parameter) + '\n\n')
        for i in search_results:
            outfile.write("{}".format(i) + '\n')
        outfile.write("-"*50 + '\n')
        
    def key_search(self, code_search):
        '''
        If searching by an ICD10-CM code find related terms
        ''' 
        self.search_results = []   
        for k, v in self.icd10_dict.items():        
            if re.match(code_search, k, flags=re.IGNORECASE):
                self.search_results.append(k + " : " + v)
                self.search_results.sort()       
            
    def value_search(self, term_search):
        '''
        If searching for a term or word in a term        
        '''
        self.search_results = []
        code_search = re.compile(r'{0}'.format(term_search), flags=re.IGNORECASE)
        for k, v in self.icd10_dict.items():
            if code_search.search(v):
                self.search_results.append(k + "\t" + v)
                self.search_results.sort()
    
    def search_term(self):
        '''
        Infinite loop to keep searching for codes or terms if desired
        Loop is broken by appropriate input
        '''
        while True:
            lookup = input(
                        "Do you want to search by code or term or to quit?\n>")
            if lookup == "code" or lookup == "Code" or lookup == "c":
                self.search_parameter = input(
                                        "What code do you want to look for?\n>")
                self.key_search(self.search_parameter)
                self.result_presenter(self.search_parameter, self.search_results)
                self.result_logger(self.search_parameter, self.search_results)                
            elif lookup == "term" or lookup == "Term" or lookup == "t":
                self.search_parameter = input(
                                        "What term do you want to look for?\n>")
                self.value_search(self.search_parameter)
                self.result_presenter(self.search_parameter, self.search_results)
                self.result_logger(self.search_parameter, self.search_results)
            elif lookup == "quit" or lookup == "Quit" or lookup == "q":
                break
            else:
                print("Try again.")
             
# Instantiate the class and begin searching            
start_search = Icd10_search()
start_search.search_term()