#要给定编码格式

fp=open("C:\\Users\\hanxinhang\\Desktop\\test_txt.txt",'w',encoding='utf8')
fp.write('café')
fp.close

fp=open("C:\\Users\\hanxinhang\\Desktop\\test_txt.txt",'w',encoding='utf16')
fp
fp.write('café')
fp.close()

#'r','w'都默认读取文本 .'rb','wb'都是控制bytes

fp=open("C:\\Users\\hanxinhang\\Desktop\\test_txt.txt",'wb')
fp.write(b'caf\xc3\xa9')
fp.close()

fp1=open("C:\\Users\\hanxinhang\\Desktop\\test_txt.txt",'rb')
fp1

fp2=open("C:\\Users\\hanxinhang\\Desktop\\test_txt.txt",'r',encoding='utf-8')
fp2

fp3=open("C:\\Users\\hanxinhang\\Desktop\\test_txt.txt",'r')
fp3