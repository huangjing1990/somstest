from Common.Shell import *

jar_path = 'E:/huangjing/TokenUtils.jar'
command = "java -jar " + jar_path + " " + "18637692102"

print(Shell().invoke(command))
