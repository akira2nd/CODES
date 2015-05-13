#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>

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

struct ficha_pessoal vet_func[100];

main()
{
	int i;
	for(i=0;i<2;i++)
	{
		printf("Entre com o nome:\n");
		gets(vet_func[i].nome);
		printf("Telefone:\n");
		scanf("%d", &vet_func[i].telefone);
		printf("Rua:\n");
		gets(vet_func[i].end.rua);
		printf("Numero:\n");
		scanf("%d", &vet_func[i].end.numero);
		printf("bairro:\n");
		gets(vet_func[i].end.bairro);
		printf("Cidade:\n");
		gets(vet_func[i].end.cidade);
		printf("Cep:\n");
		scanf("%d", &vet_func[i].end.CEP);
	}

	for (i = 0; i < 2; i++)
	{
		printf("Entre com o nome:%s\n", vet_func[i].nome);
		printf("Telefone:%d\n", vet_func[i].telefone);
		printf("Rua:%s\n", vet_func[i].end.rua);
		printf("Numero:%d\n", vet_func[i].end.numero);
		printf("\tbairro:%s\n", vet_func[i].end.bairro);
		printf("Cidade:%s\n", vet_func[i].end.cidade);
		printf("Cep:%d\n", vet_func[i].end.CEP);
	}
	getch();
}