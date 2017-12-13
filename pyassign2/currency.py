# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 11:12:38 2017

@author: 张泽岳（1700011816）
"""
from urllib.request import urlopen

def stupidurl(source,target,amount):
    amount=str(amount)
    dildo='http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+source+'&to='+target+'&amt='+amount
    doc = urlopen(dildo)
    docstr = doc.read()
    doc.close()
    jstr = docstr.decode('ascii')
    return jstr
    
def goout(longwords):
    middlewords=''
    for i in range(1,len(longwords)-1):
        if ord(longwords[i])==46 or 47<ord(longwords[i])<58 or ord(longwords[i])==32: 
            middlewords=middlewords+longwords[i]
            
    keys=middlewords.split()
    shortwords=float(keys[1])        
    return shortwords

def exchange(currency_from, currency_to, amount_from):
    '''This function is a method of currency exchange. 
    You are supposed to enter the three-letter currency abbreviation as "currency_form" and "currency_to" 
    which are strings, and enter the amount of the money as "amount_from" which is a float.
    The function will output a float as the answer.
    '''
    xiongjie=stupidurl(currency_from, currency_to, amount_from)
    wangyizhou=goout(xiongjie)
    return wangyizhou

def test_stupidurl():
    assert('{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }'
          == stupidurl('USD','EUR',2.5))
    assert('{ "from" : "17.94202 Burundian Francs", "to" : "0.016876059892636 Bulgarian Levs", "success" : true, "error" : "" }'
          == stupidurl('BIF','BGN',17.94202))
    assert('{ "from" : "0.002339 Liberian Dollars", "to" : "0.00018704481822796 Moroccan Dirhams", "success" : true, "error" : "" }'
          == stupidurl('LRD','MAD',0.002339))
    assert('{ "from" : "0.1234 Trinidad and Tobago Dollars", "to" : "5.9101914189576 Zimbabwean Dollars", "success" : true, "error" : "" }'
          == stupidurl('TTD','ZWL',0.1234))
    

def test_goout():
    assert(goout('I have 3.17228 mol water! I am a 4.0-GPAer! HHHHHH diejojiojsoif 123666.')==4.0)
    assert(goout('IJLI isdshfia der shi jfaioewa 23000.00 jafiewojf 222 jafieojfaewjf 2222')==222)
    assert(goout('hohoho eifalwjfeweafewafewafjo. I was eijafwl6666666 eaijfiea.')==6666666)


def test_exchange():
    assert(exchange('CLF','NGN',45.577)==708141.99563535)
    assert(exchange('DJF','TRY',0.023)==0.00044257586284052)
    assert(exchange('CNY','YER',1)==38.382364793944)
    
    
def test_all():
    """test all cases"""
    test_stupidurl()
    test_goout()
    test_exchange()
    print("All tests passed")
    