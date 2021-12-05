import os 

def os_try():
    """
    os的操作，print和实际上的结果是有出入的。最好使用debuger的方法进行操作。
    """
    
    a = __file__ ## 得到文件的绝对路径
    print(f"file is {a}")
    dir1 = os.path.abspath(__file__) ## 得到文件的绝对路径

    print(f"abspath is {dir1}")
    dir2 = os.path.dirname(__file__) ## 得到上一层的绝对路径（去掉最后一个）
    print(f"dirname is {dir2}")

    base_dir = os.path.dirname(os.path.abspath(__file__))  ## 得到上一层的绝对路径（去掉最后一个）
    print(f"base_dir is {base_dir}")
    base_name = os.path.basename(os.path.abspath(__file__)) ## 得到文件名或者是最下面一层
    print(f"base_name is {base_name}")

if __name__ == '__main__':
    os_try()