
from  fulltimemployee import FullTimeemployee
from hoursbaseEmployee import HoursBaseEmployee
from  Daybaseworker import  Day_base_worker

from  payrol import Payrol

payrol=Payrol()

print("full time employee information display ")
payrol.add(FullTimeemployee("john","Aus","john@gmail.com",20000))
payrol.add(FullTimeemployee("Rohan","india","Rohan@gmaiol.com",32000))
# payrol.printed()
print("\n")

print("hourlybaseemployee information show ")
payrol.add(HoursBaseEmployee("meria noor","Irain","meria@gmail.com",240,100))
payrol.add(HoursBaseEmployee("nurie Rahman","nederland","nurie@gmail.com",230,120))
# payrol.printed()
print("\n")

print("day base employee result show")

payrol.add(Day_base_worker("sumilon","Bangladesh","sumilon@gmail.com",450,15))
payrol.add(Day_base_worker("joya bain","Bangladesh","joya@gmail.com",350,20))
payrol.add((Day_base_worker("Tanbir islam","Bangladesh","tanbir@gmail.com",400,20)))
payrol.printed()
print("\n")
