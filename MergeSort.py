def merge(arr, left, mid, right,draw_func):
    left_arr = arr[left:mid+1]
    right_arr = arr[mid+1:right+1]
    i=j=0
    k=left
    while i < len(left_arr) and j < len(right_arr):
        if(left_arr[i]<right_arr[j]):
            arr[k] = left_arr[i]
            i+=1
        else:
            arr[k] = right_arr[j]
            j+=1
        k+=1
        draw_func()
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i+=1
        k+=1
        draw_func()
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j+=1
        k+=1
        draw_func()
def merge_sort(arr,left,right,draw_func):
    if left<right:
        mid = (left+right)//2
        merge_sort(arr,left,mid,draw_func)
        merge_sort(arr,mid+1,right,draw_func)
        merge(arr,left,mid,right,draw_func)
    else:
        return None
        
def main():
    chuoi_nhap = input("Nhap day cac chu so, cach nhau bang khoang trang: ")
    arr = list(map(int,chuoi_nhap.split()))
    print(arr)
    merge_sort(arr,0,len(arr)-1)
    print(arr)
   

if __name__ == "__main__":
    main()
