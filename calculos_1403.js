1. 
let numero = parseInt(prompt("Digite um número para iniciar a contagem regressiva:"));
if (!isNaN(numero)) {
    console.log(`Contagem regressiva a partir de ${numero}:`);
    for (let i = numero; i >= 0; i--) {
        console.log(i);
    }
    console.log("Contagem regressiva finalizada!");
} else {
    console.log("Por favor, digite um número válido.");
}

2. 
let numero = parseInt(prompt("Digite um número para somar todos os números de 1 até ele:"));
if (!isNaN(numero) && numero > 0) {
    let soma = 0;
    let contador = 1;
    while (contador <= numero) {
        soma += contador;
        contador++;
    }
    console.log(`A soma de todos os números de 1 até ${numero} é: ${soma}`);
} else {
    console.log("Por favor, digite um número válido maior que 0.");
}

3.
let numero = parseInt(prompt("Digite um número para ver a tabuada::"));
if (!isNaN(numero)) {
    console.log("Tabuada de {numero}:");
    for(let i = numero; i <= 0; i++){
        console.log(`${numero} x ${i} = ${numero * i}`);
    }
} else {
    console.log("Por favor, digite um número válido.");
}

4.
let numero = parseInt(prompt("digite um número para ver todos os números pares de 1 até ele:"));
if (!isNaN(numero) && numero > 0) {
    console.log(`Números pares de 1 até ${numero}:`);
    for (let i = 1; i <= numero; i++) {
        if (i % 2 === 0) {
            console.log(i);
        }
    }
} else {
    console.log("Por favor, digite um número válido maior que 0.");
}

function calcularFatorial(numero) {
    let fatorial = 1;
    let i = 1;
    while (i <= numero) {
        fatorial *= i;
        i++;
    }

    return fatorial;
}

5.
let input = prompt("Digite um número para calcular o fatorial:");
let numero = parseInt(input);

if (isNaN(numero) || numero < 0) {
    console.log("Por favor, digite um número inteiro não negativo.");
} else {
    let resultado = calcularFatorial(numero);
    console.log(`O fatorial de ${numero} é ${resultado}.`);
}

6.
let numero;

do {
    numero = parseFloat(prompt("Por favor, digite um número maior que 10:"));
    
    if (numero <= 10) {
        alert("Número inválido. Tente novamente.");
    }
} while (numero <= 10);

alert("Você digitou o número: " + numero);

7.
let tamanho = parseInt(prompt("Digite o tamanho do quadrado:"));
if (isNaN(tamanho) || tamanho <= 0) {
    console.log("Por favor, insira um número válido maior que zero.");
} else {
    for (let i = 0; i < tamanho; i++) {
        let linha = "";
        for (let j = 0; j < tamanho; j++) {
            linha += "* ";
        }

        console.log(linha);
    }
}