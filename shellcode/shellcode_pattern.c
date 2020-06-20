/*
 * @Description: 
 * @Version: 2.0
 * @Author: 0pt1mus
 * @Date: 2020-06-03 20:08:54
 * @LastEditors: 0pt1mus
 * @LastEditTime: 2020-06-03 20:09:13
 */ 
	#include<stdio.h>
	unsigned char shellcode[] = "";
	int main(int argc, char const *argv[])
	{
		/* code */
		((void(*)())&shellcode)();
		return 0;
}