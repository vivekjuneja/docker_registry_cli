import json
import requests
import sys

''' Disable Warnings when using verify=False'''
requests.packages.urllib3.disable_warnings()

def get_reqistry_request(url, auth=False, username=None, password=None, ssl=False):


	if ssl==True:
		proto="https://"
	else:
		proto="http://"

	url_endpoint = proto + url

	if auth==False:
		req = requests.get(url_endpoint)
	else:	
		s = requests.Session()
		s.auth = (username, password)
		req = s.get(url_endpoint, verify=False)

	return req



def get_registry_catalog_request(url, auth=False, username=None, password=None, ssl=False):

	requrl = url+"/v2/_catalog"

	req = get_reqistry_request(requrl, auth, username, password, ssl)
	
	return req


def get_registry_tag_request(url, repo, auth=False, username=None, password=None, ssl=False):
	
	requrl = url + "/v2/" + repo  + "/tags/list"

	req = get_reqistry_request(requrl, auth, username, password, ssl)

	return req


def extract_url(url, auth):
	if auth==False:
		return None, None, url
	else:
		uname_pwd_delimeter=":"
		delimiter_uname_pwd_pos = url.find(uname_pwd_delimeter)
		auth_ip_delimeter="@"
		delimeter_auth_ip_pos = url.find(auth_ip_delimeter)
		username = url[:delimiter_uname_pwd_pos]
		password = url[delimiter_uname_pwd_pos+1:delimeter_auth_ip_pos]
		url_endpoint = url[delimeter_auth_ip_pos+1:]

		
		return username, password, url_endpoint


def get_all_repos(url, auth=False, ssl=False):
	
	username, password, url_endpoint = extract_url(url, auth)

	req = get_registry_catalog_request(url_endpoint, auth, username, password, ssl)

	parsed_json = json.loads(req.text)

	repo_array = parsed_json['repositories']

	return repo_array



def search_for_repo(url, repo_search_name, auth=False, ssl=False) :

	repo_array = get_all_repos(url, auth, ssl);
	
	repo_dict_search = {}

	if repo_search_name in repo_array:
		parsed_repo_tag_req_resp = get_tags_for_repo(url, repo_search_name, auth, ssl)
		repo_dict_search[repo_search_name] = parsed_repo_tag_req_resp
	else:
		''' Get all the repos '''
		repo_dict = get_all_repo_dict(url, repo_array, auth, ssl) 

		if any(False if key.find(repo_search_name)==-1 else True for key in repo_dict) ==  True:
			print "available options:- " 
			for key in repo_dict:
				if(key.find(repo_search_name)!=-1):
					repo_dict_search[key] = get_tags_for_repo(url, key, auth, ssl)

					
	return repo_dict_search


def get_tags_for_repo(url, repo, auth=False, ssl=False):
	
	username, password, url_endpoint = extract_url(url, auth)

	repo_tag_url_req = get_registry_tag_request(url_endpoint, repo, auth, username, password, ssl)


	parsed_repo_tag_req_resp = json.loads(repo_tag_url_req.text)
	
	return parsed_repo_tag_req_resp["tags"]


'''
Gets the entire repository dictionary
'''
def get_all_repo_dict(url, repo_array, auth=False, ssl=False):
	repo_dict = {}
	for repo in repo_array:
 		parsed_repo_tag_req_resp = get_tags_for_repo(url, repo, auth, ssl)
 		repo_dict[repo] = parsed_repo_tag_req_resp

 	return repo_dict


'''
Decorates the search results to be printed on the screen
'''
def decorate_list(repo_dict):
	decorated_list_values = ""
 	
	if(len(repo_dict)==0):
		return "No results!"
		
	counter = 1;
 	for repo_key in repo_dict:
 		decorated_list_values +=  "\n-----------" + "\n" + str(counter) + ") Name: " + repo_key
 		decorated_list_values += "\nTags: "
 		counter+=1;
 		for tag in repo_dict[repo_key]:
 			decorated_list_values += tag + '\t'
 	
 	decorated_list_values += "\n\n" + str(counter-1) + " images found !"
 	return decorated_list_values


def usage():
 	return "Usage: browser.py <registry_endpoint> <keyword> <value> <option1> <option2>\
 	\nValid keywords : search, list \
 	\nValid values:- \
 	\nFor keyword search, use the value as the image name. For eg:- search redis\
 	\nFor keyword list, use the value 'all' without quotes to get a list of all the docker image repos. For eg:- list all\
 	\nYou can specify the option1 as 'auth' to allow username and password to be used for authenticating the docker registry. \
 	\nFor eg:- python browser.py uname:pwd@registry_endpoint:port search busybox auth\
 	\nIf you use SSL, then specify the option2 as 'ssl' and option1 as 'auth' to allow for SSL Authentication\
 	\nFor eg:- python browser.py uname:pwd@registry_endpoint:port search busybox auth ssl\
 	\nFor more information, visit:- https://github.com/vivekjuneja/docker_registry_cli/"



if __name__ == "__main__":
	len_sys_argv = len(sys.argv[1:])


	if len_sys_argv < 3:
		print usage()

	elif len_sys_argv >= 3:
		
		regurl = sys.argv[1:][0]
		keyword = sys.argv[1:][1]
		repo_to_search = sys.argv[1:][2]
		auth_flag =False
		ssl_flag  = False

		if len_sys_argv == 3:	
			auth_flag = False
		elif len_sys_argv == 4:	
			auth = sys.argv[1:][3]
			if auth == "auth":
				auth_flag = True
			ssl = False
		elif len_sys_argv == 5: 
			auth = sys.argv[1:][3]
			ssl = sys.argv[1:][4]
			if auth=="auth":
				auth_flag = True
			if ssl=="ssl":
				ssl_flag = True
	

		search_results = None

		if keyword=="search":
			search_results = search_for_repo(regurl, repo_to_search, auth_flag, ssl_flag)
		elif keyword=="list":
			all_repos = get_all_repos(regurl, auth_flag, ssl_flag)
			search_results = get_all_repo_dict(regurl, all_repos, auth_flag, ssl_flag)
		else:
			print usage()
			sys.exit(1)

		print decorate_list(search_results)


