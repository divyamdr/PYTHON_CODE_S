#include<iostream>
#include<bits/stdc++.h>
#include <array> 
using namespace std;
int getPeakElement(int array[]) {
        
 
        int n = 5;
 
        int start = 0;
        int end = n - 1;
 
        while (start <= end) {
            int mid = (start + end) / 2;
 
            if ((mid == 0 || array[mid - 1] <= array[mid]) && (mid == n - 1 || array[mid] >= array[mid + 1])) {
                return array[mid]; // array[mid] is peak element
            } 
			else if (mid > 0 && array[mid - 1] > array[mid]) {
                end = mid - 1;
            } 
			else {
                start = mid + 1;
            }
        }
        return 0;
    }
int main() {
        array<int,5> myarray{ 1, 2, 3, 4, 5 }; 
        int peak = getPeakElement(myarray);
        cout<<(peak != 0 ? "Peak Element is " + peak : "No peak element!");
        return 0;
    }

      
