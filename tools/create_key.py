import datetime
import json
import argparse
import uuid

def create_key(days_to_expire = 1 , roles=['admin'], key_name = 'aapi_key_demo'):
    tomorrow = datetime.date.today() + datetime.timedelta(days=days_to_expire)
    key_definition = {
        'tokenName': key_name,
        'expirationDate':str(tomorrow),
        'roles':roles
    }

    return key_definition
    
def send_request(endpoint, admin_key, key_definition):
    import requests
    import urllib3

    urllib3.disable_warnings() # disable warnings when creating unverified requests 


    r = requests.post(endpoint+'/authentication/token', verify=False, json=key_definition, headers={
        'x-api-key':admin_key,
        'Content-Type':'application/json'
    })

    if r.status_code != 200:
        print('Error creating key')
        print(r.status_code)
        print(r.text)
        print(r.json())
        return None
    else:                
        return r.json()


if __name__ == '__main__':
    parser = argparse.ArgumentParser('create_key')
    default_key_name = 'aapi_key_'+str(uuid.uuid1())    
    parser.add_argument('--name', default=default_key_name)
    parser.add_argument('--lifetime', default=1, type=int)
    parser.add_argument('--roles', default=['admin','user'],nargs='+')
    parser.add_argument('--adminKey', required=True)
    parser.add_argument('--endpoint', required=True)

    args = parser.parse_args()   
    if(args.lifetime < 1):
        args.lifetime = 1 

    key_definition = create_key(args.lifetime, args.roles, args.name)    

    r = send_request(args.endpoint, args.adminKey, key_definition)
    if r:
        print('\n\n')
        print('Api Key created:')
        print('')
        print('Token name: '+args.name)
        print('Token value: '+ r['tokenValue'])
        print('Token valid for '+str(args.lifetime)+' day(s)')

    


    