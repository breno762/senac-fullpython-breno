from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    html = """
    <!DOCTYPE html>
<html lang="pt-BR">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Academia Corpo Forte</title>
  <style>
    body {
      font-family: 'Segoe UI', sans-serif;
      margin: 0;
      padding: 0;
      background: #f8f8f8;
    }

    header {
      background-color: #1b1b1b;
      color: #fff;
      padding: 30px 20px;
      text-align: center;
    }

    nav {
      display: flex;
      justify-content: center;
      background-color: #333;
      flex-wrap: wrap;
    }

    nav a {
      color: #fff;
      padding: 15px 20px;
      text-decoration: none;
      transition: background 0.3s;
    }

    nav a:hover {
      background-color: #555;
    }

    section {
      padding: 40px 20px;
      max-width: 1000px;
      margin: auto;
    }

    .hero {
      background: url('https://images.unsplash.com/photo-1571019613454-1cb2f99b2d8b') center/cover no-repeat;
      height: 350px;
      display: flex;
      align-items: center;
      justify-content: center;
      color: white;
      text-shadow: 2px 2px 5px black;
    }

    .services, .plans, .team {
      display: flex;
      flex-wrap: wrap;
      gap: 20px;
      justify-content: center;
    }

    .card {
      background: #fff;
      border-radius: 10px;
      padding: 20px;
      width: 280px;
      box-shadow: 0 4px 8px rgba(0,0,0,0.1);
      text-align: center;
    }

    .card img {
      max-width: 100%;
      border-radius: 8px;
    }

    form input, form textarea {
      width: 100%;
      padding: 10px;
      margin: 8px 0;
      border: 1px solid #ccc;
      border-radius: 5px;
    }

    form button {
      padding: 10px 20px;
      background-color: #1b1b1b;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    footer {
      background-color: #1b1b1b;
      color: white;
      text-align: center;
      padding: 20px;
    }

    @media (max-width: 600px) {
      .services, .plans, .team {
        flex-direction: column;
        align-items: center;
      }
    }
  </style>
</head>
<body>

  <header>
    <h1>Academia Corpo Forte</h1>
    <p>Treine forte. Viva melhor.</p>
  </header>

  <nav>
    <a href="#inicio">Início</a>
    <a href="#servicos">Serviços</a>
    <a href="#planos">Planos</a>
    <a href="#equipe">Equipe</a>
    <a href="#contato">Contato</a>
  </nav>

  <section class="hero" id="inicio">
    <h2>Seja bem-vindo à sua nova rotina saudável</h2>
  </section>

  <section id="servicos">
    <h2 style="text-align: center;">Nossos Serviços</h2>
    <div class="services">
      <div class="card">
        <h3>Musculação</h3>
        <p>Aparelhos modernos e acompanhamento profissional.</p>
      </div>
      <div class="card">
        <h3>Crossfit</h3>
        <p>Treinos de alta intensidade com instrutores experientes.</p>
      </div>
      <div class="card">
        <h3>Aulas em Grupo</h3>
        <p>Zumba, Funcional, Pilates, Yoga e mais!</p>
      </div>
    </div>
  </section>

  <section id="planos">
    <h2 style="text-align: center;">Planos</h2>
    <div class="plans">
      <div class="card">
        <h3>Plano Mensal</h3>
        <p>R$ 99,90</p>
        <p>Acesso total à academia.</p>
      </div>
      <div class="card">
        <h3>Plano Trimestral</h3>
        <p>R$ 269,90</p>
        <p>Desconto + Avaliação física grátis.</p>
      </div>
      <div class="card">
        <h3>Plano Anual</h3>
        <p>R$ 899,90</p>
        <p>Camiseta + 3 sessões com personal.</p>
      </div>
    </div>
  </section>

  <section id="equipe">
    <h2 style="text-align: center;">Nossa Equipe</h2>
    <div class="team">
      <div class="card">
        <img src="https://randomuser.me/api/portraits/men/75.jpg" alt="Instrutor João">
        <h4>João Silva</h4>
        <p>Personal Trainer</p>
      </div>
      <div class="card">
        <img src="https://randomuser.me/api/portraits/women/65.jpg" alt="Instrutora Ana">
        <h4>Ana Souza</h4>
        <p>Instrutora de Pilates</p>
      </div>
      <div class="card">
        <img src="https://randomuser.me/api/portraits/men/52.jpg" alt="Nutricionista Carlos">
        <h4>Carlos Lima</h4>
        <p>Nutricionista Esportivo</p>
      </div>
    </div>
  </section>

  <section id="contato">
    <h2 style="text-align: center;">Fale Conosco</h2>
    <form onsubmit="enviarFormulario(event)">
      <input type="text" placeholder="Seu nome" required>
      <input type="email" placeholder="Seu e-mail" required>
      <textarea placeholder="Sua mensagem" rows="5" required></textarea>
      <button type="submit">Enviar</button>
    </form>
    <p id="mensagem-sucesso" style="color: green; display: none;">Mensagem enviada com sucesso!</p>
  </section>

  <footer>
    <p>&copy; 2025 Academia Corpo Forte. Todos os direitos reservados.</p>
  </footer>

  <script>
    function enviarFormulario(event) {
      event.preventDefault();
      document.getElementById("mensagem-sucesso").style.display = "block";
    }
  </script>

</body>
</html>
    """
    return HttpResponse(html)
