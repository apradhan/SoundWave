import datetime
from Class.EBSBackupClass import EBSBackupClass  #from Class import *
from Class.EBSConnectClass import EBSConnectClass  #from Class import *



if __name__ == "__main__":
    import sys
    

      
    #print len(sys.argv) 
    if len(sys.argv) < 5:
        print "Usage: python RunEBSBackup.py number_of_snapshots_to_keep, description_of_snapshot,"
        print "snapshot_search_filter and volumen id list[]"    
        print "All arguments are required."
        sys.exit(1) 
    
    print sys.argv
    #keep = int(sys.argv[1])  desc = sys.argv[2]  snapfilter = sys.argv[3]

    
    #exit()

     
    now = datetime.datetime.now()
    #print 'Program Start  ' + now.strftime("%Y-%m-%d %H:%M")  #now = datetime.datetime.now() 
    timestamp =  now.strftime("%Y%m%d_%H%M%S") 
    #print timestamp
    
    
    myEBSConnect = EBSConnectClass()
    myec2_conn = myEBSConnect.connect()
    #print myec2_conn

    #params = [myec2_conn, keep, desc, snapfilter]
    #print 'params: ' + str(params)

    myEBSBackup = EBSBackupClass()
    #print sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]
    myEBSBackup.backup_snapshot(myec2_conn, timestamp, sys.argv)


    """
    print 'params: ' + str(params)
    """
    
    exit()