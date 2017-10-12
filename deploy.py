# Deploy script for the application
# Deltes old deployed versions in google cloud
def delete_old_deployed_versions():
	print("Deleting old versions")

# Create html files from markdown
def create_html_from_md():
	print("Creating html files from markdown")
	import glob
	from subprocess import call #Used to call pandoc command
	for file_name in glob.iglob("./**/*.md",recursive=True): #Get all the markdown files
		if "index.md" in file_name:
			call(["pandoc",file_name,"--from","markdown_github","--to","html","-s","--highlight-style","tango","--css","/style.css","-o","."+file_name.split(".")[1]+".html"])
		else:
			call(["pandoc","--toc",file_name,"--from","markdown_github","--to","html","-s","--highlight-style","tango","--css","/style.css","-o","."+file_name.split(".")[1]+".html"])

# Deploys the application to goole cloud
def deploy_to_google_cloud():
	print("Deploying to google cloud")
# Starting of the script
if __name__=="__main__":
	print("Deploying the application .... Started")
	delete_old_deployed_versions()
	create_html_from_md()
	deploy_to_google_cloud()
	print("Deploying the application .... End ")
