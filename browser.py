import json
import requests
import sys

def get_all_repos(url):
	req = requests.get("http://" + url+"/v2/_catalog")

	parsed_json = json.loads(req.text)

	repo_array = parsed_json['repositories']

	return repo_array

def search_for_repo(url, repo_search_name) :

	is_repo_full_name_found = True;

	repo_array = get_all_repos(url);

	if repo_search_name in repo_array:
		parsed_repo_tag_req_resp = get_tags_for_repo(url, repo_search_name)
		print parsed_repo_tag_req_resp
	else:
		''' Get all the repos '''
		repo_dict = get_all_repo_dict(url, repo_array) 
		if any(key.startswith(repo_search_name) for key in repo_dict) ==  True:
			print "available options:- " 
			for key in repo_dict:
				if(key.startswith(repo_search_name)):
					print key + " : " + str(get_tags_for_repo(url, key))

		'''print repo_search_name + " not available "
		is_repo_full_name_found = False;'''


def get_tags_for_repo(url, repo):
	repo_tags_url = "http://" + url + "/v2/" + repo  + "/tags/list"

	repo_tag_url_req = requests.get(repo_tags_url)
	parsed_repo_tag_req_resp = json.loads(repo_tag_url_req.text)
	return parsed_repo_tag_req_resp["tags"]
	
def get_all_repo_dict(url, repo_array):
	repo_dict = {}
	for repo in repo_array:
 		parsed_repo_tag_req_resp = get_tags_for_repo(url, repo)
 		repo_dict[repo] = parsed_repo_tag_req_resp

 	return repo_dict

if __name__ == "__main__":
	len_sys_argv = len(sys.argv[1:])

	if len_sys_argv < 3:
		print "Usage: browser.py <registry_endpoint> <keyword> <values> \n valid keywords : search, list, gettag"
	elif len_sys_argv == 3:
		regurl = sys.argv[1:][0]
		keyword = sys.argv[1:][1]
		repo_to_search = sys.argv[1:][2]
		if keyword=="search":
			search_for_repo(regurl, repo_to_search)
		elif keyword=="list":
			get_all_repo_dict(regurl, get_all_repos(regurl))
		else:
			print "Usage: browser.py <registry_endpoint> <keyword> <values> \n valid keywords : search, list, gettag"


