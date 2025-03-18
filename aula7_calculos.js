1.
function calcularMedia() {
    let notas = [];
    let soma = 0;
    for (let i = 1; i <= 4; i++) {
        let nota = parseFloat(prompt(`Insira a nota ${i} (de 0 a 10):`));
        while (nota < 0 || nota > 10 || isNaN(nota)) {
            nota = parseFloat(prompt(`Nota inválida. Insira a nota ${i} (de 0 a 10):`));
        }
        
        notas.push(nota);
        soma += nota;
    }
    let media = soma / notas.length;
    console.log(`A média das notas é: ${media.toFixed(2)}`);
    if (media >= 7) {
        console.log("Aprovado");
    } else {
        console.log("Reprovado");
    }
}
calcularMedia();

2.
function somaNumerosPares(inicio, fim) {
    let soma = 0;
    for (let i = inicio; i <= fim; i++) {
        if (i % 2 === 0) {
            soma += i;
        }
    }

    return soma;
}
const inicio = parseInt(prompt("Digite o número de início do intervalo:"));
const fim = parseInt(prompt("Digite o número de fim do intervalo:"));

if (!isNaN(inicio) && !isNaN(fim) && inicio <= fim) {
    const resultado = somaNumerosPares(inicio, fim);
    console.log(`A soma dos números pares entre ${inicio} e ${fim} é: ${resultado}`);
} else {
    console.log("Por favor, insira números válidos e certifique-se de que o início é menor ou igual ao fim.");
}

3.
function ehPalindromo(str) {
    const strLimpa = str.replace(/\s+/g, '').toLowerCase();
    
    const strInvertida = strLimpa.split('').reverse().join('');
    
    return strLimpa === strInvertida;
}

const entrada = prompt("Digite uma palavra ou frase:");

if (ehPalindromo(entrada)) {
    console.log("É palíndromo");
} else {
    console.log("Não é palíndromo");
}
            

