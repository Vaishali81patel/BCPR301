# Written By Thomas
#
# This is the main file. The dependency injection is handled from here
# and the cmdloop is started.



from controller import Controller
from View.graph_view import *
from Model.interconnect import *
from Model.EmpFileHandler.file_handler import *
from Model.Check_Empdata.data_validator import *
from Model.EmpDatabase.database import *
import sys


if __name__ == '__main__':
    Controller(GraphView(), Interconnector(
                            Cehck_Empdata(),
                            Emp_File_Handler(),
                            Emp_Database(),
                            Controller.file_path_check_set(sys.argv)
                            )
                          ).cmdloop()
