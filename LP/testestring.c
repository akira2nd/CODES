#include <stdio.h>
#include <conio.h>

main(){
	char *vetor = "teste de programacao";
	char *p;

	p = &vetor[2];
	printf("%c\n", *p);
	p = p+2;
	printf("%c\n", *p);
	getch();
}
