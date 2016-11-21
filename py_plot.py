from rpy2.robjects.packages import importr
utils = importr("utils")
# Define command and arguments
command = 'Rscript'
path2script = 'C:/Users/my/Downloads/extract.R'

# Variable number of args in a list


# Build subprocess command
cmd = [command, path2script]

# check_output will run the command and store to result
#x = subprocess.check_output(cmd, universal_newlines=True)

#retcode = subprocess.call([path2script])
##
#subprocess.Popen("R --vanilla C:/Users/my/Downloads/extract.R", shell = True)

r.source("extract.R")
print(x)