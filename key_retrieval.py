
def get_keys(path):
	# retrieve keys and tokens from private file at <path>
	keys_tokens = open(path, "r")
	lines = keys_tokens.readlines()
	api_key = lines[5]
	api_secret_key = lines[8]
	access_token = lines[14]
	access_token_secret = lines[17]
	return api_key, api_secret_key, access_token, access_token_secret