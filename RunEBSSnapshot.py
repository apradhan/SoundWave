import datetime
from Class.EBSSnapshotClass import EBSSnapshotClass  #from Class import *
from Class.EBSConnectClass import EBSConnectClass  #from Class import *

#import sys, getopt, boto
#from boto.ec2.image import Image
#from boto.ec2.image import ImageAttribute
#from boto.ec2.key import Key
#from datetime import datetime, date, time
#from collections import defaultdict

if __name__ == "__main__":
    import sys
    
    
    
    if len(sys.argv) <= 4:
        print "Usage: python ebs_snapshot.py instance_id, number_of_backups_to_keep, description and AMI filter"    
        print "All arguments are required."
        sys.exit(1) 
     
    instid = sys.argv[1]
    keep = int(sys.argv[2]) 
    desc = sys.argv[3] 
    amifilter = sys.argv[4]
    #print instid + '  ' + str(keep) + '  ' + desc + '  ' + amifilter
    
    #exit()
        
    #Parameters, substitute your own below
    amiownerid = '' #AWS owner ID goes here

     
    now = datetime.datetime.now()
    #print 'Program Start  ' + now.strftime("%Y-%m-%d %H:%M")  #now = datetime.datetime.now() 
    
    timestamp =  now.strftime("%Y%m%d_%H%M%S") 
    #print timestamp
    
    
    myEBSSnapshot = EBSSnapshotClass()
    
 
    myEBSConnect = EBSConnectClass()
    myec2_conn = myEBSConnect.connect()
    print myec2_conn


    #print instid + '  ' + str(keep) + '  ' + desc

    params = [myec2_conn, instid, keep, desc]
    print 'params: ' + str(params)
    
    myEBSSnapshot.backup_instance(params, amiownerid, amifilter)
     
    #After you create an AMI above, it is counted as one of AMIs that is retained by the line below
     
    myEBSSnapshot.del_older_ami(params, amiownerid, amifilter) 
     
    
    #backup_volumes(myparams)
    
    exit()