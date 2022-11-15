
from fulltimeemployee import FulltimeEmployee
from  hourlybaseemployee import  HourlybaseEmployee
from  payrol import  Payrol

payrol = Payrol()

payrol.add(FulltimeEmployee("sumilon ","biswas",20000))
payrol.add(FulltimeEmployee("anik ","Rahman",25000))
payrol.add(FulltimeEmployee("Ripon ","sarker",23000))
payrol.add(HourlybaseEmployee("anika ","Rehman",230,120))
payrol.add(HourlybaseEmployee("jion","Root",200,150))
payrol.add(HourlybaseEmployee("shipon","melor",150,250))

payrol.printed()