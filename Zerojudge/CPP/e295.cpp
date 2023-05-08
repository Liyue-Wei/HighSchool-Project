#include<iostream>
using namespace std;
long i, n;
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(0);
    cout.tie(0);
    while(cin >> i >> n){
        cout << i+n << '\n';
    }
    return 0;
}

/*
#include <stdio.h>
using namespace std;

char ReadChar() {
	static int counts = 1 << 21;
	static const int length = 1 << 20;
	static char buffer[length];
	static char *pointer = buffer, *end = buffer;
	if (pointer == end) {
		if (counts < length)
			return EOF;
		counts = fread(buffer, 1, length, stdin);
		end = buffer + counts;
		pointer = buffer;
	}
	return *(pointer++);
}

template <class type>
bool ReadNumber(type *number) {
	static char buffer;
	static bool negative;
	while ((buffer = ReadChar()) < '-')
		if (buffer == EOF)
			return false;
	negative = (buffer == '-');
	*number = (negative ? '0' : buffer - '0');
	while ((buffer = ReadChar()) >= '0')
		*number = (*number << 3) + (*number << 1) + buffer - '0';
	*number *= (negative ? -1 : 1);
	return true;
}

class Printer {
public:
	static const int length = 1 << 20;
	char buffer[length], *pointer, *end;

	Printer() {
		pointer = buffer, end = pointer + length - 1;
	}

	~Printer() {
		*pointer = '\0', printf("%s", buffer);
	}

	void PrintNumber(unsigned int number, char separation) {
		static char digits[20];
		int index = 0;
		digits[index] = separation, index++;
		if (!number)
			digits[index] = '0', index++;
		while (number)
			digits[index] = (number % 10) + '0', index++, number /= 10;
		while (index) {
			if (pointer == end)
				*pointer = '\0', printf("%s", buffer), pointer = buffer;
			--index, *pointer = digits[index], pointer++;
		}
	}

} *printer = new Printer();

int main() {
	unsigned int number1, number2;
	while (ReadNumber(&number1) && ReadNumber(&number2))
		(*printer).PrintNumber(number1 + number2, '\n');
	delete printer;
}
*/

//https://zerojudge.tw/ShowProblem?problemid=e295
