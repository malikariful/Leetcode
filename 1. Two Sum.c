

/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
// #include <stdlib.h>
// int compare_ints(const void* a, const void* b)
// {
//     int arg1 = *(const int*)a;
//     int arg2 = *(const int*)b;
 
//     if (arg1 < arg2) return -1;
//     if (arg1 > arg2) return 1;
//     return 0;
 
//     // return (arg1 > arg2) - (arg1 < arg2); // possible shortcut
//     // return arg1 - arg2; // erroneous shortcut (fails if INT_MIN is present)
// }


// int compareints (const void * a, const void * b)
// {
//   return ( *(int*)a - *(int*)b );
// }

int* twoSum(int* nums, int numsSize, int target, int* returnSize){
    int i,j;
    *returnSize=2;
    int *ret = (int*)malloc(2*sizeof(int));
    //qsort(nums,numsSize,sizeof(int),compare_ints);
    //printf("numsSize %d\n",numsSize);
    for(i=0;i < numsSize;++i){ 
        ret[0]=i;
        for(j=i+1;j < numsSize;++j){ 
            if(nums[j]+nums[i]==target){
                //printf("[%d,%d]",i,j);
                ret[1]=j;
                return ret;
            }
        }
        //pItem = (int*) bsearch (&y, nums+i+1, numsSize-i-1, sizeof (int), compareints);
        
    }
    return 0;
    
}
