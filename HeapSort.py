def heapify(arr,n,i,draw_func):
    largest = i
    l = 2*i+1
    r = 2*i+2
    if l < n:
        if arr[l] > arr[largest]:
            largest = l
    if r < n:
        if arr[r] >arr[largest]:
            largest = r
    if largest != i:
        arr[i],arr[largest] = arr[largest],arr[i]
        draw_func()
        heapify(arr,n,largest,draw_func)
def heap_sort(arr,draw_func):
    n=len(arr)
    for i in range(n//2-1,-1,-1):
        heapify(arr,n,i,draw_func)
    for i in range(n-1,0,-1):
        arr[i],arr[0] = arr[0],arr[i]
        draw_func()
        heapify(arr,i,0,draw_func)
def main():
    chuoi_nhap = input("Nhap day cac chu so, cach nhau bang khoang trang: ")
    arr = list(map(int,chuoi_nhap.split()))
    print(arr)
    heap_sort(arr)
    print(arr)
   

if __name__ == "__main__":
    main()
