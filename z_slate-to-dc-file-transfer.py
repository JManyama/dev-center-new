from unipath import Path
import shutil 


# CircleCi will run this script 8th (last)

# This script will run after CircleCI generates a fresh set of static files in Slate

# Slate Repo -  Staic Files for API Explorer and API Reference
from_slate_repo_explorer = Path (r"C:\Users\I860605\Desktop\Dev_Center_New\dev_concur\src\Slate-API-Explorer-Reference\slate\build\index.html")
from_slate_repo_reference = Path (r"C:\Users\I860605\Desktop\Dev_Center_New\dev_concur\src\Slate-API-Explorer-Reference\slate\build\api-reference.html")

# Dev Center Repo - Static Files for API Explorer and API Reference
to_dc_repo_explorer = Path(r"C:\Users\I860605\Desktop\Dev_Center_New\dev_concur\src\slate-ui\build\index.html")
to_dc_repo_reference = Path(r"C:\Users\I860605\Desktop\Dev_Center_New\dev_concur\src\slate-ui\build\api-reference.html")


# Move Static API Explorer and API Reference Files from Slate to Dev Center
def moveFilesToDC():
    shutil.copy(from_slate_repo_explorer, to_dc_repo_explorer)
    shutil.copy(from_slate_repo_reference, to_dc_repo_reference)
    print("Static files have been moved from Slate to Dev Center")
    
    

def main():
    moveFilesToDC()

main()