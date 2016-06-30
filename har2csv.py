#free license to use and distribute
#written by sandeep k shyam - shyamsandeep@gmail.com

import json

if '__main__' == __name__:
    import sys

    if len(sys.argv) < 3:
        print "Usage: %s <har_file> <response time>" % sys.argv[0]
        sys.exit(1)
    objects_file = 'result.csv'
    har_file = sys.argv[1]
    latency = int(sys.argv[2])
    f = open(objects_file,'a')
    f.write("Request - Url"+","+"Time in Seconds")
    f.write("\n")

    # Read HAR archive
    har_data = open(har_file, 'rb').read()
    skip = 3 if '\xef\xbb\xbf' == har_data[:3] else 0

    har = json.loads(har_data[skip:])

    entries = filter(lambda x: latency <= x['time']/1000, har['log']['entries'])
    urls_time = set(map(lambda x: (str(x['request']['url']) + "," + str("{0:.2f}".format(x['time']/1000))), entries))
        
    print "%d Requests took latency greater than %d seconds:" %(len(urls_time), latency)
    for url in urls_time:	
	print url
	f.write(url)
	f.write("\n")
    f.close()
    print "Result also appended to  result.csv file \n"
