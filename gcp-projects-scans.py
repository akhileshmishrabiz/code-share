#Before running this script, you'll need to install the google-cloud-resource-manager package and 
# authenticate with a Google Cloud account that has access to your organization. You can find instructions 
# on how to do this in the Google Cloud Client Libraries for Python documentation.

from google.cloud import resource_manager

def list_projects():
    client = resource_manager.Client()

    # List all projects in the organization
    projects = client.list_projects()

    # Iterate through the projects and print their names
    project_list=[]
    for project in projects:
        project_list.append(project.project_id)
    return project_list

if __name__ == "__main__":
    list_projects()
