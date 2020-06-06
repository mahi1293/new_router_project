
$(function () {
    console.log("Hello!");
});

$.ajax({
    url:  'list',
    type:  'get',
    dataType:  'json',
    success: function  (data) {
        let rows =  '';
        data.ipaddress.forEach(ipaddress =>
        {
            rows += `
            <tr>
                <td>${ipaddress.ip_address}</td>
                <td>${ipaddress.eth0}</td>
                <td>${ipaddress.host}</td>
                <td>${ipaddress.sap_id}</td>

                <td>
                    <button class="btn deleteBtn" data-id="${ipaddress.id}">Delete</button>
                    <button class="btn updateBtn" data-id="${ipaddress.id}">Update</button>
                </td>
            </tr>`;
    });
    $('#myTable > tbody').append(rows);
    $('.deleteBtn').each((i, elm) => {
        $(elm).on("click",  (e) => {
            deleteIpAddress($(elm))
        })
    })
    $('.updateBtn').each((i, elm) => {
        $(elm).on("click",  (e) => {
            updateIpAddress($(elm))
        })
    })

    }
});


function  deleteIpAddress(el){
    id  =  $(el).data('id')
    $.ajax({
        url:  `delete/${id}`,
        type:  'post',
        dataType:  'json',
        success:  function (data) {
            $(el).parents()[1].remove()
        },
        headers: { 'X_METHODOVERRIDE': 'DELETE' }
    });
}


function  updateIpAddress(el){
    id  =  $(el).data('id')
    $.ajax({
        url:  `update/${id}`,
        type:  'put',
        dataType:  'json',
        success:  function (data) {
            alert(data)
        },
        headers: { 'X_METHODOVERRIDE': 'PUT' }
    });
}
