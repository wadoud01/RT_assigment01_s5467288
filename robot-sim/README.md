Assignment N°01
================================
Name : Abdelouadoud Guelmami
ID: S5467288


In robot.som file you may find :
1)README.md : it contains all the information needed considering the code, flowchatrs, and analysing in general.

2)assignment.py : it contains the whole code of the assigmnet, the code was writting in Python form.

3)main flowchart.png: it's a diagram that represents our code using flowcharts, also it's needed to mention it's simplfied and composed of other 2 two functions inside that also are represented in other flowchart diagram. (PNG form)

4)Track_silver flowchart.png : it's an diagram that represents our code using flowcharts of Track_silver() function (the function used to grab the silver boxs). (PNG form)

5)Track_golden flowchart.png:it's an diagram that represents our code using flowcharts of Track_golden() function (the function used to grab the golden boxs). (PNG form)

note: The flowchart got seperated in order to make it less complex and more simplified


Code
----------------------
There are 3 parts : Main functions, Track_silver(), Track_golden()

1)Main funciton : Is made by "for" loop (6 repetitions because there are 6 silver boxes), It starts the function "Track_silver()" which starts tracking the silver box, the when it finshes it executs the function "Track_golden()" to grab new golden box. after six times it prints that the mission is completed.

2)Track_silver(): this fuction is used to grab the silver box. using while loop and if statements. 
-we used some variable in order to control the following:
-Var = 0 or 1 : var is used to quit the while loops, if the the var is 0 is exits the tracki_silver function.
-List_silver: the list is used in order to register the ID of the silver box in order to avoid being repeated.


3)Track_golden(): this fuction is used to grab the silver box. using while loop and if statements.
-we used some variable in order to control the following:
-Var = 0 or 1 : var is used to quit the while loops, if it's 1 it exits the track_golden fuction
-List_gold: the list is used in order to register the ID of the silver box in order to avoid being repeated.

Analysing the code 
--------------------
The benifits:
1) the code does the requirements succussfully.
2) The main function is short and contains only few lines.
3) the code is well organized.

The disadvatages:
1) only it brings the nearest box in R.see(), which means if there is other close box not in R.see() it won't be detected.
