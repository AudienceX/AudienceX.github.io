import os
from io import StringIO

dir, _ = os.path.split(__file__)
rootpath = os.path.join(dir, '../../_posts')
path = os.path.join(rootpath, '内容')
output_filepath = os.path.join(rootpath, '目录', "全文索引.md")


def get_current_time():
    """
    获取当前时间
    Returns: 
    string: 格式 yyyy-MM-dd hh:mm:ss
    """
    import time
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

def write_post(value):
    with open(output_filepath, 'w') as f:
        f.write(value)

def format_path(path, rootpath):
    # realpath = os.path.relpath(path, rootpath)
    depth = len(os.path.relpath(path, rootpath).split(os.path.sep))

    _, name = os.path.split(path)

    if os.path.isdir(path):
        ret = '#' * depth + ' ' + name
    else:
        fname = path.replace(rootpath, '').replace('.md', '')
        ret = '- {' + "% post_link \"内容{}\" %".format(fname) + '}'
              
    return ret

def write_metadata(sb):
    sb.write('---\n')
    sb.write("title: 全文索引\n")
    sb.write("categories: [目录]\n")
    sb.write('date: {}\n'.format(get_current_time()))
    sb.write('---\n')
    sb.write('\n')
     

if __name__  == "__main__":
    sb = StringIO()
    write_metadata(sb)

    for dirpath, dirnames, filenames in os.walk(path):
        # 排序子目录名，保证输出顺序
        dirnames.sort()

        sb.write(format_path(dirpath, path))
        sb.write('\n')

        # 排序文件名，保证输出顺序
        filenames.sort()
        # 打印文件名
        for filename in filenames:            
            _, ext = os.path.splitext(filename)
            if ext != '.md':
                continue
            sb.write(format_path(os.path.join(dirpath, filename), path))
            sb.write('\n')

    write_post(sb.getvalue())




