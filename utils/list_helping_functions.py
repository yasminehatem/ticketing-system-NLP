# -*- coding: utf-8 -*-
# + {}

def read_list(filename):
    saved_processed_data=[]
    with open(filename, 'r') as filehandle:
        for line in filehandle:
            # remove linebreak which is the last character of the string
            currentPlace = line[:-1]

            # add item to the list
            saved_processed_data.append(currentPlace)
    return saved_processed_data  
#DON't RUN THE LIST IS ALREADY PROCESSES
def write_list(list_,filename):
    with open(filename, 'w') as f:
        for item in list_ :
            f.write("%s\n" % item)
#RUN TO GET THE PROCESSED LIST

