/*
 * @Description: 
 * @Version: 2.0
 * @Author: 0pt1mus
 * @Date: 2020-05-25 10:13:02
 * @LastEditors: 0pt1mus
 * @LastEditTime: 2020-05-25 10:21:46
 */ 
#include<stdio.h>

unsigned char shellcode[] = "";

int main(int argc, char const *argv[])
{
    /* code */
    ((void(*)())&shellcode)();
    return 0;
}