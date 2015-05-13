#include <stdio.h>
#include <conio.h>
#include <string.h>
#include <stdlib.h>

int _i = 0;

struct carros
{
	char marca[15];
	int ano;
	char cor[10];
	double preco;
};

struct carros vetcarros[20];

int ler_carros(int i){

	printf("Digite a marca:\n");
	scanf("%s", &vetcarros[i].marca);

	printf("\nDigite o ano:\n");
	scanf("%d", &vetcarros[i].ano);

	printf("\nDigite a cor:\n");
	scanf("%s", &vetcarros[i].cor);

	printf("\nDigite o preco:\n");
	scanf("%lf", &vetcarros[i].preco);

	printf("\n");
	system("PAUSE");
	_i++;
}

double ler_preco(double x, int i){
	int a;
	
	printf("\nLocalizado(s):\n");
	for (a = 0; a < i; a++)
	{
		if (vetcarros[a].preco <= x)
		{
			printf("%s\n", vetcarros[a].marca);
			printf("%s\n", vetcarros[a].cor);
			printf("%d\n", vetcarros[a].ano);
			printf("\n");
		}
	}
	printf("\n");
	system("PAUSE");
}


char ler_marca(char x[15], int i){
	int a;
	
	printf("\nLocalizado(s):\n");
	for (a = 0; a <= i; a++)
	{
		if (!stricmp(vetcarros[a].marca , x))
		{
			printf("%.2lf\n", vetcarros[a].preco);
			printf("%d\n", vetcarros[a].ano);
			printf("%s\n", vetcarros[a].cor);
			printf("\n");
		}
	}
	printf("\n");
	system("PAUSE");
}






//função para chamar as demais....................................................................................................
int escolher_func(int x, int i){
	double pr;
	char txt[15];

	system("cls");

	switch(x){
		case 1:
		ler_carros(i);
		break;
		
		case 2:
		printf("Digite o preco procurado\n");
		scanf("%lf", &pr);
		ler_preco(pr, i);
		break;
		
		case 3:
		printf("Digite a marca procurada\n");
		scanf("%s", &txt);
		ler_marca(txt, i);
		break;

		case 4:
		printf("Digite a marca procurada\n");

		break;

	}
}



//inicio do programa.........................................................................................................
main()
{
	int x;

	do
	{
		printf("\t**** Carros ****\n\n");
		printf("( 1 )---Cadastrar Carro\n");
		printf("( 2 )---Procurar por preco\n");
		printf("( 3 )---Procurar por marca\n");
		printf("( 4 )---Procurar por marca, ano e cor\n");
		printf("( 5 )---Sair\n");

		printf("Selecione uma atividade:\n");
		
		scanf("%d", &x);
		if (x <=5 && x!=0)
		{
			escolher_func(x, _i);
		}else{
			system("cls");
			printf("Opcao invalida\n");
			system("PAUSE");
		}
		system("cls");
		
	} while (x != 5);
}