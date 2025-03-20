function somaArray(numeros) {
    let soma = 0;
    for (let i = 0; i < numeros.length; i++) {
        soma += numeros[i];
    }
    return soma;
}

const arrayDeNumeros = [1, 2, 3, 4, 5];
const resultado = somaArray(arrayDeNumeros);
console.log(resultado);

function somaArray(strings) {
    let strings 