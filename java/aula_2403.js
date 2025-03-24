let cliente1 = {
    nome: "Jõao Silva"
    saldo = 1000
    conta = 12345-6
}

let cliente2 = {
    nome: "Maria Souza",
    saldo = 2500
    conta = "78901-2"
}

function depositar(cliente, valor) {
    cliente.saldo += valor;
    console.log (Depósito de R$${valor} realizado. Novo saldo: R$${cliente.saldo}`);
}
