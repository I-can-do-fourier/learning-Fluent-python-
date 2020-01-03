#1 endode/decode时遇到的问题

#coping with UnicodeEncodeError

city = 'São Paulo'

a=city.encode("utf8")
b=city.encode("utf16")

c=city.encode("cp437",errors='ignore')
c=city.encode("cp437",errors='replace')
c=city.encode("cp437",errors='xmlcharrefreplace')

# codecs.register_error

#coping with UnicodeDecodeError
octets = b'Montr\xe9al'#These bytes are the characters for “Montréal” encoded as latin1; '\xe9' is the byte for “é”.

a=octets.decode('cp437')#可以用cp437解码，因为它是Latin1的父集
b=octets.decode('iso8859_7')#这样会出现误码
c=octets.decode('utf-8',errors='replace')#这样会无法解码,用?替换掉

#2 SyntaxError

#chardetect 

#BOM utf-16 判断是little-endian还是big-endian   utf-16le utf-16be无bom标识  utf-8无需bom标识 