import os
import shutil
import tarfile

listOfFiles = []
workloc = "/home/joker/workloc"
rpmbundle = "/home/joker/rpmbundles"

# Cleanup workloc
shutil.rmtree(workloc)
os.mkdir(workloc)

# Get all files that start with "rpm"
os.chdir(rpmbundle)
for files in os.listdir("."):
    if files.startswith("rpm"):
	listOfFiles.append(files)

# Sort them by date/time
files2 = sorted(listOfFiles, key=os.path.getctime)

# Get newest rpm-bundle file
newest = files2[-1]

# Copy it to work location
shutil.copyfile(newest, workloc + "/" + newest)

# Go to work location
os.chdir(workloc)

# Extract the archive
tfile = tarfile.open(newest, 'r:gz')
tfile.extractall('.')
os.remove(newest)

# Copy files in parent
# directories = [d for d in os.listdir(os.getcwd()) if os.path.isdir(d)]
# os.chdir(directories[0])



