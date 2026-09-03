def quick_sort(arr,low,high, draw_func):
    if low<high:
        pivot = Partition(arr,low,high,draw_func)
        quick_sort(arr,low,pivot-1,draw_func)
        quick_sort(arr,pivot+1,high,draw_func)
    

def Partition(arr,low,high,draw_func):    
    pivot = arr[high]
    i = low-1
    for j in range(low, high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
            draw_func()
    arr[i+1],arr[high] = arr[high],arr[i+1]
    draw_func() #kich hoat ve
    return i+1 #vi tri chot


def main():
    chuoi_nhap = input("Nhap day cac chu so, cach nhau bang khoang trang: ")
    arr = list(map(int,chuoi_nhap.split()))
    print(arr)
    quick_sort(arr,0,len(arr)-1)
    print(arr)
   

if __name__ == "__main__":
    main()
    
    