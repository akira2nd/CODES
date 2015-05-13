#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>

int main()
{
	struct ponto
	{
		int x;
		int y;
	}ponto1;

	struct ponto *pontoponteiro;
	pontoponteiro = &ponto1;

	printf("Didite o valor x\n");
	scanf("%d", &pontoponteiro->x);
	printf("Didite o valor y\n");
	scanf("%d", &pontoponteiro->y);
	printf("X %d\n", pontoponteiro->x);
	printf("Y %d\n", pontoponteiro->y);
}