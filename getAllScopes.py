from tetpyclient import RestClient
import tetpyclient
import requests.packages.urllib3
import argparse
import json
from columnar import columnar



CEND = "\33[0m"
CGREEN = "\33[32m"
CYELLOW = "\33[33m"
CRED = "\33[31m"
URED = "\33[4;31m" 
Cyan = "\33[0;36m"

# =================================================================================
# See reason below -- why verify=False param is used
# python3 getAllScopes.py --url https://asean-tetration.cisco.com/ --credential jonathan_api_credentials.json
# feedback: Le Anh Duc - anhdle@cisco.com
# =================================================================================

requests.packages.urllib3.disable_warnings()


parser = argparse.ArgumentParser(description='Tetration Get all scopes')
parser.add_argument('--url', help='Tetration URL', required=True)
parser.add_argument('--credential', help='Path to Tetration json credential file', required=True)
args = parser.parse_args()


def CreateRestClient():
    rc = RestClient(args.url,
                    credentials_file=args.credential, verify=False)
    return rc

def GetApplicationScopes(rc):
    resp = rc.get('/app_scopes')

    if resp.status_code != 200:
        print("Failed to retrieve app scopes")
        print(resp.status_code)
        print(resp.text)
    else:
        return resp.json()

def GetAppScopeId(scopes,name):
    try:
        return [scope["id"] for scope in scopes if scope["name"] == name][0]
    except:
        print("App Scope {name} not found".format(name=name))        

def ShowScopes(scopes):
    """
        List all the Scopes in Tetration Appliance
        Scope ID | Scope Name | Parent Scope | VRF | Policy Priority
        """
    columns = None
    if columns:
            headers = []
            data_list = []
    else:
        headers = ['Scope ID', 'Name', 'Parent Scope', 'VRF', 'Policy Priority']
        data_list = [[x['id'],
                    x['name'],
                    x['parent_app_scope_id'],
                    x['vrf_id'], x['policy_priority']] for x in scopes ]
    table = columnar(data_list, headers, no_borders=False)
    print(table)

def main():
    rc = CreateRestClient()
    scopes = GetApplicationScopes(rc)
    print (CGREEN + "Here is the all scopes configured in your cluster: " + CEND)
    ShowScopes(scopes)

if __name__ == "__main__":
    main()