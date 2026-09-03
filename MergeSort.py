def merge(arr, left, mid, right):
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
    while i < len(left_arr):
        arr[k] = left_arr[i]
        i+=1
        k+=1
    while j < len(right_arr):
        arr[k] = right_arr[j]
        j+=1
        k+=1
def merge_sort(arr,left,right):
    if left<right:
        mid = (left+right)//2
        merge_sort(arr,left,mid)
        merge_sort(arr,mid+1,right)
        merge(arr,left,mid,right)
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
