# pylint: disable=line-too-long
import argparse
import functools
import json
import sys
import time
import requests

# vRNI is using a self-signed certificate, so ignore any warnings.
requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

class App_Create():
    """Main class which holds the DS and functions required for App and Tier and Token creation"""

    def __init__(self):
        """
        **** Customer needs to set up the below properties before running the script  for first time ****
        self.host : vRNI IP Address
        self.username : username of local account
        self.password : password of local account
        """
        self.verbose = False
        self.delay = 0
        self.host = "10.79.197.111"
        self.username = 'admin@local'
        self.password = 'admin'
        self.token = ''
        self.token_age = 0
        self.app = False
        self.tier = False
        self.app_dict = {}
        self.appmodelkey = ""


    def create_Authtoken(self):
        """
        Creates an Auth Code which would be used for further API calls.
        """

        try:
            response = requests.post("https://{}/api/ni/auth/token".format(self.host),
                                     json={'username': self.username, 'password': self.password,
                                           'domain': {'domain_type': 'LOCAL'}}, verify=False)

            print("\n")
            response_json = response.json()
            if response.status_code != 200 or response_json.get('code'):
                print("Error logging into API")
                print(response_json)
                sys.exit(1)
            self.token = response_json.get('token')
            self.token_age = response_json.get('expiry')
        except requests.exceptions.ConnectionError:
            print("Error connecting to {}, connection refused".format(self.host))
            sys.exit(1)



    def token_check(self):
        """
        Checks if the current token in "self.token"  is still valid. Else create a new one
        which would replace the old one.
        """

        i = self.token_age - time.time() * 1000
        if i <= 200:
            print("Creating New token.\n")
            self.create_Authtoken()
            print("###########################################")
            print(" Active token is :",self.token)
            print("Current Token is active for :",(self.token_age - time.time() * 1000)/60000,"minutes")
            print("###########################################")


    def create_App(self):
        """
        Creates an APP as per the input of user.
        appmodelkey := Contains the internal model key of the application.
        app_dict := It contains the co-relation between application name to appmodelkey
        """


        print("************************* APP WORK-FLOW **************************")
        app_name = input("Input the App Name to create.\n")
        token = "NetworkInsight"+" "+ self.token

        req = requests.post("https://{}/api/ni/groups/applications".format(self.host),
                            headers={'Authorization': token, 'Content-Type': 'application/json'},
                            json={'name': app_name}, verify=False)

        appmodelkey = req.json().get('entity_id')
        self.app_dict[app_name] = appmodelkey
        print("APP MODEL KEY is below, to be used in Tier Creation\n",appmodelkey)
        print("********************************************************************")
        self.main()

    def create_Tier(self):
        """
        Creates a Tier as per the input of user.
        Tier_name and Tier_filter is as per use choice.
        appmodelkey is input by the user which says which application the tier belongs to.
        """

        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@   TIER WORK-FLOW @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        AppID = input("Input the APP MODEL KEY.\n")
        Tier_name = input("Input the Tier Name.\n")
        Tier_filter = input("Input the Tier filter.\n")
        self.appmodelkey = AppID
        appmodelkey = self.appmodelkey
        token = "NetworkInsight" + " " + self.token

        mytierdata = [{ "membership_type": "SearchMembershipCriteria", "search_membership_criteria": {"entity_type": "VirtualMachine", "filter": Tier_filter}}]

        req = requests.post("https://{}/api/ni/groups/applications/{}/tiers".format(self.host, appmodelkey),
                            headers={'Authorization': token, 'Content-Type': 'application/json'},
                            json={'name': Tier_name, 'group_membership_criteria': mytierdata}, verify=False)
        print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
        self.main()




    def main(self):
        """Starting point for the Script """
        targettype = input("Select 1 for App and Select 2 for Tier.\n")


        if targettype == '1':
            self.app = True
            print("You are going to create an App.\n")
            self.token_check()
            self.create_App()


        if targettype == '2':
            self.tier = True
            print("You are going to create a Tier.\n")
            self.token_check()
            self.create_Tier()
        if targettype != '1' and targettype != '2':
            print("Invalid argument, Please input 1 for App or 2 for Tier\n")
            sys.exit(1)



if __name__ == "__main__":
    try:
        App_Create().main()
    except KeyboardInterrupt:
        pass