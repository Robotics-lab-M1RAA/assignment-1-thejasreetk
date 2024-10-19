### Robotics lab - Assignment completion & submission instructions
### --------------------------------------------------------------

1. Install git commandline on your Ubuntu OS (follow the steps in the link shared earlier)

2. Accept the assigment using the GitHub classroom assignment link (share in the class whatsapp group)

3. Clone the assignment from the remote git repo (ie, the one in the GitHub classroom) to your PC \
Use ```git clone``` command for this

4. Do the assignment on your PC / lab PC

5. You can push the partially completed assignment to the remote git

(please note that i have renamed the folder as JIM-CET; your assignment folder would have your name)

6. Once the assignment is completed push it to the remote repo on or before the due time.

#### Steps to push local repo (ie the files on your PC) to remote repo (ie the one on the GitHub)

1. **Staging :** Go to the local repo folder and launch a terminal or navigate to local repo via terminal
use ```git add .``` \      
#### note the space after add  the '.' after add ; this caches (or adds) all the files in the local repo. \
This process is known as staging 

2. Staged files are files that are ready to be committed to the repository you are working on. \

if you want to clear current git cache \
for example you didn't want to include some/all files in the current commit

```git rm -r --cached . ```      # don't forget the dot (.)

if want to remove any particular folder or file then use \

```git rm  --cached filepath/foldername```

3. **Commit :** With ```git commit``` command you commit to the remote repo \
It is always good to include a message in double quotes to identify the commit 

```git commit -m "commit-message"```
For example ```git commit -m "assign1-half-complete"```

4. **Push changes to GitHub**
So far we have only modified our local copy of the repository. The push term refers to upload local repository content to a remote repository. 
Pushing is an act of transfer commits from your local repository to a remote repository. Pushing is capable of overwriting changes; caution should be taken when pushing.

```git push```
You would be asked to enter your user name and personal access token 
## Personal access tokens are an alternative to using passwords for 
## authentication to GitHub when using the GitHub API or the command line.
### [follow this link to create a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens#creating-a-personal-access-token-classic) 


