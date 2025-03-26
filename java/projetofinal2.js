class Professor {
    constructor(nome, departamento) {
        this.nome = nome;
        this.departamento = departamento;
        this.disciplinas = [];
    }

    atribuirDisciplina(disciplina) {
        if (typeof disciplina === 'string' && disciplina.trim() !== '') {
            this.disciplinas.push(disciplina);
        } else {
            console.log("Disciplina inválida. A disciplina deve ser uma string não vazia.");
        }
    }

    listarTurmas() {
        if (this.disciplinas.length === 0) {
            console.log(`${this.nome} não tem disciplinas atribuídas.`);
            return;
        }
        console.log(`Disciplinas atribuídas a ${this.nome}:`);
        this.disciplinas.forEach((disciplina, index) => {
            console.log(`${index + 1}. ${disciplina}`);
        });
    }
}

const professor1 = new Professor("Mariana Costa", "Física");
professor1.atribuirDisciplina("Mecânica");
professor1.atribuirDisciplina("Termologia");
professor1.listarTurmas();