$(document).ready(function () {
    
    portugues = {
        "sEmptyTable": "Nenhum registro encontrado",
        "sInfo": "Mostrando de _START_ até _END_ de _TOTAL_ registros",
        "sInfoEmpty": "Mostrando 0 até 0 de 0 registros",
        "sInfoFiltered": "(Filtrados de _MAX_ registros)",
        "sInfoPostFix": "",
        "sInfoThousands": ".",
        "sLengthMenu": "_MENU_ resultados por página",
        "sLoadingRecords": "Carregando...",
        "sProcessing": "Processando...",
        "sZeroRecords": "Nenhum registro encontrado",
        "sSearch": "Pesquisar",
        "oPaginate": {
            "sNext": "Próximo",
            "sPrevious": "Anterior",
            "sFirst": "Primeiro",
            "sLast": "Último"
        },
        "oAria": {
            "sSortAscending": ": Ordenar colunas de forma ascendente",
            "sSortDescending": ": Ordenar colunas de forma descendente"
        },
        "select": {
            "rows": {
                "_": "Selecionado %d linhas",
                "0": "Nenhuma linha selecionada",
                "1": "Selecionado 1 linha"
            }
        },
        "buttons": {
            "copy": "Copiar para a área de transferência",
            "copyTitle": "Cópia bem sucedida",
            "copySuccess": {
                "1": "Uma linha copiada com sucesso",
                "_": "%d linhas copiadas com sucesso"
            }
        }
    }

    var tableRecebedores = $("#table-recebedores").DataTable({
        "ajax": { url: "https://api.pagar.me/1/recipients/?api_key=" + pagarme_api, dataSrc: "" },
        "columns": [
            { "data": "register_information.name", "defaultContent": "Sem dados" },
            { "data": "id", "defaultContent": "Sem dados" },
            { "data": "bank_account.bank_code", "defaultContent": "Sem dados" },
            { "data": "bank_account.agencia", "defaultContent": "Sem dados" },
            { "data": "bank_account.conta", "defaultContent": "Sem dados" },
            { "data": "bank_account.conta_dv", "defaultContent": "Sem dados" },
            { "data": "bank_account.document_number", "defaultContent": "Sem dados" },
            { "data": "status", "defaultContent": "Sem dados" },
            { "data": "last_transfer", "defaultContent": "Sem dados" },
            { "data": "date_created", "defaultContent": "Sem dados" },
        ],
        columnDefs: [{
            targets: 9,
            render: $.fn.dataTable.render.moment('YYYY-MM-DDTHH:mm:ss.SSSZ', 'DD/MM/YYYY - HH:mm:ss')
        }],
        "scrollY": "350px",
        "scrollX": true,
        "oLanguage": portugues
    });

    var tableSaldo = $("#table-saldo").DataTable({
        "ajax": {
                    url: "https://api.pagar.me/1/balance/?api_key=" + pagarme_api,
                    dataSrc: function (data) {
                        var a = [];
                        a.push(data)
                        return a;
                    },
                },
        "columns": [
            { "data": "waiting_funds.amount", "defaultContent": "Sem dados" },
            { "data": "transferred.amount", "defaultContent": "Sem dados" },
            { "data": "available.amount", "defaultContent": "Sem dados" },
        ],
        columnDefs: [{
            targets: [0,1,2],
            render: function ( data, type, row, meta ) {
                var valor = parseFloat(data)/100.00;
                return "R$ " + valor.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');;
              }
        }],
        "dom": 't',
        "oLanguage": portugues
    });

    var tableTransacoes = $("#table-transacoes").DataTable({
        "ajax": {
                    url: "https://api.pagar.me/1/transactions?api_key=" + pagarme_api,
                    dataSrc: ""
                },
        "columns": [
            { "data": "id", "defaultContent": "Sem dados" },
            { "data": "status", "defaultContent": "Sem dados" },
            { "data": "amount", "defaultContent": "Sem dados" },
            { "data": "customer.name", "defaultContent": "Sem dados" },
            { "data": "date_created", "defaultContent": "Sem dados" },
            { "data": "split_rules[, ].recipient_id"},
            { "data": "split_rules[, ].id"}
        ],
        columnDefs: [
            {
            targets: [2],
            render: function ( data, type, row, meta ) {
                var valor = parseFloat(data)/100.00;
                return "R$ " + valor.toFixed(2).replace(/\d(?=(\d{3})+\.)/g, '$&,');;
              }
            },
            {
                targets: 4,
                render: $.fn.dataTable.render.moment('YYYY-MM-DDTHH:mm:ss.SSSZ', 'DD/MM/YYYY - HH:mm:ss')
            }
        ],
        "scrollY": "200px",
        "scrollX": true,
        "oLanguage": portugues
    });

    
    $("#busca-saldo").on("click", function () {
        // set the ajax option value of the dataTable here according to the select's value
        tableSaldo.ajax.url(
                "https://api.pagar.me/1/recipients/" + encodeURIComponent($("#id-recebedor").val()) + "/balance?api_key=" + pagarme_api
            ).load();
    });

    setInterval(function () {
        tableRecebedores.ajax.reload(null, false);
    }, 5000);

    setInterval(function () {
        tableTransacoes.ajax.reload(null, false);
    }, 5000);
    
})