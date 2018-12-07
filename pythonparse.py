#
# working to parse a nested tuple into dict

#
#
from ast import literal_eval

str = "([(u'soapEnvelope', ([(u'@xmlnssoap', u'http//schemas.xmlsoap.org/soap/envelope/'), (u'@xmlnsxsi', u'http//www.w3.org/2001/XMLSchema-instance'), (u'@xmlnsxsd', u'http//www.w3.org/2001/XMLSchema'), (u'soapBody', ([(u'MakePaymentResponse', ([(u'@xmlns', u'http//govconnect.com/epay'), (u'MakePaymentResult', ([(u'ReturnCode', u'Payment_Success'), (u'ResultMessage', None), (u'TimeoutLimit', u'180'), (u'ConfirmationNumber', u'18062261053382'), (u'TotalAmount', u'2'), (u'SettlementSubmissionDate', u'6/23/2018'), (u'CardType', u'Unknown'), (u'AuthorizationCode', u'2697')]))]))]))]))])"

obj = literal_eval(str)[0]

def r(s):
    if isinstance(s, tuple) and len(s) == 2:
        return {s[0]:r(s[1])}
    if isinstance(s, list):
        return {x[0]:r(x[1]) for x in s}
    return s

print(r(obj))
