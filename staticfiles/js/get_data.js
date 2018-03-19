
function getFormData(form) {
    var unindexed_array = form.serializeArray();
    var indexed_array = {};

    $.map(unindexed_array, function (n, i) {
        indexed_array[n['name']] = n['value'];
        console.log(n['name'], n['value'])
    });

    return indexed_array;
}


function update_user(id) {
    var form_data = $('#user-form');
    $.ajax({
        url: 'update_user_data/' + id + '/',
        type: 'POST',
        data: getFormData(form_data),
        dataType: 'json',
        success: function (response) {
            if (response.errors) {
                console.log(response.errors);
            }
            else {
                document.getElementById('users_list').innerHTML = response.html;
                console.log('Object successfully updated');
            }
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    })
}

function fill_form(id, url, element_id) {
    $.ajax({
        url: url + id + '/',
        type: 'GET',
        dataType: 'json',
        success: function (response) {
            if (response.errors) {
                console.log(response.errors);
            }
            else {
                document.getElementById(element_id).innerHTML = response.html;
            }
        },
        error: function (xhr, status, error) {
            console.log('error =', error)
        }
    });
}