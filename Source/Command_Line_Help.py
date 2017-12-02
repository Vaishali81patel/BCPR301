# The module defines only one class: the Cmd class. Creating a command line interpreter is
# done by sub-classing the cmd.Cmd class.

from cmd import Cmd
import string, sys
import os

class HelpComm(Cmd):

    def __init__(self):
        Cmd.__init__(self)
        self.prompt = ">>> "
        self.intro  = "WELCOME TO THE CONSOLE!!!!"  ## defaults to None

    # Command definitions
    def do_list(self, args):
        """Print a list of commands that have been entered"""
        print ("self._list")

    def do_Exit(self, args):
        """Exits from the console"""
        return -1

    # Command definitions to support Cmd object functionality
    def do_EOF(self, args):
        """Exit on system end of file character"""
        return self.do_Exit(args)

    def do_shell(self, args):
        """Pass command to a system shell when line begins with '!'"""
        os.system(args)

    # Get help for add command
    def do_help(self, args):
        """Get help on commands
           'help' or '?' with no arguments prints a list of commands for which help is available
           'help <command>' or '? <command>' gives help on <command>
        """
        # The only reason to define this method is for the help text in the doc string
        Cmd.do_help(self, args)

    # add command opetions
    def help_add(self):
        print ("""*** OPTIONS
            -l : This loads the information from a file. The file is given to the command as a string.
            -m : This is for manual data entry. The user will be prompted for the information in steps after entering this option.
            -d : This loads the information into the system from a database.  ***""")

    # save command options
    def help_save(self):
        print ("""***     OPTIONS     
                -s : This is a standard save. The information is saved to a file in the saves folder in the program files. (object is serialized)
                -d : This saves the current information to the database.
                -f : This saves a file to the specified file location.    ***""")

    # show command options
    def help_show(self):
        print("""*** OPTIONS
            -a : Shows a bar graph of the total sales made by males verse the total sales made by female.
            -b : Shows a pie chart of the percentage of female workers verse male workers
            -c : Shows a scatter plot graph of peoples age verse their salary.
            -d : Shows a pie chart of the BMI of a set of people.   ***""")


    def do_add(self,s):
        print ('This command adds the employee data to the system. ')

    def do_save(self,s):
        print ('This command saves the current employee data.')

    def do_show(self,s):
        print ('This displays the current working information in a given manner.')


if __name__ == "__main__":
    helpcommand = HelpComm()
    helpcommand.cmdloop()
