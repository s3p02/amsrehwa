#USE SED
#NO-BACKUP 
sed -i '' 's/800 438-4357/202-456-1414/g;s/800-GET-HELP/202-456-1414/g;s/800.438.4357/202-456-1414/g;' /Users/sharan_sreesai/Documents/amsrehwa/problem2/*.html
#BACKUP --RECOMMENDED IF BACKUP FOR REFERENCE IS REQUIRED
sed -i.backup 's/800 438-4357/202-456-1414/g;s/800-GET-HELP/202-456-1414/g;s/800.438.4357/202-456-1414/g;' /Users/sharan_sreesai/Documents/amsrehwa/problem2/*.html