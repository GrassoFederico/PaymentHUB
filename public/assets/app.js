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
                stopLoader();

                let table = $('#tables').find('.active').first().data('table');
                
                if (getUrlVars()['tabella']) {
                    table = getUrlVars()['tabella'];

                    $('[data-table]').removeClass('active');

                    $(`[data-table="${table}"]`).addClass('active');
                }

                initDatatables(table);
                
                $('[data-table]').on('click', function () {
                    $('[data-table]').removeClass('active');

                    $(this).addClass('active');

                    let table = $(this).data('table');

                    initDatatables(table);
                });
            }
        });
    }

    function initDatatables(table) {

        startLoader();

        $.ajax({
            method: 'GET',
            url: `dati/${table}`,
            success: function (response) {

                let dataTableContainer = $('#datatable-container');

                dataTableContainer.empty();

                dataTableContainer.append(`
                    <div class="d-flex justify-content-between align-items-center">
                        <h5 class="text-uppercase">${table}</h5>
                        <button class="btn btn-sm btn-primary" data-bs-toggle="modal" data-bs-target="#${table}Modal">
                            Aggiungi
                        </button>
                    </div>
                    <hr/>
                `);

                let th = '';
                let tr = '';

                if (response[0]) {

                    th = Object.keys(response[0]).map(function(column) {
                        return `<th>${column}</th>`
                    }).join('');

                    th += '<th class="text-end">Azioni</th>';

                    tr = response.map(function (row) {
                        let td = '<tr>';

                        td += Object.entries(row).map(function (data) {
                            if (data[0] == 'id') {
                                return `<td>${data[1]}</td>`;
                            } else if ((data[0] == 'attivo') || (data[0] == 'test')) {                    
                                return `<td>
                                    <input data-id="${row.id}" class="form-check-input" type="checkbox" name="${data[0]}" value="${data[1] ? '0' : '1'}" ${data[1] ? 'checked' : ''}>
                                </td>`;
                            } else if ((data[0] == 'crea_pagamento') || (data[0] == 'recupera_pagamento') || (data[0] == 'esegui_pagamento') || (data[0] == 'verifica_pagamento')) {                    
                                return `<td>
                                    <input data-id="${row.id}" class="form-control form-control-sm" type="number" name="${data[0]}" value="${data[1]}">
                                </td>`;
                            } else if ((data[0] == 'id_rotta') || (data[0] == 'id_versione')) {
                                let t = (data[0] == 'id_rotta') ? 'rotta' : 'versione';

                                return `<td>
                                    <select data-id="${row.id}" data-campo="id" data-tabella="${t}" data-value="${data[1]}" name="id_${t}" class="form-select w-100" placeholder="Seleziona un ${t}" required>
                                    </select>
                                </td>`;
                            } else if ((data[0] == 'id_pagamento') || (data[0] == 'id_motore')) {
                                let t = (data[0] == 'id_pagamento') ? 'pagamento' : 'motore';

                                return `<td>
                                    <select data-id="${row.id}" data-campo="nome" data-tabella="${t}" data-value="${data[1]}" name="id_${t}" class="form-select w-100" placeholder="Seleziona un ${t}" required>
                                    </select>
                                </td>`;
                            } else if ((data[0] == 'id_nazione')) {
                                return `<td>
                                    <select data-id="${row.id}" data-campo="codice_2_caratteri" data-tabella="nazione" data-value="${data[1]}" name="id_nazione" class="form-select w-100" placeholder="Seleziona un nazione" required>
                                    </select>
                                </td>`;
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
                }

                dataTableContainer.append(`
                    <table id="datatable" class="table table-sm">
                        <thead>
                            <tr>
                                ${th}
                            </tr>
                        </thead>
                        <tbody>
                            ${tr}
                        </tbody>
                    </table>
                `);

                dataTableContainer.find('#datatable').first().DataTable();

                $('select[data-tabella]').each(function () {

                    let $select = $(this);

                    $.ajax({
                        url: '/select',
                        method: 'POST',
                        data: {
                            campo: $(this).data('campo'),
                            tabella: $(this).data('tabella')
                        },
                        success: function (response) {
                            response.map(function (data) {
                                $select.append(`
                                    <option value="${data.id}" ${($select.data('value') == data.id) ? 'selected' : ''}>${data.campo}</option>
                                `);
                            });
                        }
                    })
                });
            },
            complete: function() {

                stopLoader();

                $('select[data-id], input[data-id]').on('input, change', function() {

                    $.ajax({
                        method: 'PUT',
                        url: `/${table}`,
                        data: {
                            ide: $(this).data('id'),
                            campo: $(this).attr('name'),
                            valore: $(this).val()
                        }
                    })
                });

                $('button[data-id]').on('click', function () {

                    $.ajax({
                        method: 'DELETE',
                        url: `/${table}/${$(this).data('id')}`,
                        complete: () => {
                            window.location.href = `/?tabella=${table}`;
                        }
                    })
                });
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

    // Legge i valori in query string
    function getUrlVars()
    {
        var vars = [], hash;
        var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
        for(var i = 0; i < hashes.length; i++)
        {
            hash = hashes[i].split('=');
            vars.push(hash[0]);
            vars[hash[0]] = hash[1];
        }
        return vars;
    }

    // Select AJAX
    $('select[data-tabella]').one('click', function (e) {

        e.stopImmediatePropagation();
        e.stopPropagation();

        let $select = $(this);

        $.ajax({
            url: '/select',
            method: 'POST',
            data: {
                campo: $(this).data('campo'),
                tabella: $(this).data('tabella')
            },
            success: function (response) {
                
                $select.empty();
                response.map(function (data) {

                    $select.append(`
                        <option value="${data.id}">${data.campo}</option>
                    `);
                });
            }
        })
    });
});