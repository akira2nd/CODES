#include <conio.h>
#include <stdlib.h>
#include <stdio.h>
#include <string.h>

main(){
	FILE *p;
	int i;
	if ((p=fopen("dados.txt","w"))==NULL)
	{
		printf("Erro! impossivel abrir o arquivo!\n");
		exit(1);
	}
	for (i = 0; i < 101; i++)
	{
		fprintf(p,"%d\n", i);
	}
	fclose(p);
}