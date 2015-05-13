#include <conio.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

main(){
	FILE *p;
	int i = 0;
	char c;
	if ((p=fopen("dados.txt","r"))==NULL)
	{
		printf("Erro! impossivel abrir o arquivo!\n");
		exit(1);
	}

	while(!feof(p))
	{
		//printf("linha %d = ", i);
		c = getc(p);
		printf("%c", c);	
		//i++;
	}
	getch();
	fclose(p);
}