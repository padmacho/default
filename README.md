# default
Default repo contais website artifact
# Deploy the change to google app engine
    gcloud source repos clone default --project=eduami-150711
Above command will clone the repo that is backing up the app.
Go to cloned folder and run below command to deploy

    gcloud app deploy
If the app deployment is sucessful. You can see changes in www.eduami.org
