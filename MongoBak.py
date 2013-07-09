import datetime
from Class.MongoBackupClass import MongoBackupClass

if __name__ == "__main__":
    import sys
    
    #python MongoBak.py structure cids 'is_assigned: t'
    #python MongoBak.py structure holding ''
    
    if len(sys.argv) <= 3:
        print "Usage: You need a database name, a collection name and a find expression, 'collectionfield: value'"    
        sys.exit(1) 
        
    mydatabase = sys.argv[1]
    mycollection = sys.argv[2]  
    myfindexpr = sys.argv[3] 
    print mydatabase + '  ' + mycollection + '  ' + myfindexpr
    
    myMongoBak = MongoBackupClass()
    mybackup = myMongoBak.backupcollection(mydatabase, mycollection, myfindexpr)
        
    exit()




