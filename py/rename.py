import os
import argparse

def rename_files(directory_path, prefix, rename, run=False):
    # 获取目录下所有文件
    files = os.listdir(directory_path)

    for file_name in files:
        # 检查文件名是否以"E0"开头
        # if file_name.startswith('E0'):
        if prefix in file_name:
            # 提取数字部分
            pos = file_name.find(prefix)
            pre = file_name[:pos]
            last = file_name[pos+len(prefix):]
            new_name = f'{pre}{rename}{last}'
            
            old_path = os.path.join(directory_path, file_name)
            new_path = os.path.join(directory_path, new_name)
            
            # 执行重命名
            if run:
                os.rename(old_path, new_path)
            print(f'Renamed: {file_name} to {new_name}')

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Rename files.')
    parser.add_argument('--dir', required=True, type=str, help='Path to the directory containing files')
    parser.add_argument('--target', required=True, type=str, help='Prefix str')
    parser.add_argument('--rename', required=True, type=str, default='S01E', help='rename to')
    parser.add_argument('--run', action='store_true', help='start runing.')
    args = parser.parse_args()

    # 调用函数进行文件重命名，传递目录参数
    rename_files(args.dir, args.target, args.rename, args.run)

