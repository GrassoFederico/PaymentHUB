jQuery(() => {

    // Inizializza l'elenco delle tabelle
    initTables();

    // Inizializza l'elenco delle tabelle
    function initTables() {

        startLoader();

        $.ajax({
            method: 'GET',
            url: '/tabelle',
            success: function (response) {
                response.map((row, index) => {
                    let $tables = $('#tables');

                    let active = index ? '' : 'active';
                    let ariaCurrent = index ? '' : 'aria-current="true"';

                    let table = row['Tables_in_payments_hub'];

                    $tables.append(`
                        <a href="#" data-table="${table}" class="list-group-item list-group-item-action ${active}" ${ariaCurrent}>
                            <small class="text-uppercase">${table}</small>
                        </a>
                    `);
                });
            },
            complete: function () {
                initDatatables();
            }
        });
    }

    function initDatatables() {

        let table = $('#tables').find('.active').first().data('table');

        $.ajax({
            method: 'GET',
            url: `dati/motore`,
            success: function (response) {
                let dataTable = $('#datatable');

                dataTable.before(`
                    <div class="d-flex justify-content-between align-items-center">
                        <h5 class="text-uppercase">${table}</h5>
                        <button class="btn btn-sm btn-primary" data-bs-toggle="modal" data-bs-target="#${table}Modal">
                            Aggiungi
                        </button>
                    </div>
                    <hr/>
                `);

                let th = Object.keys(response[0]).map(function(column) {
                    return `<th>${column}</th>`
                }).join('');

                th += '<th class="text-end">Azioni</th>';

                let tr = response.map(function (row) {
                    let td = '<tr>';

                    td += Object.entries(row).map(function (data) {
                        if (data[0] == 'id') {
                            return `<td>${data[1]}</td>`;
                        } else {                        
                            return `<td>
                                <input data-id="${row.id}" class="form-control form-control-sm" name="${data[0]}" value="${data[1]}">
                            </td>`;
                        }

                    }).join('');

                    td += `
                        <td class="text-end">
                            <button data-id="${row.id}" class="btn btn-sm btn-danger">Cancella</button>
                        </td>
                    `;

                    td += '</tr>';

                    return td;
                }).join('');

                dataTable.append(`
                    <thead>
                        <tr>
                            ${th}
                        </tr>
                    </thead>
                    <tbody>
                        ${tr}
                    </tbody>
                `);

                $(dataTable).DataTable();
            },
            complete: function() {

                $('input[data-id').on('input', function() {
                    
                    $.ajax({
                        method: 'PUT',
                        url: '/motore',
                        data: {
                            ide: $(this).data('id'),
                            campo: $(this).attr('name'),
                            valore: $(this).val()
                        },
                        success: function(response) {
                            alert(response);
                        }
                    })
                });

                $('button[data-id]').on('click', function () {
                    
                    $.ajax({
                        method: 'DELETE',
                        url: `/motore/${$(this).data('id')}`,
                        success: function(response) {
                            alert(response);

                            window.location.reload();
                        }
                    })
                });

                stopLoader();
            }
        });

    }

    // Controlli di gestione per il loader
    function startLoader() {

        $('#loader').show();
    }

    function stopLoader() {
        $('#loader').hide();
    }
});