import os
import sys

def MultipleGitPuller():
    
    startingDir = input("Please Provide the path of the directory that you want to git pull: ")


    startingDir = os.path.normpath(startingDir.replace('\\', '/'))

    if(os.path.exists(startingDir)):
        actualdir = startingDir
    else:
        print("Error, please make sure the path is correct and exists.")
        return MultipleGitPuller()

    foundAtleast1dir= False
    gitpullsCount = 0
    dirsSearchedCount = 0

    for root,dirs,files in os.walk(actualdir,True):
        
        operationalPath = os.path.join(root,'.github')

        if os.path.exists(operationalPath):
            print(root)
            if not foundAtleast1dir:
                foundAtleast1dir = True #For signaling that in all of the executions we atleast found a pullable directory
            print(f'GIT CLONE DIRECTORY FOUND, PROCEEDING WITH GITPULL AT: {root}')
            os.chdir(operationalPath)
            os.system('git pull')
            gitpullsCount += 1
        dirsSearchedCount +=1

    if not foundAtleast1dir:
        print("Didn't find any git pullable directories inside the provided root")
    else:
        print(f'Total Number of GITPULLs: {gitpullsCount}, Total Number of directories searched: {dirsSearchedCount} ')



if __name__ == '__main__':

    #provide the path of your git pullable files, this script will git pull anything inside the path you provide.
    MultipleGitPuller()
