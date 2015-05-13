#include <stdio.h>
#include <conio.h>

main()
{
	int a;
	int *p;
	a = 10;
	p = &a;
	*p = 32;
	printf("%d\n", a);
	getch();
}
