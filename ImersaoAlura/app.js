function pesquisar() {
    // Seleciona a seção onde os resultados da pesquisa serão exibidos pelo seu ID.
    let section = document.getElementById("resultados-pesquisa"); 

    let campoPesquisa = document.getElementById("campo-pesquisa").value

    // se campoPesquisa for uma string sem nada
    if (campoPesquisa == "" ){
        section.innerHTML = "<p>Nada foi encontrado. Você precisa digitar o nome de um jogo ou estilo relacionado</p>"
        return 
    }

    // Para pesquisar um nome e ele aparecer independente se é com letra maiúscula ou minúscula
    campoPesquisa = campoPesquisa.toLowerCase( )
  
    // Inicializa uma string vazia para armazenar os resultados da pesquisa.
    let resultados = "";
    let titulo = "";
    let descricao = "";
    let tags = "";
  
    // Itera sobre cada item (dado) na lista de dados.
    for (let dado of dados) {
      titulo = dado.titulo.toLowerCase( )
      descricao = dado.descricao.toLowerCase( )
      tags = dado.tags.toLowerCase( )
      // se titulo includes campoPesquisa
      if (titulo.includes(campoPesquisa) || descricao.includes(campoPesquisa) || tags.includes(campoPesquisa)) {
        // cria um novo elemento
        resultados += `
        <div class="item-resultado">
          <h2>
            <a href="${dado.link}" target="_blank">${dado.titulo}</a>
          </h2>
          <p class="descricao-meta">${dado.descricao}</p>
          <a href=${dado.link} target="_blank">Mais informações</a>
        </div>
      `;
      }
      // Constrói o HTML para cada resultado, incluindo o título, descrição e link.
      // O template literal (``) permite inserir variáveis diretamente no texto.
      
    }

    if (!resultados) {
      resultados = "<p>Nada foi encontrado</p>"
    }
  
    // Atribui o HTML gerado para a seção de resultados, substituindo o conteúdo anterior.
    section.innerHTML = resultados;
  }