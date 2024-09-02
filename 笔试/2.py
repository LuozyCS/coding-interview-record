def count_objects(java_code):
    count = 0
    lines = java_code.split('\n')
    
    for line in lines:
        line = line.strip()
        # 忽略注释行
        if line.startswith("//") or line.startswith("/*") or line.startswith("*"):
            continue
        # 统计 new 关键字的出现次数
        count += line.count("new ")
    
    return count

if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    java_code = input().strip()
    print(count_objects(java_code))