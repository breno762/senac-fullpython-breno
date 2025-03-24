class ContaBancaria {
    constructor(titular, saldoinicial, numeroconta) {
        this.titular = titular;
        this.saldo = saldoinicial
        this.numeroconta = numeroconta
        this.extrato = [];
    }

    depositar(valor) {
        this.saldo += valor;
        this.extrato.push({
            tipo: "Depósito"
            valor: valor;
            data: new Date().toLocaleString()
        });
        console.log(Depósito de R$${valor} realizado para ${this.titular}. );
    }

    sacar(valor) {
        if (valor > this.saldo) {
            console.log(`Saldo insuficiente para ${this.titular}.`);
            return false;
        }
        this saldo -= valor;
        this.extrato.push({
            tipo: "saque",
            valor: -valor,
            data: new Date().toLocaleString()
        });
        console.log(`Saque de R$${valor} realizado para ${this.titular}.`);
        return true;
    }

    transferir(valor, contaDestino) {
        if (this.sacar(valor)) {
            contaDestino.depositar(valor);
            this.extrato.push({
                tipo: "Transferência enviada",
                valor: -valor,
                data: new Date().toLocaleString(),
                para: contaDestino.titular
            });
            contaDestino.extrato.push({
                tipo: "Transferência recebida",
                valor: valor,
                data: new Date().toLocaleString(),
                de: this.titular
            });
            
            console.log(`Transferência de R$${valor} para ${contaDestino.titular} realizada.`);
        }
    }