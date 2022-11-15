##########################   Info   ############################################
'''
Name: Bash Command Finder
Author: Patrick Skovgaard (Github: PatrickSkovgaard)
Used for: Bash Command Line, with Python.
'''

##########################   Functionality   ###################################
'''
Find by command name (whole or part) or type(?)
Display info and examples about a command
'''

##########################   Misc   ############################################
'''
Make as a .sh tool?
Make as another extension tool?
'''

##########################   Code   ############################################

def main():
    print("\nBash Command Finder.") 
    print("[Commands are from https://github.com/trinib/Linux-Bash-Commands, with additional ones from myself]") 
                                                                                         #(TODO: right??? ^^)
    print("[This tool is edited and made by me (PatrickSkovgaard on GitHub).]\n")

    print("Description:")
    print("Search by name (part or whole) or type (e.g. network)") 
    print("and get info and examples for the command.\n")

    print("Usage: python bcfind.py [OPTIONS] || [COMMAND-NAME] || [TYPE]\n")

    print("OPTIONS:\n")
    print("Listing commands, tags, types or examples. Only one option allowed:\n" +
          "-lc:         List all bash commands.\n" + 
          "-ltype:      List all types.\n")


    #Like a switch case, just python-style
    match 1: #TODO: find ud af hvordan jeg læser argumenter fra command line
        case "-lc":
            command_list()
        case _:
            print("Couldn't find anything.. check your syntax.")




def command_list():
    
    ''' Commands section '''

    commands = []

    #read all lines in command list document and insert them into an array
    for line in open("Linux-Bash-Commands/command_list.txt", "r", errors="ignore", newline=None).readlines():
        commands.append(line)

    #remove newline character from elements
    for i in range(len(commands)):
        if str(commands[i]).endswith("\n"):
            commands[i] = str(commands[i]).split("\n")[0]


    #Better way of printing a readable list of commands, each on their own line
    for command in commands:
        print(command)



main()
#command_list()
