#!/usr/bin/python3

def clean_docker():
    import os,re,requests
    try:
        os.environ["JFROGUSERNAME"]
    except KeyError:
        print ("Error: please set the environment variable JFROGUSERNAME")
        sys.exit(1)
    try:
        os.environ["JFROGPASSWORD"]
    except KeyError:
        print ("Error: please set the environment variable JFROGPASSWORD")
        sys.exit(1)
    try:
        os.environ["JFROGLIMIT"]
    except KeyError:
        print ("Error: please set the environment variable JFROGLIMIT")
        sys.exit(1)

    jfrogusername=os.environ['JFROGUSERNAME']
    jfrogpassword=os.environ['JFROGPASSWORD']
    jfroglimit=os.environ['JFROGLIMIT']
    base_url = 'https://stellaromada-stellar-docker.jfrog.io/artifactory/'
    headers = {
        'content-type': 'text/plain',
    }
    data = 'items.find({"name":{"$eq":"manifest.json"},"stat.downloaded":{"$before":'+jfroglimit+'}})'
    myResp = requests.post(base_url+'api/search/aql', auth=(jfrogusername, jfrogpassword), headers=headers, data=data)
    for result in eval(myResp.text)["results"]:
        artifact_url = base_url+ result['repo'] + '/' + result['path']
        if not re.search("latest$",artifact_url):
            print(artifact_url)
            requests.delete(artifact_url, auth=(jfrogusername, jfrogpassword))

if __name__ == '__main__':
    clean_docker()
