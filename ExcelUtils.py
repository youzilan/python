#coding=utf-8
import xlrd
def ReadExcel(excelFile):
    data=xlrd.open_workbook(excelFile,"r")
    """open_workbook()：必选参数：文件名、读写模式r/w"""

    table=data.sheet_by_name("Sheet1")
    """
    
        table = data.sheets()[0]          #通过索引顺序获取
 
        table = data.sheet_by_index(0) #通过索引顺序获取
 
        table = data.sheet_by_name(u'Sheet1')#通过名称获取
        
        """
    nrows=table.nrows #总行数
    ncols=table.ncols  #总列数
    for i in xrange(0,nrows):
        rowValues=table.row_values(i)
        for item in rowValues:
            print item
    return ;
ReadExcel("C:\\Users\\Administrator\\Desktop\\test\\TestReport.xls")
"""文件路径\要加转义字符"""



