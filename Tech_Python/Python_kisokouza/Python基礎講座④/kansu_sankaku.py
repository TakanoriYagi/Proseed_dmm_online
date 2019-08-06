# 今回のこの関数をtriangle_areaと名付けました。
# 引数には、高さと底辺を設定しています。
def triangle_area(height, width):
    area = height*width/2
    return area
# 高さと、底辺の長さを、30、20と引数に入れ、プリントしています。
print(triangle_area(30, 20))