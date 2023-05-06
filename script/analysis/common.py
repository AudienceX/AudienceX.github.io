import os

def get_files_in_directory(directory, extensions):
    """
    递归查询
    Params:
    - directory: 目录 
    - extensions(str or a tuple of str): 需要匹配的文件后缀, e.g ('jpg', 'jpeg', 'png', 'gif')
    """
    # os.walk 用于遍历目录树
    for dirpath, dirnames, filenames in os.walk(directory):
        for filename in filenames:
            if filename.lower().endswith(extensions):
                # 如果是图片文件, 则将其文件名添加到结果列表中
                yield os.path.join(dirpath, filename)


project_path = '/Users/xuefeng/Documents/vscode-workspace/gitee/private-notes'
tf_icon_src_path = '/Users/xuefeng/Downloads/TF/icon-原图'
tf_icon_dst_path = project_path + '/node_modules/hexo-theme-aurora/source/static/img/tf-icon'

scan_file_types = ('jpg', 'jpeg', 'png', 'webp')