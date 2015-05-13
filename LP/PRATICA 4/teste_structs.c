#include <stdio.h>
#include <conio.h>
#include <string.h>

struct endereco
{
	char rua[50];
	int numero;
	char bairro [20];
	char cidade[30];
	char estado [3];
	long int CEP;
};

struct ficha_pessoal
{
	char nome[50];
	long int telefone;
	struct endereco end;
};

main()
{
	struct ficha_pessoal ficha;
	struct ficha_pessoal ficha, ficha2;

	gets(ficha.nome);
	ficha.telefone = 4921234;
	strcpy(ficha.end.rua, "Rua das Flores");
	ficha.end.numero=10;
	strcpy(ficha.end.bairro, "Jardins");
	strcpy(ficha.end.estado, "MG");
	ficha.end.CEP=31340230;

	ficha2 = ficha;

	printf("%s\n", ficha2.nome);
	printf("%d\n", ficha2.telefone);
	printf("%s\n", ficha2.end.rua);
	printf("%d\n", ficha.end.numero);
	printf("%s\n", ficha.end.bairro);
	printf("%s\n", ficha.end.estado);
	printf("%d\n", ficha.end.CEP);
	getch();
}