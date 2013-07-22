
class EBSConnectClass:
    #!/usr/local/bin/python2.7
    
    
    def __init__(self):
        self.data = []
     
    #Documentation at http://boto.s3.amazonaws.com/ec2_tut.html 
    #Must set up a .boto file in the home directory
     
    def connect(self):
        import sys        
        import boto.ec2
        
        regions = boto.ec2.regions()
        usw1 = regions[5]
        conn_usw1 = usw1.connect()
        
        #print conn_usw1
        return conn_usw1
        
        
        


