#include <conio.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

main(){
	FILE *p;
	int i = 1;
	char c[200];
	if ((p=fopen("dados.txt","r"))==NULL)
	{
		printf("Erro! impossivel abrir o arquivo!\n");
		exit(1);
	}

	while((fgets(c,sizeof(c),p))!=NULL)
	{
		printf("linha %d = \t%s", i,c);
		i++;
	}
	getch();
	fclose(p);
}