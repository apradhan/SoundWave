class MongoBackupClass:
    #!/usr/local/bin/python2.7
    
    
    def __init__(self):
        self.data = []
        
    def backupcollection(self, mydatabase, mycollection, myfindexpr):
        import pymongo
        from pymongo import MongoClient
        
        
        print 'InClass: ' + mydatabase + '  ' + mycollection + '  ' + myfindexpr
        
        if myfindexpr:
            findfield = myfindexpr.split(':')[0].strip()
            findval = myfindexpr.split(':')[1].strip()
        else:
            findfield = findval = ''
        
        print findfield, findval
        
        #exit()
        
        client = MongoClient()
        db = client[mydatabase]
        collection = db[mycollection]
        #print db, collection
        
        #For testing purposes
        #onedocument = collection.find_one()
        #print onedocument
        
        mycollectsnap = mycollection + 'snap'
        #print mycollectsnap
        
        collectionsnap = db[mycollectsnap]
        #print collectionsnap
        collectionsnap.drop()
        
        
        listcollections = db.collection_names()
        #print listcollections  
        
        #exit()
        

        #copyover = db.collection.find().forEach( function(x){db.collectionsnap.insert(x)} )
        if not mycollectsnap in listcollections:
            if myfindexpr:         
                cursor = collection.find({'%s' % findfield :'%s' % findval})    #e.g. "is_assigned": "t"
            else:
                cursor = collection.find()
            print cursor
            #exit()              
            for document in cursor:
                #print document
                snap_id = collectionsnap.insert(document)
                #print snap_id
            
            print 'Collection ' + mycollection + ' copied' 
            return [1]
          
        else:
            print mycollectsnap + ' collection exists in ' + mydatabase + ' database'
            return [0] 
            
        
       
            
            
        
        
        

        
        
        

        
      
         
        
        
        
        