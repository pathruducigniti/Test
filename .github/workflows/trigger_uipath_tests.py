import requests

def get_api_key(client_id, user_key, tenant_name):
    token_url = "https://account.uipath.com/oauth/token"

    headers = {
        "Content-Type": "application/json",
        "X-UIPATH-TenantName": tenant_name
    }

    data = {
        "grant_type": "refresh_token",
        "client_id": client_id,
        "refresh_token": user_key
    }

    response = requests.post(token_url, json=data, headers=headers)
    if response.status_code == 200:
        return response.json()["access_token"]
    else:
        print("Failed to retrieve API key.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)
        return None

def trigger_uipath_tests(api_key, org_id, test_set_key, account_name, tenant_name):
    url = "https://cloud.uipath.com/"+account_name+"/"+tenant_name+"/orchestrator_/api/TestAutomation/StartTestSetExecution?testSetKey="+test_set_key+"&triggerType=ExternalTool"

    payload = {}
    headers = {
      'X-UIPATH-OrganizationUnitId': org_id,
      'Authorization': 'Bearer '+api_key,
      }

    response = requests.request("POST", url, headers=headers, data=payload)
    if response.status_code == 200:
        print("Test set triggered successfully.")
    else:
        print("Failed to trigger test set.")
        print("Status Code:", response.status_code)
        print("Response:", response.text)

if __name__ == "__main__":
    client_id = "8DEv1AMNXczW3y4U15LL3jYf62jK93n5"
    user_key = "MM9NONPjVVOtAAdbBmkHZ79CVOZQ3hLIEd6hTaol7A_sx"
    org_id = "2005055"  # Add your Folder ID here
    test_set_key = "4f7cd455-6598-4e17-8f8a-bacce81934ac"
    tenant_name = "CignitiTechnologiesLtdDefault"
    account_name = "cigniti_rpa_coe"
    api_key = get_api_key(client_id, user_key, tenant_name)
    if api_key:
        trigger_uipath_tests(api_key, org_id, test_set_key, account_name, tenant_name)
