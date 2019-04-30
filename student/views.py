import os
import sys
import xlwt

from django.conf import settings
from django.shortcuts import render



# Create your views here.

def get(self, request):

    """
    下载文件
    """
    user = request.user

    row_num = 0
    students = Studnt.objects.all()

    data = [[vul.ip,vul.port,vul.vul_name,vul.vul_type,get_lelve(vul.level),vul.description,
                vul.reference,vul.advice,get_status(vul.status),utc2local(vul.create_time)] for vul in students]

    filename = '学生名单.xls'
    file_path = os.path.join('download')
    save_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    the_file_name = os.path.join(save_path.encode("utf-8"), filename.encode("utf-8"))

    book = xlwt.Workbook(encoding='utf-8')
    sheet1 = book.add_sheet('学生名单')

    title_list = ['序号','姓名','性别','年龄','漏洞类型','危险等级','漏洞描述','风险地址','修复建议','处置状态','最近发现时间']
    for col in range(len(title_list)):
        sheet1.write(0, col, title_list[col])
    for vul in data:
        row_num += 1
        vul.insert(0,row_num)
        for col_num in range(len(vul)):
            sheet1.write(row_num, col_num, vul[col_num])
    book.save(the_file_name)
    file_name_download = os.path.join('/media', file_path, filename)

    return Response({
        "status": 200,
        "msg": "成功",
        "data": {"download_url": file_name_download}
    })