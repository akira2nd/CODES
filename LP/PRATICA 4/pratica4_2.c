#include <stdio.h>
#include <conio.h>

main()
{
	int *p, n;
	printf("digite um numero:");
	scanf("%d", &n);
	p = &n;
	printf("numero:%d endereco:%p\n", *p,&p);
	getch();
}
