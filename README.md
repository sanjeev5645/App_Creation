# App_Creation


****** How to use the script   ******

STEP 1.

Install python in your machine. ( latest 3.x  preferred )                       
Windows: -  https://www.digitalocean.com/community/tutorials/install-python-windows-10
Linux: -  https://www.scaler.com/topics/python/install-python-on-linux/
 
Feel free to use any online resource to complete this step.



STEP 2.

Install the required libraries in the python environment that was setup in Step 1.
Steps: https://packaging.python.org/en/latest/tutorials/installing-packages/ 

Follow “Installing from PyPI” option. This is the simplest option. 

Libraries/projects to install are
argparse
functools
json
sys
time
re
requests


STEP 3.

Set up the python script & execute it.    
Download/Clone the App creation code from the GitHub repository.
https://github.com/sanjeev5645/App_Creation.git


Ubuntu Machine ( used for demo )

ankita@ankita:/tmp/DIR$ git clone https://github.com/sanjeev5645/App_Creation.git
Cloning into 'App_Creation'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0
Unpacking objects: 100% (3/3), 2.27 KiB | 580.00 KiB/s, done.
ankita@ankita:/tmp/DIR$ ls
App_Creation
ankita@ankita:/tmp/DIR$ cd App_Creation/
ankita@ankita:/tmp/DIR/App_Creation$ ls
app_creation.py
ankita@ankita:/tmp/DIR/App_Creation$ ls -l
total 8
-rw-rw-r-- 1 ankita ankita 5572 Sep 28 18:39 app_creation.py
ankita@ankita:/tmp/DIR/App_Creation$ chmod 744 app_creation.py
ankita@ankita:/tmp/DIR/App_Creation$ ls
app_creation.py
ankita@ankita:/tmp/DIR/App_Creation$
ankita@ankita:/tmp/DIR/App_Creation$
ankita@ankita:/tmp/DIR/App_Creation$
ankita@ankita:/tmp/DIR/App_Creation$ python3 app_creation.py
Select 1 for App and Select 2 for Tier.
1
You are going to create an App.

Creating New token.



##############
 Active token is : H1O3SyYroAAt5+wycwtZrA==
Current Token is active for : 299.9986484008789 minutes
##############
********* APP WORK-FLOW *******
Input the App Name to create.
App10
APP MODEL KEY is below, to be used in Tier Creation
 10000:561:6650020740672764927
**********************
Select 1 for App and Select 2 for Tier.
2
You are going to create a Tier.

@@@@@@@@ TIER WORK-FLOW @@@@@@@@@
Input the APP MODEL KEY.
10000:561:6650020740672764927
Input the Tier Name.
T1
Input the Tier filter.
Name like TEST**
@@@@@@@@@@@@@@@@@@@@@@
Select 1 for App and Select 2 for Tier.
6
Invalid argument, Please input 1 for App or 2 for Tier


STEP 4.	Script Workflow and the options. 

The script works in a loop when you select option 1 or 2 ( depending on the action you want to perform ).  Select any other keystroke and you will exit the program.

**********   Workflow  **********

/Users/sathishs/PycharmProjects/App_Creation/venv/bin/python /Users/sathishs/PycharmProjects/App_Creation/app_creation.py 
Select 1 for App and Select 2 for Tier
1
You are going to create an App.
 
Creating a New token.
 
 
 
#################
 
 Active token is : dCt36jqtEMACr6kBfIewmg==
Current Token is active for : 300 minutes
##################
 
****** APP WORK-FLOW *****
Input the App Name to create.
APP1
APP MODEL KEY
 10000:561:1817094528323472647
********************
Select 1 for App and Select 2 for Tier
2
You are going to create a Tier.
 
@@@@@@@@  TIER WORK-FLOW @@@@@@@
Input the APP MODEL KEY.
10000:561:1817094528323472647
Input the Tier Name.
T1
Input the Tier filter.
Name like work**
@@@@@@@@@@@@@@@@@@@@@@@
Select 1 for App and Select 2 for Tier.
2
You are going to create an Tier.
 
@@@@@@@ TIER WORK-FLOW @@@@@@@@@
Input the APP MODEL KEY.
10000:561:1817094528323472647
Input the Tier Name.
T2
Input the Tier filter.
Name like UB**
@@@@@@@@@@@@@@@@@@@@@@@@@@
Select 1 for App and Select 2 for Tier.
1
You are going to create an App.
 
****** APP WORK-FLOW ********
Input the App Name to create
App2
APP MODEL KEY
 10000:561:6693327657838766034
**************************
Select 1 for App and Select 2 for Tier
2
You are going to create a Tier.
 
@@@@@@@@@TIER WORK-FLOW @@@@@@@@
Input the APP MODEL KEY.
10000:561:6693327657838766034
Input the Tier Name
T1
Input the Tier filter
Name like woker**
@@@@@@@@@@@@@@@@@@@@@@@@@
Select 1 for App and Select 2 for Tier.
2
You are going to create a Tier.
 
@@@@@@@@@@ TIER WORK-FLOW @@@@@@@@
Input the APP MODEL KEY.
10000:561:6693327657838766034
Input the Tier Name.
T2
Input the Tier filter.
Name like UB**
@@@@@@@@@@@@@@@@@@@@@@@@@@
Select 1 for App and Select 2 for Tier.
1
You are going to create an App.
 
****** APP WORK-FLOW *******
Input the App Name to create.
App3
APP MODEL KEY
 10000:561:2514963798579868199
***********************
Select 1 for App and Select 2 for Tier
2
You are going to create a Tier.
 
@@@@@@@@ TIER WORK-FLOW @@@@@@@@@@
Input the APP MODEL KEY.
10000:561:1817094528323472647
Input the Tier Name.
T3
Input the Tier filter.
Name like TEST**
@@@@@@@@@@@@@@@@@@@@@@@@@@
Select 1 for App and Select 2 for Tier.
1
You are going to create an App.
 
****** APP WORK-FLOW ********
Input the App Name to create.
App4
APP MODEL KEY
 10000:561:7842716976004605665
***************************
Select 1 for App and Select 2 for Tier.
2
You are going to create a Tier.
 
@@@@@@@@ TIER WORK-FLOW @@@@@@@@
Input the APP MODEL KEY.
10000:561:7842716976004605665
Input the Tier Name.
T1
Input the Tier filter.
Name like UB**
@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
Select 1 for App and Select 2 for Tier.
2
You are going to create a Tier.
 
@@@@@@@@@@ TIER WORK-FLOW @@@@@@@
Input the APP MODEL KEY.
10000:561:1817094528323472647
Input the Tier Name.
T5
Input the Tier filter.
Name like UB**
@@@@@@@@@@@@@@@@@@@@@@@@@@
Select 1 for App and Select 2 for Tier.
6
Invalid argument, Please input 1 for App or 2 for Tier





$$$$$$$$ END  $$$$$$$$$






