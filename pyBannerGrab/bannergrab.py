#!/usr/bin/python

#
##################################################
######## Please Don't Remove Author Name #########
############### Thanks ###########################
##################################################
#
#
__author__='''
    Suraj Singh
    surajsinghbisht054@gmail.com
    http://bitforestinfo.blogspot.com/
'''

# =================Other Configuration================ 
# Usages :
usage = "usage: %prog [options] "
# Version
Version="%prog 0.0.2"
# ====================================================

# Importing Modules
import socket
import time
import threading
import optparse
import sys
import errno



# Port Scanner Engine
class BannerScanner:
    def __init__(self, target, port, thread, timeout):
        self.target=target
        self.port=port
        self.thread=thread
        self.timeout=timeout
        self.store_open_ports=[]
        self.port.reverse()

        # Start Thread
    def get_result(self):
        return self.startthreading()

        # Check Port 
    def checkopenport(self):
        s=socket.socket()
        s.settimeout(float(self.timeout))
        #socket.setdefaulttimeout(float(self.timeout))
        port=self.port.pop()
        storeobj=str(s.connect_ex((self.target, int(port))))
        if storeobj=="0":
            # If Open Port Found
            self.store_open_ports.append(port)
        s.close()
        return 
        

        # Start Threadings
    def startthreading(self):
        listthread=[]
        for i in range(len(self.port)):
            storethread=threading.Thread(target=self.checkopenport)
            storethread.start()
            # Threead Controller
            if int(threading.activeCount())==int(self.thread):
                printingline="\r< IP : {} | Number of Threads : {} | Open Port Checking : {} | Open Ports Founded {} >".format(self.target,str(threading.activeCount()),str(i),str(len(self.store_open_ports)))
                sys.stdout.write(printingline)
                sys.stdout.flush()
                time.sleep(float(self.timeout))
            listthread.append(storethread)

        # Wait For All Thread
        for i in listthread:
            i.join()
        return (self.target, self.store_open_ports)

