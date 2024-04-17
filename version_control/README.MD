#Create a Folder containing all the Files you want to Version controll 

# use the (Git init) command to initialize git into the folder

# add README.md Files to all subdirectories so the subfolders can be recognized by git 

# add these both commands to authenticate to git : git config --global userName & git config --global Email

# Code and modify things 

# Add gitignore files for the files that you don't want to be commited
## the gotigonre files contain commands such as (/output/*) This command will not inculde this folder into the commit
### and if we want to incude only one file from that ignored subdirectory we will use this command (!/output/thisfile.file)

# usign the command (git add . --dry-run --verbose ) for a summary of what is included in the commit 

# we can delete a f ile staed to  the commit using (git rm --cashed filename.file) and we can add it later using the command (git add filename)

# we finally commit to the local repository using the command 'git commit -m "Message of the commit"

# we can delete a file to test the restore command by (rm directoy/filename.file) and use the command () to restore the file (git checkout directory/filename.file) 
# if we want to undo a commit - let's say we commited a new file- so we use (git reset --soft HEAD~) this will undo the commit and return to the initial HEAD and return to the pe commit state

# using (git reset HEAD addedfile.file) will return to the state of pre add