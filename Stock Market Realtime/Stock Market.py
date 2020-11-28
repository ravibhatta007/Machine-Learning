k=0
while k<60:
    webpage=[]
    valuehigh=[]
    valuelow = []
    data=[]
    results=[]
    code=[]
    code.append("TSLA")
    code.append("AAPL")
    valuehigh.append(488)
    valuehigh.append(120)
    valuelow.append(400)
    valuelow.append(118)
    for i in range(0, len(code)):
        webpage.append("https://finance.yahoo.com/quote/"+code[i]+"/")
    
    from urllib.request import urlopen
    for i in range(0,len(webpage)):
        data.append(urlopen(webpage[i]).read())
        data[i]=str(data[i])
    # Print first few hundred characters of this string:
    #print("*** type(data) == {} ***".format(type(data)))
    #n = 1000
    #print("*** Contents (first {} characters) ***\n{} ...".format(n, data[:n]))
    import re
    for i in range(0,len(webpage)):
        pattern_object = re.compile('currentPrice":{"raw":(\d*)')
        results.append(pattern_object.findall(data[i]))


    import winsound
    for i in range(0,len(webpage)):
        if int(results[i][0]) >valuehigh[i]:
            filename1 = 'burp.wav'
            winsound.PlaySound(filename1, winsound.SND_FILENAME)
            print(code[i]+" share high")
    for i in range(0,len(webpage)):
        if int(results[i][0]) < valuelow[i]:
            filename2 = 'goddamnit.wav'
            winsound.PlaySound(filename2, winsound.SND_FILENAME)
            print(code[i]+" share too low")
    import time
    time.sleep(60)
    k=k+1
