'''
Created on Nov 16, 2015

@author: Lex Hokanson
'''
import re
from tkinter import *

# Start the GUI and set variables for widgets
root = Tk()
root.title("ICD10-CM Search")
radio1 = IntVar()
search = StringVar()
search.set("Enter a search term")

class Icd10_search(object):
    '''
    ICD-CM 10 Term/Code search
    '''
    def __init__(self, search_parameter='', search_results=''):
        '''
        Search parameter and search results as attributes.
        Create the codes dictionary from the source file.
        '''
        self.search_parameter = search.get()
        self.search_results = []
        
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
        results_text.insert(END, "Your search parameter: {}".format(
                                                    search_parameter + "\n"))
        print(self.search_results)
        if len(search_results) == 0:
            results_text.insert(END, "There were no results for that search.\n")
        elif len(search_results) == 1:
            results_text.insert(END, "{}".format(search_results[0]))
        else:
            for i in search_results:
                results_text.insert(END,"\n"+"{}".format(i))
            results_text.insert(END, "\n\nSearch found {} results.\n".format(
                                                        len(search_results)))
            
    def result_logger(self):
        '''
        Write to an external file the search parameter and corresponding codes
        '''        
        outfile = open("ICD10SearchResults_" + search.get() + ".txt", 'w')
        outfile.write("Search parameter: {}".format(search.get()) + '\n\n')
        for i in self.search_results:
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
        code_search = re.compile(r'{0}'.format(term_search), 
                                 flags=re.IGNORECASE)
        for k, v in self.icd10_dict.items():
            if code_search.search(v):
                self.search_results.append(k + "\t" + v)
                self.search_results.sort()
    
    def search_term(self):    
        if radio1.get() == 0:
            self.search_parameter = search.get()
            self.value_search(self.search_parameter)
            self.result_presenter(self.search_parameter, self.search_results)             
        elif radio1.get() == 1:
            self.search_parameter = search.get()
            self.key_search(self.search_parameter)
            self.result_presenter(self.search_parameter, self.search_results)
                         
# Instantiate the class           
program = Icd10_search()

# Functions for reset and quit buttons
def resetter():
    results_text.delete(1.0, END)
    search.set("Enter a search term")

def quitter():
    root.destroy()


# Create a Frame with aText widget to display results with a scrollbar
frame = Frame(root)
frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
scrollbar = Scrollbar(frame)
scrollbar.grid(row=0, column=1, sticky=N+S)
results_text = Text(frame, width=120, yscrollcommand=scrollbar.set)
results_text.grid(row=0, column=0, sticky=N+S+E+W)
scrollbar.config(command=results_text.yview)
frame.grid(row=0, column=0, columnspan=5)

# Radio buttons to select whether the user will search by code or term
term_radio = Radiobutton(root, text="Term", variable=radio1, value=0)
term_radio.grid(row=1, column=0)
code_radio = Radiobutton(root, text="Code", variable=radio1, value=1)
code_radio.grid(row=1, column=1)

# Entry widget for search term, will start with text
search_entry = Entry(root, textvar=search)
search_entry.grid(row=2, column=0)

# Buttons to run the query, reset the widgets, save the results or to quit
run_search = Button(root, text="Run", command=program.search_term)
run_search.grid(row=3, column=0)
reset_button = Button(root, text="Reset", command=resetter)
reset_button.grid(row=3, column=1)
save_results = Button(root, text="Save", command=program.result_logger)
save_results.grid(row=3, column=2)
quit_button = Button(root, text="Quit", command=quitter)
quit_button.grid(row=3, column=3)

root.mainloop()