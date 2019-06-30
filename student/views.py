import os
import sys
import xlwt
import io
from urllib.parse import quote


from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.

def get(self, request):

    """
    下载静态(模板)文件, 将文件交给nginx代理下载
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


def down_load():
    """
    以文件流直接下载
    用于动态生成的数据
    :return:
    """
    row_num = 0
    all_vuls = VI.objects.all()
    temp = all_vuls.values('ip', 'port', 'vul_name', 'vul_type').distinct()
    temp_id_list = [all_vuls.filter(**dict(item)).order_by('-create_time').first().id for item in temp]
    vuls = all_vuls.filter(id__in=temp_id_list).order_by('-create_time')

    data = [[vul.ip, vul.port, vul.vul_name, vul.vul_type, get_lelve(vul.level), vul.description,
             vul.reference, vul.advice, get_status(vul.status), utc2local(vul.create_time)] for vul in vuls]

    filename = '漏洞列表.xls'
    file_path = os.path.join('download')
    save_path = os.path.join(settings.MEDIA_ROOT, file_path)
    if not os.path.exists(save_path):
        os.mkdir(save_path)
    the_file_name = os.path.join(save_path.encode("utf-8"), filename.encode("utf-8"))

    book = xlwt.Workbook(encoding='utf-8')
    sheet1 = book.add_sheet('漏洞列表')

    title_list = ['序号', 'IP', '端口', '漏洞名称', '漏洞类型', '危险等级', '漏洞描述', '风险地址', '修复建议', '处置状态', '最近发现时间']
    for col in range(len(title_list)):
        sheet1.write(0, col, title_list[col])
    for vul in data:
        row_num += 1
        vul.insert(0, row_num)
        for col_num in range(len(vul)):
            sheet1.write(row_num, col_num, vul[col_num])
    buffer = io.BytesIO()
    book.save(buffer)
    filename = quote(filename) # 下载中文名称
    response = HttpResponse(buffer.getvalue())
    response['Content-Type'] = 'application/vnd.ms-execl,charset=utf-8-sig'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(filename)
    return response


def down_template(request):
    """下载模板文件
    """
    plugin_id = request.GET.get('plugin_id','')
    if plugin_id:
        try:
            plugin = PluginInfo.objects.get(id=int(plugin_id))
        except PluginInfo.DoesNotExist:
            context = {
                "status": 500,
                "msg": "插件不存在",
            }
            return Response(context)
        file_name = plugin.file_name
        file_path = os.path.join(FILE_BASE_PATH, file_name)
    else:
        file_path = os.path.join(TEMPLATE_FILE_PATH,'template.py')

    def file_iterator(file_name, chunk_size=512):
        with open(file_name, 'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    response = StreamingHttpResponse(file_iterator(file_path))
    the_file_name = 'template.py'
    response['Content-Type'] = 'application/octet-stream,charset=utf-8-sig'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(the_file_name)
