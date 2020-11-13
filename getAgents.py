from tetpyclient import RestClient
import tetpyclient
import json
import requests.packages.urllib3
import sys
import os
import argparse
import time
import csv
from columnar import columnar
from time import mktime
from datetime import datetime



CEND = "\33[0m"     #End
CGREEN = "\33[32m"  #Information
CYELLOW = "\33[33m" #Request Input
CRED = "\33[31m"    #Error
URED = "\33[4;31m" 
Cyan = "\33[0;36m"  #Return

# =================================================================================
# feedback: Le Anh Duc - anhdle@cisco.com
# See reason below -- why verify=False param is used
# python3 getAgents.py --url https://10.71.129.30 --credential Japan_api_credentials.json
# =================================================================================
requests.packages.urllib3.disable_warnings()


parser = argparse.ArgumentParser(description='Tetration Get all sensors')
parser.add_argument('--url', help='Tetration URL', required=True)
parser.add_argument('--credential', help='Path to Tetration json credential file', required=True)
args = parser.parse_args()


def CreateRestClient():
    rc = RestClient(args.url,
                    credentials_file=args.credential, verify=False)
    return rc

def GetSensors(rc):
    resp = rc.get('/sensors')

    if resp.status_code != 200:
        print(URED + "Failed to retrieve sensors list")
        print(resp.status_code)
        print(resp.text)
    else:
        return resp.json()

def ShowAgents(sensors):
    """
        List all the agents registered in Tetration Appliance
        Hostname | UUID| Agent Type | Last checkin | Install Date | Version | Scopes
        """
    columns = None
    if columns:
            headers = []
            data_list = []
    else:
        headers = ['Host Name', 'UUID', 'Agent Type', 'Last Check-in', 'Install Date', 'Version', 'Scopes']
        data_list = [[x['host_name'], x['uuid'], x['agent_type'], time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(x['last_config_fetch_at'])), time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(x['created_at'])), x['current_sw_version'], ','.join(set([y['vrf'] for y in x['interfaces']])) ]for x in sensors['results'] ]
    table = columnar(data_list, headers, no_borders=False)
    print(table)

def main():
    rc = CreateRestClient()
    sensors = GetSensors(rc)
    print (CGREEN + "Here is the sensors detail: " + CEND)
    ShowAgents(sensors)

if __name__ == "__main__":
    main()