
class EBSBackupClass:
    #!/usr/local/bin/python2.7
    
    
    def __init__(self):
        self.data = []

    def list_to_dict(lst):
        # http://stackoverflow.com/questions/1233546/python-converting-list-of-tuples-into-a-dictionary
        dict = defaultdict( list )
    
        for key, value in lst:
            if key in dict:
                raise Exception("Key {} found multiple times in list {)".format(key, lst))
            dict[key] = value
        return dict
    
     
    def backup_snapshot(self, myconn, mytimestamp, myargv):
        import sys
        import inspect
        from operator import itemgetter, attrgetter
        from Class.SnapRec import SnapRec
        from boto.exception import EC2ResponseError
        
        ownerid = '' #Must have AWS owner ID here
        #http://stackoverflow.com/questions/7605631/passing-a-list-to-python-from-command-line
        #http://stackoverflow.com/questions/817087/call-a-function-with-argument-list-in-python

        #print "In Class:", myconn, mytimestamp, myargv
        classname = myargv.pop(0)
        snapkeep = myargv.pop(0)
        snapdesc = myargv.pop(0)
        snapfilter = myargv.pop(0)
        
        #print classname, snapkeep, snapdesc, snapfilter, myargv
        
        try:
            for volid in myargv:
                print '\n\nDescription:' + snapdesc + ' Volume_ID:' + volid + ' Program_Start_Timestamp:' + mytimestamp
                
                fullsnapdesc = snapdesc + '_' + volid + '_' + mytimestamp
                print fullsnapdesc

                snapojb = myconn.create_snapshot(volid, fullsnapdesc) #COMMENT OUT FOR TESTING
                
                #print asnapshot['Snapshot']
                #print snapfilter
                allsnaps = myconn.get_all_snapshots(snapshot_ids=None, owner=ownerid, restorable_by=None, filters={'volume_id': volid, 'description': snapfilter})
                #print 'List of snapshot objects:' + str(allsnaps)
                #print '\n'
                row=0
                allsnapobj = []
                for snap in allsnaps:
                    if (row<100): 
                        row+=1 
                        #print row 
                    else: 
                        exit()
                    
                    #snaplist = [row, snap.id, snap.volume_id, snap.description, snap.start_time] 
                    #print snaplist
                    allsnapobj.append(SnapRec(row, snap.id, snap.volume_id, snap.description, snap.start_time))
                    #print inspect.getcomments(snap)
                    #getmemlist = inspect.getmembers(snap)
                    #print getmemlist
                
                #print allsnapobj
                #print '\n'
            
                allsnapobj_sort = sorted(allsnapobj, key=attrgetter('start_time'),reverse=True)
                #print allsnapobj_sort
                print '\n'
                
                cnt=0
                for snap in allsnapobj_sort:
                    cnt+=1
                    #print cnt, type(cnt), snapkeep, type(snapkeep)
                    if (cnt<=int(snapkeep)):
                        print 'Keeping snapshot:' + snap.snapid + ' ' + snap.description + '  ' + snap.start_time
                    else:
                        print 'Zapping snapshot:' + snap.snapid + ' ' + snap.description + '  ' + snap.start_time  
                        
                        myconn.delete_snapshot(snap.snapid)   #COMMENT OUT FOR TESTING  
                        
        except EC2ResponseError:
            print "400 Bad Request"
            #print "It looks like the snapshot Name, " + paramdate + " is already in use."
        except Exception as e:
            print "Unexpected error:", sys.exc_info()[0]
            print e
            raise 
            
        return(0)

                    


        
        
        
       
        

        
     
