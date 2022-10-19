#include <iostream>
// #include <cstdio>

int addition(int a, int b) {
	int result= a+b;
	std::cout << "Your result:" << result ;
	return result;
}

int main() {
	addition(2,3) ;
	return 0;
}


extern "C" {
	__declspec(dllexport) int* addition_c(int a_c, int b_c) {return addition(a_c, b_c);}
}