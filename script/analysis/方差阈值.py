import os
import math
from PIL import Image, ImageChops
import multiprocessing
from tqdm import tqdm


def get_rmse(img1, img2):
    """
    计算两张图片的均方根误差 (Root Mean Square Error, RMSE) 
    此函数用于判断两张图片内容相似度
    """
    # 计算img_a和img_c的均方根误差（RMSE）
    diff = ImageChops.difference(img1, img2)
    h = diff.histogram()
    sq = (value*((idx % 256)**2) for idx, value in enumerate(h))
    sum_of_squares = sum(sq)
    rmse = math.sqrt(sum_of_squares / float(img1.size[0] * img1.size[1]))
    return rmse

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
                # 如果是图片文件，则将其文件名添加到结果列表中
                yield os.path.join(dirpath, filename)


project_path = '/Users/xuefeng/Documents/vscode-workspace/gitee/private-notes'

tf_icon_src_path = '/Users/xuefeng/Downloads/TF/icon-原图'
tf_icon_dst_path = project_path + '/node_modules/hexo-theme-aurora/source/static/img/tf-icon'



def func(fp):
    """
    根据图片地址和 imgs_dir 地址生成方差
    """
    _, fname = os.path.split(fp)
    name, ext = os.path.splitext(fname)

    list = []
    img1 = Image.open(fp)
    cnt = 0
    for sfp in get_files_in_directory(tf_icon_dst_path, ('jpg', 'jpeg', 'webp')):
        img2 = Image.open(sfp)
        list.append(get_rmse(img1, img2))
        cnt += 1
        if cnt == 5:
            break
    return (name, sorted(list)[:5])


if __name__ == '__main__':
    
    with multiprocessing.Pool(processes=10) as pool:
        results = []
        for result in tqdm(pool.imap_unordered(func, get_files_in_directory(tf_icon_src_path, ('jpg', 'jpeg', 'webp'))), total=225):
            results.append(result)


        for item in results:
            name, li = item
            print(name + ", list=" + str(li))


    # # results = pool.map(process_image, [(name, img, map_icon) for name, img in map_src.items()])


    # rmsse_ret = dict(results)
    # for k, v in rmsse_ret.items():
    #     print(f"k={k}, and count = {v}")

            



