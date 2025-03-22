1.
function somaMatrizes(matrizA, matrizB) {
    if (matrizA.length !== 3 || matrizB.length !== 3 ||
        matrizA[0].length !== 3 || matrizB[0].length !== 3) {
        throw new Error("As matrizes devem ser 3x3.");
    }

    const matrizResultado = [];

    for (let i = 0; i < 3; i++) {
        matrizResultado[i] = [];
        for (let j = 0; j < 3; j++) {
            matrizResultado[i][j] = matrizA[i][j] + matrizB[i][j];
        }
    }

    return matrizResultado;
}

const matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

const matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
];

const resultado = somaMatrizes(matriz1, matriz2);
console.log(resultado);

2.
function transporMatriz(matriz) {
    if (matriz.length !== 3 || matriz.some(linha => linha.length !== 3)) {
        throw new Error("A matriz deve ser 3x3.");
    }

    const matrizTransposta = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ];

    for (let i = 0; i < 3; i++) {
        for (let j = 0; j < 3; j++) {
            matrizTransposta[j][i] = matriz[i][j];
        }
    }

    return matrizTransposta;
}

const matrizOriginal = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
];

const matrizTransposta = transporMatriz(matrizOriginal);
console.log(matrizTransposta);

3.
function multiplicarMatrizes(matrizA, matrizB) {
    if (matrizA.length !== 2 || matrizA[0].length !== 2 || matrizB.length !== 2 || matrizB[0].length !== 2) {
        throw new Error("Ambas as matrizes devem ser 2x2.");
    }

    let resultado = [
        [0, 0],
        [0, 0]
    ];

    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
            resultado[i][j] = matrizA[i][0] * matrizB[0][j] + matrizA[i][1] * matrizB[1][j];
        }
    }

    return resultado;
}

let matrizA = [
    [1, 2],
    [3, 4]
];

let matrizB = [
    [5, 6],
    [7, 8]
];

let resultado = multiplicarMatrizes(matrizA, matrizB);
console.log("Resultado da multiplicação:");
console.log(resultado);