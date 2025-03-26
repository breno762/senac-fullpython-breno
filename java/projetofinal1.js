class Aluno {
    constructor(nome, matricula, curso) {
        this.nome = nome;
        this.matricula = matricula;
        this.notas = [];
        this.curso = curso;
    }

    adicionarNota(nota) {
        if (typeof nota === 'number' && nota >= 0 && nota <= 10) {
            this.notas.push(nota);
        } else {
            console.log("Nota inválida. A nota deve ser um número entre 0 e 10.");
        }
    }

    calcularMedia() {
        if (this.notas.length === 0) {
            return 0;
        }
        const soma = this.notas.reduce((acc, nota) => acc + nota, 0);
        return soma / this.notas.length;
    }
}

const aluno1 = new Aluno("João Silva", "123456", "Engenharia");
aluno1.adicionarNota(8);
aluno1.adicionarNota(7.5);
aluno1.adicionarNota(9);
console.log(`Média de ${aluno1.nome}: ${aluno1.calcularMedia()}`);