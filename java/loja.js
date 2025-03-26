class Produto {
    constructor(nome, preco, estoque) {
        this.nome = nome;
        this.preco = preco;
        this.estoque = estoque;
    }
}

class Cliente {
    constructor(nome, endereco) {
        this.nome = nome;
        this.endereco = endereco;
        this.carrinho = [];
    }

    adicionarAoCarrinho(produto, quantidade) {
        if (produto.estoque >= quantidade) {
            this.carrinho.push({ produto, quantidade });
            produto.estoque -= quantidade;
            console.log(`${quantidade} de ${produto.nome} adicionado ao carrinho.`);
        } else {
            console.log(`Desculpe, não há estoque suficiente para ${produto.nome}.`);
        }
    }
}

class Pedido {
    constructor(cliente) {
        this.cliente = cliente;
        this.itens = [];
        this.total = 0;
        this.status = 'Pendente';
    }

    adicionarItem(produto, quantidade) {
        this.itens.push({ produto, quantidade });
        this.total += produto.preco * quantidade;
    }

    finalizarCompra() {
        if (this.itens.length === 0) {
            console.log('O carrinho está vazio. Adicione itens antes de finalizar a compra.');
            return;
        }
        this.status = 'Finalizado';
        console.log(`Compra finalizada! Total: R$ ${this.total.toFixed(2)}`);
    }

    calcularFrete() {
        const taxaFrete = 10;
        return this.total > 100 ? 0 : taxaFrete;
    }
}

const produto1 = new Produto('Camiseta', 50, 10);
const produto2 = new Produto('Calça', 80, 5);

const cliente = new Cliente('João', 'Rua das Flores, 123');

cliente.adicionarAoCarrinho(produto1, 2);
cliente.adicionarAoCarrinho(produto2, 1);

const pedido = new Pedido(cliente);
cliente.carrinho.forEach(item => {
    pedido.adicionarItem(item.produto, item.quantidade);
});

const frete = pedido.calcularFrete();
pedido.total += frete;
console.log(`Frete: R$ ${frete}`);
pedido.finalizarCompra();