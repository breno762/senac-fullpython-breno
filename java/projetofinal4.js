class Escola {
    constructor(nome) {
        this.nome = nome;
        this.listaAlunos = [];
        this.listaProfessores = [];
    }

    matricularAluno(aluno) {
        if (aluno && aluno.nome && aluno.matricula) {
            this.listaAlunos.push(aluno);
            console.log(`Aluno ${aluno.nome} matriculado na escola ${this.nome}.`);
        } else {
            console.log("Aluno inválido. O aluno deve ter um nome e uma matrícula.");
        }
    }

    contratarProfessor(professor) {
        if (professor && professor.nome && professor.departamento) {
            this.listaProfessores.push(professor);
            console.log(`Professor ${professor.nome} contratado na escola ${this.nome}.`);
        } else {
            console.log("Professor inválido. O professor deve ter um nome e um departamento.");
        }
    }

    gerarRelatorio() {
        console.log(`Relatório da Escola: ${this.nome}`);
        console.log(`Alunos Matriculados: ${this.listaAlunos.length}`);
        this.listaAlunos.forEach(aluno => {
            console.log(`- Nome: ${aluno.nome}, Matrícula: ${aluno.matricula}`);
        });

        console.log(`Professores Contratados: ${this.listaProfessores.length}`);
        this.listaProfessores.forEach(professor => {
            console.log(`- Nome: ${professor.nome}, Departamento: ${professor.departamento}`);
        });
    }
}

const escola = new Escola("Escola Fundamental");

const aluno1 = { nome: "Brenda", matricula: "123456" };
const aluno2 = { nome: "Luísa Almeida", matricula: "654321" };

const professor1 = { nome: "Lucas Lima", departamento: "Física" };
const professor2 = { nome: "Mariana Costa", departamento: "Geografia" };

escola.matricularAluno(aluno1);
escola.matricularAluno(aluno2);
escola.contratarProfessor(professor1);
escola.contratarProfessor(professor2);

escola.gerarRelatorio();