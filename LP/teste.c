#include <stdio.h>
#include <stdlib.h>
#include <conio.h>

int eprimo(int n){
	int var = 1,i;
	for(i=2;i<n;i++){
		if(n%i == 0){
			var = 0;
			break;
		}
	}
	return var;
}

int main(){
	int n,num;

	printf("Numero:");
	scanf("%d", &n);
	num = eprimo(n);

	if (num)
	{printf("%d E primo!\n",n);}
	else{printf("%d Nao e primo!\n",n);}
	getch();
}

//1. Escreva uma função que recebe um inteiro positivo n e devolve 1 se n é primo, 0 em caso contrário.
