from subprocess import call  # Used to call pandoc command


# Deploy script for the application
# Deletes old deployed versions in google cloud
def delete_old_deployed_versions():
    print("Deleting old versions")


def update_anchor_elements_in_index_file(index_file):
    # Read index.html file
    with open(index_file, 'r') as myfile:
        data = myfile.read()

    # Read all the anchor element hrefs and set them as name attribute to anchor tag
    from bs4 import BeautifulSoup
    soup = BeautifulSoup(data, "html.parser")
    # Fill all the anchor elements in html file
    for anchor in soup.find_all('a'):
        href = anchor["href"]
        # if it is not index.html anchor element, add name attribute
        if "index" not in href:
            anchor["name"] = href.split(".")[0]

    # Update the index.html file
    with open(index_file, 'w') as the_file:
        the_file.write(str(soup))


# Create html files from markdown
def create_html_from_md():
    print("Creating html files from markdown")
    import glob
    # Update anchor links in article.md and index.md
    for file_name in glob.iglob("./**/*.md", recursive=True):  # Get all the markdown files
        if "index.md" in file_name or "Article.md" in file_name:
            call(["pandoc", file_name, "--from", "markdown_github", "--to", "html", "-s", "--highlight-style", "tango",
                  "--css", "/style.css", "-o", "." + file_name.split(".")[1] + ".html"])
            update_anchor_elements_in_index_file("./" + file_name.split(".")[1] + ".html")
        else:
            call(["pandoc", "--toc", file_name, "--from", "markdown_github", "--to", "html", "-s", "--highlight-style",
                  "tango", "--css", "/style.css", "-o", "." + file_name.split(".")[1] + ".html"])


# Deploys the application to goole cloud
def deploy_to_google_cloud():
    print("Deploying to google cloud")


# call(["gcloud","--quiet","app","deploy"])
# Starting of the script
if __name__ == "__main__":
    print("Deploying the application .... Started")
    delete_old_deployed_versions()
    create_html_from_md()
    deploy_to_google_cloud()
    print("Deploying the application .... End ")
