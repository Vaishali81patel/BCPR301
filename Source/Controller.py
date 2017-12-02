# Written By Vaishali
    # This is the controller for this system which
    # ensure what is happening in the Cmdloop and associated command with it
    # It also interact with Model and GraphView

from cmd import Cmd


class Controller(Cmd):


    def __init__(self, in_view, in_interconnector):
        # Written By Vaishali
        #
        # The Controller object is connected Interconnected and View object
        # and is assigned to the respective attribute in the controller object.
        #
        Cmd.__init__(self)
        self.prompt = '> '
        self.my_view = in_view
        self.my_interconnector = in_interconnector

    @staticmethod
    def file_path_check_set(running_args):
        # Written By Vaishali
        #
        # This is the part of the system that allows for command line arguments.
        # The functionality provided here is the user is able to supply a default
        # path to where they would like to store their files when they are saved.
        #
        # It is handled by taking the sys.argsv then checking if there
        # was only one string provided. then it checks if the path is accessible.
        #
        # If it is the default is set. otherwise it defaults to the main and
        # continues working.
        #

        if len(running_args) > 2:
            print("TOO MANY ARGUMENTS SUPPLIED!")
            return running_args[0]
        try:
            open(running_args[1], 'r')
            return running_args[1]
        except OSError as error:
            print(error)
            print("DEFAULT WORKING DIRECTORY!.")
            return running_args[0]
        except IndexError:
            print("NO DEFAULT PATH PROVIDED!.")
            print("DEFAULT WORKING DIRECTORY.")
            return running_args[0]

    def do_add(self, *args):
        # Vaishali
        """
        ***
        OPTIONS
            -l : This loads the information from a file. The file is given to the command as a string.
            -m : This is for manual data entry. The user will be prompted for the information in steps after entering this option.
            -d : This loads the information into the system from a database.
        ***
        """

        options_arr = self.parse_args(args)
        option_direct = {
            '-l': self.my_interconnector.load_file,
            '-m': self.manual_add,
            '-d': self.my_interconnector.load_database
        }
        self.find_in_dict(options_arr, option_direct)

    def do_save(self, *args):
        #Vaishali
        """
        ***
        OPTIONS
            -s : This is a standard save. The information is saved to a file in the saves folder in the program files. (object is serialized)
            -d : This saves the current information to the database.
            -f : This saves a file to the specified file location.
        ***
        """
        options_arr = self.parse_args(args)
        option_direct = {
            '-f': self.my_interconnector.save_file,
            '-d': self.my_interconnector.save_database,
            '-s': self.my_interconnector.serialize_empdata_arr
        }
        self.find_in_dict(options_arr, option_direct)

    def do_show(self, *args):
        # Vaishali
        """
        ***
        OPTIONS
            -a : Shows a bar graph of the total sales made by males verse the total sales made by female.
            -b : Shows a pie chart of the percentage of female workers verse male workers
            -c : Shows a scatter plot graph of peoples age verse their salary.
            -d : Shows a pie chart of the BMI of a set of people.
        ***
        """
        options_arr = self.parse_args(args)
        option_direct = {
            '-a': self.my_view.sales_by_gender_graph,
            '-b': self.my_view.employees_by_gender_graph,
            '-c': self.my_view.age_verse_salary_graph,
            '-d': self.my_view.bmi_pie_graph
        }
        for key, value in option_direct.items():
            if options_arr[0] == key:
                value(self.my_interconnector.get_data())

    @staticmethod
    def do_quit(arg):
        # Closes the program
        # If quit is typed into the cmd. it quits.
        quit()

    # Another way to the quit.
    do_q = do_quit

    @staticmethod
    def parse_args(arg_str):
        #
        # This method takes a argument string which is a string of options
        # given to the interconnect after a command has been invoked. It
        # then splits this string up every time it finds a blank space.
        #
        # The resulting array is then returned to the calling function.
        #
        #
        try:
            arg_arr = None
            for arg in arg_str:
                arg_arr = arg.split(' ')
            if len(arg_arr) > 2:
                return "Too many arguments were given"
            else:
                return arg_arr
        except IndexError:
            return False

    def manual_add(self):
        #
        # This simply invokes the manual data entry flow in the
        # view then passes that information into the add manual
        # data in the model.
        #
        #
        self.my_interconnector.add_manual_data(self.my_view.manual_person_flow())

    def find_in_dict(self, options_arr, options_direct):
        # When a matching is found the try_launch method is called
        # which launches the value at the corresponding matched key.
        #
        #
        arg_found = False
        for key, value in options_direct.items():
            if options_arr[0] == key:
                if not self.try_to_launch(key, value, options_arr):
                    return
                else:
                    return
        if not arg_found:
            return

    @staticmethod
    def try_to_launch(key, value, options_arr):
        # Written By Thomas
        #
        # Is given a matched option and key value pair.
        # The key is checked to make sure it isnt -m because
        # this acts differntly. if it is the value is ran on its own.
        #
        # if it isnt the options array needs to have exactly 2 items
        # otherwise it will fail if it has 2 item the value is ran.
        #
        if key == '-m':
            value()
            return True
        else:
            if len(options_arr) == 2:
                value(options_arr[1])
                return True
            else:
                return False
