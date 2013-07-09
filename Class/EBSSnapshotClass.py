
class EBSSnapshotClass:
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
    
     
     
    def connect(self, accesskey, secretkey): 
        import sys
        from boto.ec2.connection import EC2Connection
        from boto.ec2.regioninfo import RegionInfo
        
        # Substitute your access key and secret key here
        aws_access_key = accesskey
        aws_secret_key = secretkey
        # Change to your region/endpoint...
        region = RegionInfo(endpoint='us-west-1.ec2.amazonaws.com', name='us-west-1')
       
        ec2_conn = EC2Connection(aws_access_key, aws_secret_key, region=region) 
        print 'Connection to EC2 established'
        print ec2_conn
        return ec2_conn

        
     
    def backup_instance(self, backupparam):
        
        print 'Backing up EC2 instance.'
        print backupparam
        ec2_conn = backupparam[0]
        instances = ec2_conn.get_all_instances(instance_ids=[backupparam[1]])
        #print instances
    
        instid = backupparam[1]
        datestring = self.get_date()
        #datestring = '2013-04-04'
        paramdate = backupparam[3] + '_' + datestring
        #print paramdate     
        return 1  #Uncomment for testing purposes
        
        if ec2_conn.create_image(instid, paramdate, no_reboot=False):
            print 'Image created with description: ' + paramdate
            return 1
        else:
            print 'AMI image was not created.' 
            return 0
            
    def get_date(self):
        import datetime
        
        #utc_datetime = datetime.utcnow()
        #formated_string = utc_datetime.strftime("%Y-%m-%d-%H%MZ") #Result: '2011-12-12-0939Z'
        adatetime = datetime.datetime.now()
        formated_string = adatetime.strftime("%Y-%m-%d") #Result: '2011-12-12'
        return formated_string
        
    
    def del_older_ami(self, myparams, ownerid, filterstring):
        from datetime import datetime, date, time
        
        ec2_conn = myparams[0]
        target = ec2_conn.get_all_images(owners=[ownerid],filters={'name': filterstring})   #image_ids=['ami-3cf3df79']
        #print target
        #print len(target)
        #print target[0], target[1]    
        
        #print '\nLooping through all the AMIs'
        dlist = []
        for img in target:
            ilist = []
            #print img, img.name, img.id
            ec2_image = ec2_conn.get_image_attribute(img.id, attribute='launchPermission')
            #print ec2_image
            
            dp = img.name.split('_')[1].split('-')
            #print dp
            d= date(int(dp[0]),int(dp[1]),int(dp[2]))
            #print d
            ilist = (img.name, img.id, d)
            #print ilist
            
            dlist.append(ilist)
            
        #print dlist
        #print dlist[0][2]
        
        #http://stackoverflow.com/questions/6666748/python-sort-list-of-lists-ascending-and-then-decending
        #L = [['a',1], ['a',2], ['a',3], ['b',1], ['b',2], ['b',3]]
        #L.sort(key=lambda k: (k[0], -k[1]), reverse=True)
        #L now contains:
        #[['b', 1], ['b', 2], ['b', 3], ['a', 1], ['a', 2], ['a', 3]]
        
        dlist.sort(key=lambda k: (k[2]), reverse=True)
          
        #print 'Sorted dlist:', dlist
        
        print 'Deregistering older AMIs and deleting their snapshots'
        amiret = myparams[2]
        print 'Retaining ' + str(amiret) + ' ami backups'
        cnt = 1
        for amilist in dlist:
            print amilist, cnt
            
            if cnt <= amiret:
                cnt += 1
                print 'keeping ami ' + amilist[1]
                continue
            else:
                print 'zap the ami ' + amilist[1]
                #Comment out line below for testing purposes
                #ec2_conn.deregister_image(amilist[1], delete_snapshot=True)
                print 'AMI ' + amilist[0] + ' with image id of ' + amilist[1] + ' is deleted along with associated snapshots.'
            cnt += 1
        


