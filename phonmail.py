# phones\emails extractor by bedroo17
import re


class extractor:
    # put your input text in text
    def __init__(self, text  ): # put your input text in text
        # put your input text in text
        self.text = text
        self.text = self.text.lower()
        self.tro = True
        self.provider = "all"
        self.country_code = "all"
    
    def reg(self):
        # the phone regex :
        if self.country_code == "all":

            self.PhoneRe = re.compile(r'''( 
            #555-555-1234 or 555-1234 or (555)-555-1234 << american numbers examples
            (((\d\d\d) | (\(\d\d\d\)))? # d meaning digit | meaning or ? meaning optional and (meaning group)
            (\s|-)   #seprators \s mean space and - mean - LOL kidding with you bro
            \d\d\d   #first three digits
            -        #another separators
            \d\d\d\d)? #last digits \s means space
            (((\d\d\d) (-)? | \(\d\d\d\) (-)?)?(0?\d{9,12}))? # this is regex for arabs countries code \d{9} short cut for \d\d\d\d\d\d\d\d\d
            )''',re.VERBOSE)
            #VERBOSE for writing commends inside the triple quotations
            # re.compile('((\d\d\d) | (\(\d\d\d\)))?(\s|-)\d\d\d-\d\d\d\d') without verbose mode
        else:
            country = self.country_code
            country = country.replace("+","")
            code_regex = regexer(country)			
            self.PhoneRe = re.compile("{}".format(code_regex))
            

       
        self.EmailRe = re.compile(r''' 
        # anything@anything.anything << emails examples 
        [A-Za-z0-9_.+]+ #name part [create our own regex A-Z all capital letters a-z all small letters _+ some symbols]
        @                # @ symbol
        {} + # domain part the last (+) means must has something after it like .com or .net
        '''.format(self.provider), re.VERBOSE)

    def emails(self,provider = "all",output = "string"):
        self.provider = provider.lower()
        if self.provider == "all":
            self.provider = "[A-Za-z0-9_.+]"
        elif self.provider.isalpha() == False:
            print("provider must be a domain name for specific extracting or 'all' which is the deafult value")
            raise AttributeError
        #self.provider.lower()
        self.provider = self.provider.lower()
        self.reg()
        if  not self.tro:
            return "hi" 
        #self.ExtractedP = self.PhoneRe.findall(self.text) # findall means start collecting the regex
        self.ExtractedE = self.EmailRe.findall(self.text)
        if output == "list":
            return self.ExtractedE
        elif output != "string" and output != "list":
            raise AttributeError
        #print(ExtractedP)
        #find()
        
        #print(EveryPhone)
        # all this to print it in a good format don't be scare
        #self.final = ("phones\n-------------\n"+"\n".join(self.EveryPhone) + "\nemails\n-------------------\n" +"\n".join(self.ExtractedE))
        self.final = ("\n".join(self.ExtractedE))
        self.final = self.final.split()
        self.final = "\n".join(self.final)
        return self.final
    def phones(self,country_code = "all" , output = "string"):
        if output != "string" and output != "list":
            raise AttributeError
        self.country_code = country_code
        self.country_code = self.country_code.lower()
        if self.country_code.isspace() == True:
            print("country_code  must be a country code or name for specific extracting or 'all' which is the deafult value")
            raise AttributeError
        self.reg()
        self.ExtractedP = self.PhoneRe.findall(self.text) # findall means start collecting the regex
        #findall return list of tuples so that why we create this loop try the code without this loop to understand from here
        
        self.EveryPhone = []
        if self.country_code == "all":
            
            for self.phone in self.ExtractedP:
                self.EveryPhone.append(self.phone[0])
            #to here and don't forget to print ExtractedP not EveryPhone
            self.final = ("\n".join(self.EveryPhone))
            self.final = self.final.split()
            self.final = "\n".join(self.final)
            if output == "list":
                return self.final.splitlines()
            return self.final
        elif self.country_code == "1":
            for self.phone in self.ExtractedP:
                self.EveryPhone.append(self.phone[0])
            #to here and don't forget to print ExtractedP not EveryPhone
            self.final = ("\n".join(self.EveryPhone))
            self.final = self.final.split()
            self.final = "\n".join(self.final)
            if output == "list":
                return self.final.splitlines()
            return self.final
        else:
            self.final = ""
            for phone in self.ExtractedP:
                self.final = self.final + phone + "\n"

            self.final = self.final.split("\n")
            self.final = ("\n".join(self.final))
            self.final = "\n".join([ll.rstrip() for ll in self.final.splitlines() if ll.strip()])
            if output == "list":
                return self.final.splitlines()
            return self.final
    def email_counter(self,provider = "all"):
        provider = provider.lower()
        emailes = self.emails(output="list" , provider= provider)
        return len(emailes)
    def phone_counter(self,country_code = "all"):
        self.country_code = country_code.lower()
        emailes = self.phones(output="list" , country_code= self.country_code)
        return len(emailes)    
        
def regexer(code):			
    if code == "1":
        return "(((\d\d\d)|(\(\d\d\d\)))?(\s|-)\d\d\d-\d\d\d\d)?"
    else:
        return  "(\(?" + code + "\)?\s?\-?\d{9,10})?"
