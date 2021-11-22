import json

def get_json_for_folder(self, folder_name):

    res = self.deployApi.get_deployed_folders_new(server="*", folder=folder_name)
    return json.loads(res.replace("'", '"'))