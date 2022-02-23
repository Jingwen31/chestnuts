# Version Control - Git 

### Work independently

```
git clone 
git add script.py
git commit -m "add new files"
git push
```  
  
### Work on teams

#### Scenario #1

*Step 1: You have a local version of this repository on your laptop, and to get the latest stable version, you pull from the develop branch.*  

```
# switch to develop branch  
git checkout develop
```  

```
# pull the latest changes in the develop branch  
git pull
```

*Step 2: when you start working on the demographic feature, you create a new branch called demographic, and start working on your code in this branch.*  

```
# Create and switch to a new branch called demographic from the develop branch
git checkout -b demographic
```  
  
```
# Work on this new feature and commit as you go  
git commit -m 'add gender recommendations'
git commit -m 'add location specific recommendations'
```  
  
*Step 3: However, in the middle of your work, you need to work on another feature. So you commit your changes on this demographic branch, and switch back to the develop branch.*  
  
```
# Commit your changes before switching
git commit -m "refactored gender recommendations"
```  
  
```
# Switch to develop branch
git checkout develop
```  

*Step 4: From this develop branch, you create another branch for a new feature called friend_groups.*  
  
```
# Create and switch to a new branch called friend_groups from the develop branch
git checkout -b friend_groups
```  
  
*Step 5: After you finish your work on the friend_groups branch, you commit your changes, switch back to develop branch, merge it back to develop branch, and push this to the remote repository's develop branch.*  
  
```
# Commit you changes before switching
git commit -m "finalize friend_groups recommendations"

# Switch to develop branch
git checkout develop

# Merge friend_groups branch into develop branch
git merge --no-ff friends_groups

# push to the remote repository
git push origin develop
```  
  
*Step 6: Now, switch back to the demographic branch to continue your progress.*  
  
```
# Switch back the the demographic branch
git checkout demographic
```  
  
#### Branching

```
# show all the branches you have available
git branch
(type q to back to original terminal)
```  
  
```
# checkout to a branch
git checkout  

# create a new branch and checkout to it
git checkout -b
```  
  
```
# delete a branch, this command requires that you are not currently on the branch you would like to delete
git branch -d
```
  
#### Scenario 2


