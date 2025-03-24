function somaArray(numeros) {
    let soma = 0;
    for (let i = 0; i < numeros.length; i++) {
        soma += numeros[i];
    }
    return soma;
}

1.
function somarNumeros(array) {
    return array.reduce((acumulador, valorAtual) => acumulador + valorAtual, 0);
}

const numeros = [1, 2, 3, 4, 5];
const soma = somarNumeros(numeros);

console.log(soma);

2.
function ordenarStrings(array) {
    return array.slice().sort();
}

const strings = ["banana", "maçã", "laranja", "abacaxi"];
const stringsOrdenadas = ordenarStrings(strings);

console.log(stringsOrdenadas);

3.
function removerDuplicados(array) {
    return [...new Set(array)];
}

const numeros = [1, 2, 2, 3, 4, 4, 5];
const numerosSemDuplicados = removerDuplicados(numeros);

console.log(numerosSemDuplicados);