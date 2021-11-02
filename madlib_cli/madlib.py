import re
def wlcMsg():
    print("""
    *************************************
        Welcome to MAD LIBS® Game


    Try a word puzzle and fill the Blanks

    *************************************    
    """)
wlcMsg()

def read_template(path):
    """ This function read text file and return a stripped string of the file’s contents"""
    try:
     with open(path) as tmpFile:
        fileContent=tmpFile.read().strip()
        print('\n'+fileContent+'\n')
        return fileContent
    except:
        raise FileNotFoundError(f"({path}) was not found ")


def parse_template(str):
    """ This function takes string from the template file and returns astring with removed parts and a list of parts """
    partslist=list(re.findall(r'{(.*?)}',str))
    print(partslist)    
    removedPartsStr=re.sub('{.*?}','{}',str)
    print(removedPartsStr)
   
    return removedPartsStr, partslist

def merge(str,text):
    """This function takes empty template and the user entered parts then mearged it and return the merged string  """
    #print(text)
    mergedStr=str.format(*text)
    print(mergedStr)
    with open('madlib_cli/assets/madlib_template_result.txt','w') as test_result:
        test_result.write(mergedStr)
    return mergedStr

if __name__=="__main__":
    readfile=read_template('madlib_cli/assets/madlib_template.txt')
    text,words=parse_template(readfile)  
    resArr=[]
    for i in words:
        user_entry=input(f"insert{i}>>") 
        resArr.append(user_entry)
        gameres=merge(text,resArr)