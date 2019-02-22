import sys

# Open a file
with open(sys.argv[1]) as lo_hk:

    for line in lo_hk:
        #line = lo_hk.readline()
        print("Read Line: %s" % (line))


# Close opend file
lo_hk.close()