# Banner Grabbing Class
class BannerGrabber:
    def __init__(self, host, thread, output):
        self.host = host
        self.thread = thread
        self.output = output
        self.banners = []
        self.iter_address()

        # iter All Address
    def iter_address(self):
        starttime = time.time()
        # iter Host Iterms
        for address, port in self.host.items():
            self.start_threading(address, port)
        closetime = time.time()
        print("\n\n",'*'*50,'\n')
        for i in self.banners:
            print("[+] IP : {} | Port : {} | Banner : {}".format(i[0][0],i[0][1],i[1]))
        print("\n",'*'*50,'\n')
        print("[+] Scan Started On ", time.ctime(starttime))
        print("[+] Scan Finished On", time.ctime(closetime))            
        print('[+] Total Time Taken ', end=' ')
        print(closetime-starttime, ' Seconds ')
        print("\n",'*'*50,'\n')
        print("\n\n Thanks For Using My Program by SSB")
        # if Output File Name Is Provided
        if self.output:
            f = open(self.output, 'a')
            for address, port in self.host.items():
                f.write("{} | {} | {}".format(i[0][0],i[0][1],[i[1]]))
            f.close() 
        return

        # Start threadings
    def start_threading(self, address, port):
        listthread=[]
        for i in port:
            storethread=threading.Thread(target=self.banner_ip, args=(address, i,))
            storethread.start()
            if int(threading.activeCount())==int(self.thread):
                printingline="\r< IP : {} | Number of Threads : {} | Port : {}>".format(address, threading.activeCount(),i)
                sys.stdout.write(printingline)
                sys.stdout.flush()
                time.sleep(float(2))
            listthread.append(storethread)
        # Wait For All Threads
        for i in listthread:
            i.join()
        return

        # Banner Grabbing Functions
    def banner_ip(self,address, port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #s.settimeout(10)
        try:
            s.connect((address, port))
            if port==80:
                print("\n[+] HTTP PROTOCOL Founded. IP : {}| PORT : {}".format(address, port))
                #Send some data to remote server
                message = "GET / HTTP/1.1\r\n\r\n"
                s.sendall(message)
                #Now receive data
                self.banners.append([(address, port),s.recv(4096)])
            else:
                self.banners.append([(address, port),s.recv(4096)])
        except socket.error as e:
            if e.errno == errno.ECONNREFUSED:
                pass
            else:
                self.banners.append([(address, port), e])
        s.close()
        return 



# Port Numbers Extractor
def port_extraction(port):
    storeport=[]
    # Verifiying Port Value
    if port:
        # Verifying Port is in Range
        if "-" in port and "," not in port:
            x1,x2=port.split('-')
            storeport=list(range(int(x1),int(x2)+1))
        # Verifying Port is in Commas
        elif "," in port and "-" not in port:
            storeport = [int(i) for i in port.split(',')]
        elif "," in port and "-" in port:
            x2=[]
            for i in port.split(','):
                if '-' in i:
                    y1,y2=i.split('-')
                    x2=x2+list(range(int(y1),int(y2)+1))
                else:
                    x2.append(int(i))
            storeport=x2
        else:
            storeport.append(int(port))
    else:
        print("[*] Please Provide Ports For Scanning.")
        sys.exit(0)
    return storeport



# Checking About User Input Data is IP Or Host
def valid_ip(ip):
    " Verifying IP Address "
    try:
        socket.inet_aton(ip)
    except socket.error:
        ip=socket.gethostbyname(ip)
    return ip

# Main Function
def main():
    print(__author__)
    parser=optparse.OptionParser(usage=usage,version=Version)
    parser.add_option('-t','--target',type='string',dest='target',help="Specify Target For Scan", default=None)
    parser.add_option('-i','--input',type='string',dest='input',help="Specify Input Txt File Of Data", default=None)
    parser.add_option("-p","--port",type='string', dest="port", help="Specify Target Ports Seperated by commas or Provide Range of Ports. eg. 80-1200", default=None)
    parser.add_option('-n',"--thread",type='string', dest="thread", help="Specify Number of Thread For Scanning ", default='500')
    parser.add_option('-o',"--output",type='string', dest="output", help="Specify Path For Saving Output in Txt.", default=None)
    parser.add_option('-c',"--check",type='string', dest="check", help="Specify False Or 0 If Provided Open Ports Are Already TESTED. Or if open ports are not verified then, don't use this argument.", default=None)
    parser.add_option('-T','--timeout',type='string', dest="timeout", help="Specify Port Time Out Seconds ",default='2')

    (options, args)= parser.parse_args()


    # Conditions
    if not options.input:
        if (not options.target):
            print("[*] Please Specify Target. e.g: -t 192.168.10.1 or -t www.site.org \n[*]\t\t or Provide Input File. e.g: -i file.txt")
            sys.exit(0)

        if not options.port and not options.port:
            print("[*] Please Specify Ports Seperated by commas or Provide Range of Ports. eg. 80-120,121,122,123-1200 \n[*]\t\t or Provide Input File. e.g: -i file.txt")
            sys.exit(0)

        if not options.input:
            host = {}
            host[valid_ip(options.target)]=port_extraction(options.port)
    
    else:
        host={}
        lines =open(options.input, 'r').readlines()
        for i in lines:
            host[i.split("\t")[0]]=[]
        for i in lines:
            h = i.split("\t")[0]
            p = i.split("\t")[-1]
            host[h].append(int(p))

    thread=options.thread
    output=options.output
    timeout=options.timeout

    for h,p in host.items():
        print("[*] IP Address Detected : {} | Num. Of Port Detected : {}".format(h,len(p)))


    if not options.check:
        for target, port in host.items():
             s = BannerScanner(target, port, thread, timeout)
             r = s.get_result()
             host[r[0]]=r[1]
             print("[*] Open Ports Verified.\n[+] IP : {} | Ports : {}".format(r[0], r[1])) 
    BannerGrabber(host, thread, output)


# Trigger 
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("[Exiting Program] \n [+]Thanks For Using! Have a nice day! Bitforestinfo[=]")
        sys.exit(0)
    except Exception as e:
        print(e)
